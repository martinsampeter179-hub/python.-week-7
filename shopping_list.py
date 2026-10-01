shopping_list = []

while True:
    action = input("add / remove / show / done: ").strip().lower()

    if action == "add":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"{item} added.")

    elif action == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if shopping_list:
            print("Shopping list:")
            for item in shopping_list:
                print(item)
        else:
            print("Your list is empty.")

    elif action == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose add, remove, show, or done.")
