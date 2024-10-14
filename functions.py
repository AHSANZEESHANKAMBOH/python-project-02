
def add_contact(contact_book):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name and phone.isdigit():
        contact_book[name] = phone
    else:
        print("Invalid input. Name can't be empty and phone number must contain digits only.")

def view_contacts(contact_book):
    if contact_book:
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

def search_contact(contact_book):
    name = input("Enter name to search: ").strip()
    if name in contact_book:
        print(f"Phone number: {contact_book[name]}")
    else:
        print("Contact not found.")

def delete_contact(contact_book):
    name = input("Enter name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"{name} has been deleted.")
    else:
        print("Contact not found.")
