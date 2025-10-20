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
        print("Будь ласка, вкажіть шлях до директорії.")
        return

    folder_path = Path(sys.argv[1])

    if not folder_path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує!")
        return
    if not folder_path.is_dir():
        print(Fore.RED + "Помилка: це не директорія!")
        return
    print(Style.BRIGHT + Fore.MAGENTA + f"\nСтруктура директорії: {folder_path}\n")
