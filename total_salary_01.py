with open("list_of_developers.txt", "a") as f:
    f.write("Serj Griznov,2500\n")

with open("list_of_developers.txt", "r") as f:
    print(f.read())