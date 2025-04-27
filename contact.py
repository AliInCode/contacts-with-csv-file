import pyfiglet
from functions import read_contacts
from functions import show_contact
from functions import add_contact
from functions import remove_contacts
from functions import find_contact
from functions import write_contacts_to_csv

file_path = "E:\project\python\contactscsv\contact.CSV"
contacts = read_contacts(file_path)
# print(pyfiglet.figlet_format("My Cantacts"))
print(f"Your file path is {file_path}")
while True:
    print("1) show Contact")
    print("2) Add Contact")
    print("3) Delete Contact")
    print("4) Search Contact")
    print("5) exit app")
    print("-"*50)
    choice = int(input("Enter your chioce :"))
    if choice == 1:
        show_contact(file_path)
    elif choice == 2:
        add_contact(file_path)
    elif choice == 3:
        phone_number = input('please Enter your phone number :')
        contacts= remove_contacts(contacts, phone_number)
        write_contacts_to_csv(file_path, contacts)
        show_contact(file_path)
    elif choice == 4:
        Search = input("please Enter your search :").title()
        find_contact(contacts ,Search)
        matching_contacts = find_contact(contacts,Search)
        print("Search result :")
        print('{:<20} {:<20}{:<20}{:<20}'.format('first name',"Last name",'Phone Number',"Email"))
        for dictionary in matching_contacts :
            print('{:<20} {:<20}{:<20}{:<20}'.format(dictionary["firstname"], dictionary['lastname'], dictionary[ 'phonenumber'] , dictionary['Email']))
    elif choice == 5 :
        break