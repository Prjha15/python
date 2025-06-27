print("HEY!WELCOME BACK")
print("What's on your mind?")
print("1. Write about your day.")
print("2. Read your previous writings.")
print("3. EXIT")

choice = int(input("Enter your choice:\n"))

while True:
    if choice == 1:
        title = str(input("Enter a title or date for your entry: "))
        content = str(input("Enter your diary entry: "))
        with open("diary.txt", "a") as file:
            file.write(title + "\n")
            file.write(content + "\n")
            file.write("-" * 30 + "\n")
        break

    elif choice == 2:
        with open("diary.txt", "r") as file:
            print(file.read())
        break

    elif choice == 3:
        print("See you soon!")
        break

    else:
        print("Invalid choice.")
        break
