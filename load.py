
import os


def save_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(name + "," + phone + "\n")
    print("Contact saved successfully!")


def view_contacts():
    if not os.path.exists("contacts.txt"):
        print("No contacts saved yet.")
        return

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    for contact in contacts:
        name, phone = contact.strip().split(",", 1)
        print("Name:", name, "| Phone:", phone)


def main():
    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()

            if name and phone and "," not in name + phone:
                save_contact(name, phone)
            else:
                print("Enter valid details without commas.")

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
