"""
config.py
Define las categorías de archivos y qué extensiones pertenecen a cada una.
Si quieres agregar más tipos de archivo, solo edita este diccionario.
"""

CATEGORIAS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".odt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".apk", ".bin"],
    "Others": []  # Carpeta de respaldo para extensiones no reconocidas
}


def obtener_categoria(extension: str) -> str:
    """
    Recibe una extensión (ej: '.png') y devuelve el nombre de la carpeta
    a la que pertenece. Si no la reconoce, devuelve 'Others'.
    """
    extension = extension.lower()
    for categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return categoria
    return "Others"
