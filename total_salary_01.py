from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("list_of_developers.txt")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)

