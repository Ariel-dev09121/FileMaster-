"""
organizer.py
Contiene la lógica para escanear una carpeta, clasificar archivos,
moverlos a su carpeta correspondiente y registrar todo en un log.
"""

import os
import shutil
from datetime import datetime
from config import obtener_categoria, CATEGORIAS


class FileOrganizer:
    def __init__(self, carpeta_origen: str):
        self.carpeta_origen = carpeta_origen
        self.carpeta_logs = os.path.join(carpeta_origen, "logs")
        self.archivo_log = None
        self.total_movidos = 0
        self.errores = []

    def _preparar_log(self):
        """Crea la carpeta logs/ y el archivo de log del día si no existen."""
        os.makedirs(self.carpeta_logs, exist_ok=True)
        nombre_log = datetime.now().strftime("%Y-%m-%d") + ".log"
        self.archivo_log = os.path.join(self.carpeta_logs, nombre_log)

    def _escribir_log(self, mensaje: str):
        """Escribe una línea en el log, con marca de tiempo."""
        hora = datetime.now().strftime("%H:%M:%S")
        linea = f"[{hora}] {mensaje}\n"
        with open(self.archivo_log, "a", encoding="utf-8") as f:
            f.write(linea)

    def _crear_carpetas_destino(self):
        """Crea las carpetas de categorías (Images, Videos, etc.) si no existen."""
        for categoria in CATEGORIAS.keys():
            ruta = os.path.join(self.carpeta_origen, categoria)
            os.makedirs(ruta, exist_ok=True)

    def escanear_archivos(self):
        """
        Devuelve la lista de archivos (no carpetas) que hay directamente
        dentro de la carpeta origen. Ignora la carpeta logs y las carpetas
        de categorías ya creadas, para no mover archivos que ya organizó.
        """
        nombres_carpetas_categoria = set(CATEGORIAS.keys())
        archivos = []
        for nombre in os.listdir(self.carpeta_origen):
            ruta_completa = os.path.join(self.carpeta_origen, nombre)
            if nombre == "logs":
                continue
            if nombre in nombres_carpetas_categoria:
                continue
            if os.path.isfile(ruta_completa):
                archivos.append(nombre)
        return archivos

    def _nombre_disponible(self, carpeta_destino: str, nombre_archivo: str) -> str:
        """
        Si ya existe un archivo con el mismo nombre en destino, le agrega
        un sufijo numérico para no sobrescribir. Ej: foto.png -> foto (1).png
        """
        ruta = os.path.join(carpeta_destino, nombre_archivo)
        if not os.path.exists(ruta):
            return nombre_archivo

        nombre_base, extension = os.path.splitext(nombre_archivo)
        contador = 1
        while True:
            nuevo_nombre = f"{nombre_base} ({contador}){extension}"
            if not os.path.exists(os.path.join(carpeta_destino, nuevo_nombre)):
                return nuevo_nombre
            contador += 1

    def organizar(self, callback_progreso=None):
        """
        Ejecuta todo el proceso de organización.

        callback_progreso: función opcional que se llama después de mover
        cada archivo, recibe (nombre_archivo, categoria, actual, total).
        Sirve para actualizar la interfaz gráfica en tiempo real.
        """
        self._preparar_log()
        self._crear_carpetas_destino()

        archivos = self.escanear_archivos()
        total = len(archivos)
        self.total_movidos = 0
        self.errores = []

        for i, nombre_archivo in enumerate(archivos, start=1):
            ruta_origen = os.path.join(self.carpeta_origen, nombre_archivo)
            _, extension = os.path.splitext(nombre_archivo)
            categoria = obtener_categoria(extension)
            carpeta_destino = os.path.join(self.carpeta_origen, categoria)

            nombre_final = self._nombre_disponible(carpeta_destino, nombre_archivo)
            ruta_destino = os.path.join(carpeta_destino, nombre_final)

            try:
                shutil.move(ruta_origen, ruta_destino)
                self.total_movidos += 1
                self._escribir_log(f"Moved: {nombre_archivo} -> {categoria}/{nombre_final}")
            except Exception as e:
                self.errores.append((nombre_archivo, str(e)))
                self._escribir_log(f"ERROR: {nombre_archivo} -> {e}")

            if callback_progreso:
                callback_progreso(nombre_archivo, categoria, i, total)

        self._escribir_log(f"Resumen: {self.total_movidos}/{total} archivos organizados.")
        return self.total_movidos, total, self.errores
