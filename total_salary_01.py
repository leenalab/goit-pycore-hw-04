with open ("list_of_developers.txt.", "a+") as f:
    f.write("Serj Griznov,2500\n")
    f.seek(0)  # щоб прочитати спочатку
    print(f.read())