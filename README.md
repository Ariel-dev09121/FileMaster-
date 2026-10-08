# FileMaster 📂

A desktop app that automatically organizes the files of a folder
into categories (Images, Videos, Music, Documents, Archives,
Executables, Others).

> Built with AI assistance as an early learning project.
> I'm currently studying the code and improving it.

## Features

- Simple graphical interface (Tkinter)
- 6 languages: Spanish, English, French, Portuguese, German, Italian
- Never overwrites files: duplicates become `name (1).ext`
- Progress bar and live activity log
- Daily log files saved in a `logs/` folder

## Requirements

- Python 3.8+
- Tkinter (included with the standard Python installer on Windows)

## How to run

1. Download all the `.py` files into the same folder
2. Run: `python main.py`
3. Choose your language, select a folder and click **Organize**

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Graphical interface |
| `organizer.py` | Logic to scan, classify and move files |
| `config.py` | File categories and their extensions |
| `idiomas.py` | Interface texts for every language |

## Known limitations

- Moves files immediately, with no undo option
- Only organizes files directly inside the selected folder
- Designed for desktop (tested on Windows)

## Roadmap

- [ ] Confirmation dialog before moving files
- [ ] Undo button
- [ ] Translate code comments to English
