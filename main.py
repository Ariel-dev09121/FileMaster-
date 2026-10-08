"""
main.py
Interfaz gráfica de File Master.
Al abrir, primero pregunta el idioma (Español / English) y luego
muestra la ventana principal con los textos en ese idioma.

Ejecutar con: python main.py
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading

from organizer import FileOrganizer
from idiomas import t, IDIOMAS_DISPONIBLES


# =======================================================
#  VENTANA 1: SELECTOR DE IDIOMA
# =======================================================

class SelectorIdioma:
    """
    Primera ventana que se muestra al abrir el programa.
    Pregunta qué idioma usar y, al elegir, abre la ventana principal.

    Los botones se generan automáticamente a partir de la lista
    IDIOMAS_DISPONIBLES (en idiomas.py), así que agregar un idioma nuevo
    no requiere tocar esta clase: solo agregar su bloque de textos y su
    entrada en esa lista.
    """

    COLUMNAS = 2  # cuántos botones de idioma por fila

    def __init__(self, root):
        self.root = root
        self.root.title("File Master")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        FONDO = "#1e1e2e"
        ACENTO = "#89b4fa"
        TEXTO = "#cdd6f4"

        # Tamaño de ventana dinámico según cuántos idiomas haya
        filas = -(-len(IDIOMAS_DISPONIBLES) // self.COLUMNAS)  # redondeo hacia arriba
        alto = 160 + filas * 60
        self.root.geometry(f"380x{alto}")

        tk.Label(
            root, text="🌐 Selecciona tu idioma\nSelect your language",
            font=("Segoe UI", 13, "bold"), bg=FONDO, fg=ACENTO, justify="center"
        ).pack(pady=(25, 20))

        frame_botones = tk.Frame(root, bg=FONDO)
        frame_botones.pack()

        for indice, idioma in enumerate(IDIOMAS_DISPONIBLES):
            fila = indice // self.COLUMNAS
            columna = indice % self.COLUMNAS
            texto_boton = f"{idioma['bandera']} {idioma['nombre']}"

            btn = tk.Button(
                frame_botones, text=texto_boton, font=("Segoe UI", 11),
                bg="#313244", fg=TEXTO, activebackground="#45475a",
                relief="flat", padx=18, pady=10, cursor="hand2", width=14,
                command=lambda codigo=idioma["codigo"]: self.elegir_idioma(codigo)
            )
            btn.grid(row=fila, column=columna, padx=8, pady=6)

    def elegir_idioma(self, idioma_elegido: str):
        # Cerramos esta ventana y abrimos la app principal con el idioma elegido
        self.root.destroy()
        nueva_raiz = tk.Tk()
        FileMasterApp(nueva_raiz, idioma_elegido)
        nueva_raiz.mainloop()


# =======================================================
#  VENTANA 2: APLICACIÓN PRINCIPAL
# =======================================================

class FileMasterApp:
    def __init__(self, root, idioma="es"):
        self.root = root
        self.idioma = idioma
        self.root.title(t(self.idioma, "titulo_ventana"))
        self.root.geometry("520x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.carpeta_seleccionada = tk.StringVar(value=t(self.idioma, "carpeta_default"))
        self.organizando = False

        self._construir_interfaz()

    # ---------- INTERFAZ ----------

    def _construir_interfaz(self):
        FONDO = "#1e1e2e"
        ACENTO = "#89b4fa"
        TEXTO = "#cdd6f4"

        titulo = tk.Label(
            self.root, text=t(self.idioma, "titulo_app"), font=("Segoe UI", 20, "bold"),
            bg=FONDO, fg=ACENTO
        )
        titulo.pack(pady=(20, 5))

        subtitulo = tk.Label(
            self.root, text=t(self.idioma, "subtitulo"),
            font=("Segoe UI", 10), bg=FONDO, fg=TEXTO
        )
        subtitulo.pack(pady=(0, 20))

        btn_seleccionar = tk.Button(
            self.root, text=t(self.idioma, "btn_seleccionar"), command=self.seleccionar_carpeta,
            font=("Segoe UI", 11), bg="#313244", fg=TEXTO,
            activebackground="#45475a", relief="flat", padx=10, pady=8, cursor="hand2"
        )
        btn_seleccionar.pack(pady=5)

        self.label_carpeta = tk.Label(
            self.root, textvariable=self.carpeta_seleccionada,
            font=("Segoe UI", 9), bg=FONDO, fg="#a6adc8", wraplength=480
        )
        self.label_carpeta.pack(pady=(0, 15))

        self.btn_organizar = tk.Button(
            self.root, text=t(self.idioma, "btn_organizar"), command=self.iniciar_organizacion,
            font=("Segoe UI", 12, "bold"), bg=ACENTO, fg="#1e1e2e",
            activebackground="#74a8f5", relief="flat", padx=20, pady=10, cursor="hand2"
        )
        self.btn_organizar.pack(pady=10)

        self.progreso = ttk.Progressbar(self.root, length=440, mode="determinate")
        self.progreso.pack(pady=10)

        self.label_estado = tk.Label(
            self.root, text="", font=("Segoe UI", 9), bg=FONDO, fg=TEXTO
        )
        self.label_estado.pack(pady=(0, 5))

        self.caja_log = tk.Text(
            self.root, height=8, width=58, bg="#11111b", fg="#a6e3a1",
            font=("Consolas", 9), relief="flat"
        )
        self.caja_log.pack(pady=10)
        self.caja_log.config(state="disabled")

    # ---------- LÓGICA DE LA INTERFAZ ----------

    def seleccionar_carpeta(self):
        if self.organizando:
            return
        carpeta = filedialog.askdirectory(title=t(self.idioma, "dialogo_seleccionar_carpeta"))
        if carpeta:
            self.carpeta_seleccionada.set(carpeta)
            self._limpiar_log()

    def _limpiar_log(self):
        self.caja_log.config(state="normal")
        self.caja_log.delete("1.0", tk.END)
        self.caja_log.config(state="disabled")

    def _agregar_log(self, texto: str):
        self.caja_log.config(state="normal")
        self.caja_log.insert(tk.END, texto + "\n")
        self.caja_log.see(tk.END)
        self.caja_log.config(state="disabled")

    def iniciar_organizacion(self):
        carpeta = self.carpeta_seleccionada.get()
        if carpeta == t(self.idioma, "carpeta_default") or not carpeta:
            messagebox.showwarning(t(self.idioma, "alerta_titulo"), t(self.idioma, "alerta_sin_carpeta"))
            return

        if self.organizando:
            return

        self.organizando = True
        self.btn_organizar.config(state="disabled", text=t(self.idioma, "btn_organizando"))
        self._limpiar_log()
        self.progreso["value"] = 0

        hilo = threading.Thread(target=self._ejecutar_organizacion, args=(carpeta,), daemon=True)
        hilo.start()

    def _ejecutar_organizacion(self, carpeta: str):
        organizer = FileOrganizer(carpeta)

        def callback(nombre_archivo, categoria, actual, total):
            porcentaje = int((actual / total) * 100) if total > 0 else 100
            self.root.after(0, self._actualizar_progreso, nombre_archivo, categoria, actual, total, porcentaje)

        movidos, total, errores = organizer.organizar(callback_progreso=callback)
        self.root.after(0, self._finalizar_organizacion, movidos, total, errores)

    def _actualizar_progreso(self, nombre_archivo, categoria, actual, total, porcentaje):
        self.progreso["value"] = porcentaje
        self.label_estado.config(
            text=t(self.idioma, "moviendo", archivo=nombre_archivo, categoria=categoria, actual=actual, total=total)
        )
        self._agregar_log(f"✔ {nombre_archivo} → {categoria}/")

    def _finalizar_organizacion(self, movidos, total, errores):
        self.organizando = False
        self.btn_organizar.config(state="normal", text=t(self.idioma, "btn_organizar"))
        self.label_estado.config(text=t(self.idioma, "listo", movidos=movidos, total=total))

        if total == 0:
            messagebox.showinfo(t(self.idioma, "info_titulo"), t(self.idioma, "info_sin_archivos"))
        elif errores:
            mensaje = t(self.idioma, "info_con_errores", movidos=movidos, total=total, errores=len(errores))
            messagebox.showwarning(t(self.idioma, "info_titulo"), mensaje)
        else:
            messagebox.showinfo(t(self.idioma, "info_titulo"), t(self.idioma, "info_exito", movidos=movidos))


if __name__ == "__main__":
    root = tk.Tk()
    SelectorIdioma(root)
    root.mainloop()
