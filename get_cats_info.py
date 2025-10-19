from pathlib import Path

# Створити функцію, яка приймає шлях до файлу з інформацією про котів 
# та повертає список словників з інформацією про кожного кота.
# Використовуємо split(',') для отримання ідентифікатора, імені та віку кота.
# Cтворюємо словник з ключами "id", "name", "age" для кожного кота 
# та додаємо його до списку, який буде повернуто.
# Опрацювати мождивы помилки та винятки

def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue # пропускаємо порожні рядки, (кота не знайдено)

            try:
                cat_id, name, age = line.split(",")  # розділили id, ім’я та вік кота
                cats_list.append({
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                })
            except ValueError:
                print(f"Рядок має неправильний формат, його буде пропущено: {line}")
        return cats_list
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
cats_info = get_cats_info("cats_info.txt")

cats_info = get_cats_info("cats_info.txt")
for cat in cats_info: # виводимо кожний словник з нового рядка
    print(cat)

        


    

        
    