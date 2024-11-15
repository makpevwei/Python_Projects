contacts_dict = {}

def insert_contact():
    
    contact_name = input("Enter Contact Name: ").strip().title()
    
    while True:
        contact_number = input("Enter Contact Number: ")
        
        if contact_number.isdigit() and len(contact_number) == 11:
            contacts_dict[contact_name] = contact_number
            print("Contact saved!")
            print(contacts_dict)
            break
        else:
            print("Invalid Number. Please, enter a 11 digit number!")
            

def read_contacts():
    
    for name, number in contacts_dict.items():
        print(f"{name}: {number}")
    
        
def update_contact():
    
    contact_name = input("Enter name of contact to update: ").strip().title()
    
    if contact_name in contacts_dict:
        while True:
            new_contact_number = input("Edit Contact Number: ")
            if new_contact_number.isdigit() and len(new_contact_number) == 11:
                contacts_dict[contact_name] = new_contact_number
                print("Contact Updated!")
                print(contacts_dict)
                break
            else:
                print("Invalid Number. Please, enter a 11 digit number!")
    else:
        print("Contact not found!")
        insert_contact()
        
def delete_contact():
    
    contact_name = input("Enter name of contact to delete: ").strip().title()
    
    if contact_name in contacts_dict:
        del contacts_dict[contact_name]
        print(f"Contact {contact_name} deleted successfully!")
    else:
        print("Contact not found!")
        insert_contact()          
                    
def main():   
    print("Contact Book App")
    print("-" * 20)
    print("Enter 1 to insert a contact")
    print("Enter 2 to show  contacts")
    print("Enter 3 to update a contact")
    print("Enter 4 to delete a contact")
    print("Enter 5 to exit")
    print()     
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                insert_contact()
            elif choice == 2:
                read_contacts()
            elif choice == 3:
                update_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please, enter a number between 1 and 5.")
        except Exception as error:
            print("Invalid Input. Please, enter a numeric value.")
    
main()
    