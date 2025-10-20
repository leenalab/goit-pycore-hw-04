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