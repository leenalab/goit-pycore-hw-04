# Скрипт для візуалізації структури директорії з кольоровим виведенням
# Вивести папки та файли з різними кольорами:
# - Папки — блакитним кольором
#   - Файли — зеленим кольором

# Використання:
    # python colorama_dir.py <шлях_до_директорії>

# Приклад:
    # python colorama_dir.py "D:\09 Neovercity\Projects"

# активувати віртуальне середовище (.venv)
# встановити бібліотеку colorama:
    # pip install colorama

from pathlib import Path
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

def show_structure(): #функція - отримує шлях, перевіряє його, виводить структуру
    if len(sys.argv) < 2: # перевірка, чи передав користувач шлях   
                          # до діректорії
        print(Fore.YELLOW + "Будь ласка, вкажіть шлях до директорії.")
        return

    folder_path = Path(sys.argv[1]).resolve()

    if not folder_path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує → {folder_path}")
        return
    if not folder_path.is_dir():
        print(Fore.RED + "Помилка: це не директорія → {folder_path}")
        return
    print(Style.BRIGHT + Fore.MAGENTA + f"\nСтруктура директорії: {folder_path}\n")

    def walk_dir(path: Path, indent: int = 0): # оголошуємо внутрішню функцію -рекурсію
                             # intent - змінна для відступів           
        
        for item in path.iterdir():
            if item.is_dir():  
                print(" " * indent + Fore.CYAN + f"[DIR] {item.name}")
                 # Перевірка, чи є об'єкт директорією 

                walk_dir(item, indent + 4)  
            else:
                print(" " * indent + Fore.GREEN + f"{item.name}")
    walk_dir(folder_path)

if __name__ == "__main__":
    show_structure()

# приклад запуску функції 
# python colorama_dir.py "D:\09 Neovercity\Documents"
"""
Agreement-Olena Titiyevska.pdf
[DIR] Biography
    Біографія для Woolf eng.docx
    Біографія для Woolf укр.docx
[DIR] Motivation brief
    Motivation brief eng.docx
    Motivation brief ukr.docx
лист про зарахування.pdf
"""