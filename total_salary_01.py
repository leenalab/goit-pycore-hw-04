# Спочатку додаємо новий рядок
with open("list_of_developers.txt", "a") as f:
    f.write("\nSerj Griznov,2500\n")

# Потім читаємо увесь файл
with open("list_of_developers.txt", "r") as f:
    print(f.read())