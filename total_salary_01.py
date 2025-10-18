from pathlib import Path

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        total = 0 # змінна для підсумкової суми зарплат.
        persons = 0 # змінна для підрахунку кількості працівників

        for line in lines:
            line = line.strip()
            if not line:
                continue # пропускаємо порожні рядки
               
            try:
                name, salary = line.split(",")
                total += float(salary)
                persons += 1
            except ValueError:
                print(f"Рядок має неправильний формат та буде пропущений: {line}")
    
        if persons == 0:
            return (0, 0)
    
        average = total / persons
        return (total, average)

    except FileNotFoundError: # Ловимо помилку, якщо файл не знайдено.
    
        print("Файл не знайдено.")
        return (0, 0)
    
total, average = total_salary("list_of_developers.txt")

print(f"Загальна сума заробітної плати: {round(total)}")
print(f"Середня заробітна плата: {round(average)}") # округлюємо середню зарплату до цілого числа.