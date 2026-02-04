FILE="contact.txt"
def load_contacts():
    contacts = {}
    try:
        with open(FILE, 'r') as f:
            for line in f:
                name, phone = line.strip().split(':', 1)
                contacts[name]=phone
    except FileNotFoundError:
        pass
    return contacts
def save_cntacts(contacts):
    with open(FILE,'w') as f:
        for name, phone in contacts.items():
            f.write(f"{name}:{phone}\n")

def add_contacts(contacts):
    name=input("enter the name of the person ")
    number=input("enter the phone number ").strip()
    contacts[name]=number
    print(f"contact {name} added successfully")

def search_contact(contacts):
    name=input("name of the person to search") 
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found in contacts")
def update_contact(contacts):
    name=input("enter the name of the person to update ")
    if name in contacts:
        number=input("enter the new phone number ").strip()
        contacts[name]=number
        print(f"contact {name} successfully updated")
    else:
        print(f"{name} not found in contacts") 
def delete_contact(contacts):
    name=input("ener the name o be deleted")
    if name in contacts:
        del contacts[name]
        print(f"{name} successfully deleted")
    else:
        print(f"{name} not found in contacts")
def display_contacts(contacts):
    if not contacts:
        print("no contacts available")
    else:
        for name, phone in contacts.items(): 
            print(f"{name}: {phone}")
def main():
    contacts=load_contacts()

    while True:
        print("\n cotact book menu")
        print("1. add contacts")   
        print("2. seach contacts")
        print("3. update contacts")
        print("4. delete contacts") 
        print("5. display contacts")
        print("6. exit")
        choice= input("enter your choice").strip()      
        if choice=='1':
            add_contacts(contacts)
        elif choice=='2':
            search_contact(contacts)
        elif choice=='3':
            update_contact(contacts)            
        elif choice=='4':
            delete_contact(contacts)    
        elif choice=='5':
            display_contacts(contacts)  
        elif choice=='6':
            save_cntacts(contacts)
            print("exiting contact book")
            break
        else:
            print("invalid choice please try again")
main() 


