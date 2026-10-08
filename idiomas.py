"""
idiomas.py
Contiene todos los textos de la interfaz en cada idioma soportado.
Para agregar un idioma nuevo: copia un bloque completo (ej. "en") y tradúcelo.
"""

TEXTOS = {
    "es": {
        "titulo_app": "🥇 File Master",
        "titulo_ventana": "📂 File Master",
        "subtitulo": "Organiza automáticamente los archivos de una carpeta",
        "btn_seleccionar": "📁 Seleccionar carpeta",
        "carpeta_default": "Ninguna carpeta seleccionada",
        "btn_organizar": "🚚 Organizar",
        "btn_organizando": "Organizando...",
        "moviendo": "Moviendo: {archivo} → {categoria}/  ({actual}/{total})",
        "listo": "✅ Listo: {movidos}/{total} archivos organizados.",
        "alerta_titulo": "Atención",
        "alerta_sin_carpeta": "Primero selecciona una carpeta.",
        "info_titulo": "File Master",
        "info_sin_archivos": "No se encontraron archivos para organizar en esa carpeta.",
        "info_con_errores": "Se organizaron {movidos}/{total} archivos.\n\nHubo {errores} error(es). Revisa el log.",
        "info_exito": "¡Listo! Se organizaron {movidos} archivos correctamente. 🎉",
        "selector_titulo": "Selecciona tu idioma / Select your language",
        "selector_pregunta": "¿En qué idioma quieres usar File Master?",
        "selector_continuar": "Continuar",
        "dialogo_seleccionar_carpeta": "Selecciona la carpeta a organizar",
    },
    "en": {
        "titulo_app": "🥇 File Master",
        "titulo_ventana": "📂 File Master",
        "subtitulo": "Automatically organizes the files in a folder",
        "btn_seleccionar": "📁 Select folder",
        "carpeta_default": "No folder selected",
        "btn_organizar": "🚚 Organize",
        "btn_organizando": "Organizing...",
        "moviendo": "Moving: {archivo} → {categoria}/  ({actual}/{total})",
        "listo": "✅ Done: {movidos}/{total} files organized.",
        "alerta_titulo": "Warning",
        "alerta_sin_carpeta": "Please select a folder first.",
        "info_titulo": "File Master",
        "info_sin_archivos": "No files were found to organize in that folder.",
        "info_con_errores": "{movidos}/{total} files were organized.\n\nThere were {errores} error(s). Check the log.",
        "info_exito": "Done! {movidos} files were organized successfully. 🎉",
        "selector_titulo": "Selecciona tu idioma / Select your language",
        "selector_pregunta": "Which language do you want to use File Master in?",
        "selector_continuar": "Continue",
        "dialogo_seleccionar_carpeta": "Select the folder to organize",
    },
    "fr": {
        "titulo_app": "🥇 File Master",
        "titulo_ventana": "📂 File Master",
        "subtitulo": "Organise automatiquement les fichiers d'un dossier",
        "btn_seleccionar": "📁 Choisir un dossier",
        "carpeta_default": "Aucun dossier sélectionné",
        "btn_organizar": "🚚 Organiser",
        "btn_organizando": "Organisation...",
        "moviendo": "Déplacement : {archivo} → {categoria}/  ({actual}/{total})",
        "listo": "✅ Terminé : {movidos}/{total} fichiers organisés.",
        "alerta_titulo": "Attention",
        "alerta_sin_carpeta": "Veuillez d'abord sélectionner un dossier.",
        "info_titulo": "File Master",
        "info_sin_archivos": "Aucun fichier trouvé à organiser dans ce dossier.",
        "info_con_errores": "{movidos}/{total} fichiers organisés.\n\n{errores} erreur(s). Consultez le journal.",
        "info_exito": "Terminé ! {movidos} fichiers organisés avec succès. 🎉",
        "selector_titulo": "Sélectionnez votre langue",
        "selector_pregunta": "Dans quelle langue voulez-vous utiliser File Master ?",
        "selector_continuar": "Continuer",
        "dialogo_seleccionar_carpeta": "Sélectionnez le dossier à organiser",
    },
    "pt": {
        "titulo_app": "🥇 File Master",
        "titulo_ventana": "📂 File Master",
        "subtitulo": "Organiza automaticamente os arquivos de uma pasta",
        "btn_seleccionar": "📁 Selecionar pasta",
        "carpeta_default": "Nenhuma pasta selecionada",
        "btn_organizar": "🚚 Organizar",
        "btn_organizando": "Organizando...",
        "moviendo": "Movendo: {archivo} → {categoria}/  ({actual}/{total})",
        "listo": "✅ Concluído: {movidos}/{total} arquivos organizados.",
        "alerta_titulo": "Atenção",
        "alerta_sin_carpeta": "Primeiro selecione uma pasta.",
        "info_titulo": "File Master",
        "info_sin_archivos": "Nenhum arquivo encontrado para organizar nessa pasta.",
        "info_con_errores": "{movidos}/{total} arquivos foram organizados.\n\nHouve {errores} erro(s). Veja o log.",
        "info_exito": "Pronto! {movidos} arquivos organizados com sucesso. 🎉",
        "selector_titulo": "Selecione seu idioma",
        "selector_pregunta": "Em qual idioma você quer usar o File Master?",
        "selector_continuar": "Continuar",
        "dialogo_seleccionar_carpeta": "Selecione a pasta a organizar",
    },
    "de": {
        "titulo_app": "🥇 File Master",
        "titulo_ventana": "📂 File Master",
        "subtitulo": "Organisiert automatisch die Dateien eines Ordners",
        "btn_seleccionar": "📁 Ordner auswählen",
        "carpeta_default": "Kein Ordner ausgewählt",
        "btn_organizar": "🚚 Organisieren",
        "btn_organizando": "Wird organisiert...",
        "moviendo": "Verschiebe: {archivo} → {categoria}/  ({actual}/{total})",
        "listo": "✅ Fertig: {movidos}/{total} Dateien organisiert.",
        "alerta_titulo": "Achtung",
        "alerta_sin_carpeta": "Bitte zuerst einen Ordner auswählen.",
        "info_titulo": "File Master",
        "info_sin_archivos": "In diesem Ordner wurden keine Dateien zum Organisieren gefunden.",
        "info_con_errores": "{movidos}/{total} Dateien wurden organisiert.\n\nEs gab {errores} Fehler. Siehe Log.",
        "info_exito": "Fertig! {movidos} Dateien erfolgreich organisiert. 🎉",
        "selector_titulo": "Wählen Sie Ihre Sprache",
        "selector_pregunta": "In welcher Sprache möchten Sie File Master verwenden?",
        "selector_continuar": "Weiter",
        "dialogo_seleccionar_carpeta": "Wählen Sie den zu organisierenden Ordner",
    },
    "it": {
        "titulo_app": "🥇 File Master",
        "titulo_ventana": "📂 File Master",
        "subtitulo": "Organizza automaticamente i file di una cartella",
        "btn_seleccionar": "📁 Seleziona cartella",
        "carpeta_default": "Nessuna cartella selezionata",
        "btn_organizar": "🚚 Organizza",
        "btn_organizando": "Organizzazione...",
        "moviendo": "Spostamento: {archivo} → {categoria}/  ({actual}/{total})",
        "listo": "✅ Fatto: {movidos}/{total} file organizzati.",
        "alerta_titulo": "Attenzione",
        "alerta_sin_carpeta": "Seleziona prima una cartella.",
        "info_titulo": "File Master",
        "info_sin_archivos": "Nessun file trovato da organizzare in quella cartella.",
        "info_con_errores": "{movidos}/{total} file sono stati organizzati.\n\nCi sono stati {errores} errore(i). Controlla il log.",
        "info_exito": "Fatto! {movidos} file organizzati con successo. 🎉",
        "selector_titulo": "Seleziona la tua lingua",
        "selector_pregunta": "In quale lingua vuoi usare File Master?",
        "selector_continuar": "Continua",
        "dialogo_seleccionar_carpeta": "Seleziona la cartella da organizzare",
    },
}

# Lista de idiomas disponibles para mostrar en el selector.
# Para agregar un nuevo idioma: 1) agrega su bloque arriba en TEXTOS,
# 2) agrega una línea aquí con su código, bandera y nombre.
IDIOMAS_DISPONIBLES = [
    {"codigo": "es", "bandera": "🇲🇽", "nombre": "Español"},
    {"codigo": "en", "bandera": "🇺🇸", "nombre": "English"},
    {"codigo": "fr", "bandera": "🇫🇷", "nombre": "Français"},
    {"codigo": "pt", "bandera": "🇧🇷", "nombre": "Português"},
    {"codigo": "de", "bandera": "🇩🇪", "nombre": "Deutsch"},
    {"codigo": "it", "bandera": "🇮🇹", "nombre": "Italiano"},
]


def t(idioma: str, clave: str, **kwargs) -> str:
    """
    Devuelve el texto traducido para la clave dada en el idioma dado.
    Permite usar variables con .format(), ej: t("es", "listo", movidos=5, total=5)
    Si el idioma no existe, usa español por defecto.
    """
    diccionario = TEXTOS.get(idioma, TEXTOS["es"])
    texto = diccionario.get(clave, clave)
    if kwargs:
        return texto.format(**kwargs)
    return texto
