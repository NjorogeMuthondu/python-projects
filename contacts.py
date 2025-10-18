import json
import os

# File path for storing contacts
file_path = "C:\\data\\book.txt"

# Load existing contacts if the file exists
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        try:
            phone_book = json.load(f)
        except json.JSONDecodeError:
            phone_book = {}
else:
    phone_book = {}

# Main loop
command = ""
while command != 'exit':
    command = input('\nEnter a command (options: new, get, save, exit): ').strip().lower()

    if command == "new":
        name = input('Enter name of the person: ').strip()
        p = input('Phone number: ').strip()
        a = input('Address: ').strip()
        phone_book[name] = {'phone': p, 'address': a}
        print(f"Contact for {name} added.")

    elif command == 'get':
        name = input('Enter name of the person: ').strip()
        if name in phone_book:
            print(f"\nName: {name}")
            print(f"Phone: {phone_book[name]['phone']}")
            print(f"Address: {phone_book[name]['address']}")
        else:
            print('Person not found in address book.')

    elif command == 'save':
        try:
            with open(file_path, "w") as f:
                json.dump(phone_book, f, indent=4)
            print("Contacts saved successfully.")
        except Exception as e:
            print(f"Error saving contacts: {e}")

    elif command != 'exit':
        print("Unknown command. Please try again.")

print("Goodbye!")



