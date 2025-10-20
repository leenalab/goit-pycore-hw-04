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


def main():
    print("Welcome to the assistant bot!")
    while True:
        raw = input("Enter a command: ")
        command = raw.strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hello", "hi", "hey"]:
            print("How can I help you?")

        elif command == "":
            # порожній ввід – просто питаємо ще раз, без "Invalid command."
            continue
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()





