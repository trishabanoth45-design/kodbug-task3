
# .......... Contact Book..........

contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add a new contact

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    # View all contacts

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- All Contacts ---")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("--------------------")

    # Search for a contact by name

    elif choice == "3":
        search_name = input("Enter name to search: ").strip().lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name:
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete a contact

    elif choice == "4":
        delete_name = input("Enter name to delete: ").strip().lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit the program
    
    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
