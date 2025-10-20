# створюємо асистент-бота, який приймає команди від користувача
# і виконує відповідні дії

# Створити функцію main(), яка буде управляти основним ціклом бота
# Ствоити функцую parse_input(), яка буде розбирати введені користувачем дані на команди
# та аргументи

# Cтворити функції обробники для різних команд, такі як hello, add_contact(), 
# change_contact(), show_phone(), show_all(), close()

# програма повинна ідентифікувати та повідомляти про неправильно введені команди.

def parse_input(user_input: str): # робимо парсер (розбір) вводу

    parts = user_input.strip().split()
    if not parts:                 # якщо рядок порожній
        return "", []             # повертаємо "порожню" команду
    cmd, *args = parts
    return cmd.lower(), args

def add_contact(args, contacts: dict) -> str: # додаємо словник контактів
    # очікуємо рівно 2 аргументи: ім'я і телефон
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone     # додаємо/перезаписуємо контакт
    return "Contact added."

def change_contact(args, contacts: dict) -> str: # додаємо зміни до контактів
    # очікуємо рівно 2 аргументи: нове ім'я або новий телефон
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    if name not in contacts:   # якщо немає такого імені
        return "Contact not found."
    contacts[name] = phone     # оновлюємо номер
    return "Contact updated."


def main():
    contacts = {}  # словник для збереження контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: hello, add, change, phone, all, close\n").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]: # вихід з програми
            print("Good bye!")
            break

        elif command in ["hello", "hi", "hey"]: # привітання
            print("How can I help you?")

        elif command == "add": # додати контакт
            # просимо одразу ввести дані контакту
            print("Please, give us your user contact details: name, phone")
            details = input("Enter name and phone separated by koma and space: ").strip()

            # розбиваємо рівно на 2 частини (ім'я, телефон)
            parts = details.split(maxsplit=2)  
            if len(parts) < 2:
                print("Invalid contact details format.")
                continue

            name, phone = parts[0], parts[1]
            if not name or not phone:
                print("Invalid contact details format.")
                continue

            contacts[name] = phone

            print("Contact added.")

        elif command == "change":
              # 1) Якщо аргументи передані одразу в команді — беремо їх
            if len(args) == 2:
                name, new_phone = args
            else:
                # 2) Інакше просимо ввести дані другим input
                print("Please, enter contact to change: name, new_phone")
                details = input("Enter name and new phone separated by koma and space: ").strip()
                parts = details.split(maxsplit=2)
                if len(parts) < 2:
                    print("Invalid format. Use: change username phone")
                    continue
                name, new_phone = parts[0], parts[1]

                # 3) Міняємо номер або повідомляємо, що контакту немає
                if name in contacts:
                    contacts[name] = new_phone
                    print(f"Phone number for {name} changed to {new_phone}.")
                else:
                    print(f"Contact '{name}' not found.")
        
        elif command == "phone": # показати номер телефону
            # 1) Якщо ім’я передане одразу
            if len(args) == 1:
                name = args[0]
            else:
                # 2) Якщо користувач не вказав ім’я — питаємо окремо
                name = input("Enter the contact name: ").strip()

            while name not in contacts: # робимо цикл, поки контакт не знайдемо
                print(f"Contact '{name}' not found.")
                name = input("Please enter an existing contact name: ").strip()
                if name == "":
                    print("Empty input — returning to main menu.")
                    break

            # 3) Перевіряємо, чи контакт існує
            if name in contacts:
                print(f"{name}'s phone number is {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")
        
        elif command == "all": # показати всі контакти
               # Якщо записник порожній
            if not contacts:
                print("Your contact list is empty.")
            else:
                print("Contact list:")
                for name, phone in contacts.items():
                    print(f"• {name}: {phone}")




        elif command == "":
            # порожній ввід – просто питаємо ще раз, без "Invalid command."
            continue
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()





