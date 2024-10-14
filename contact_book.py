# contact_book

from functions import add_contact, view_contacts, search_contact, delete_contact

def contact_book_app():
    contact_book = {}
    while True:
        print("\n1. Add Contact\n2. View All Contacts\n3. Search for Contact\n4. Delete Contact\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    contact_book_app()
