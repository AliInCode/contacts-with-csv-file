import csv

def read_contacts(file_path):
    with open(file_path, "r") as file:
        contacts = []
        reader = csv.reader(file)
        for row in reader:
            contact = {
                'firstname': row[0],
                'lastname': row[1],
                'phonenumber': row[2],
                'Email': row[3]
            }
            contacts.append(contact)
    return contacts

def show_contact(file_path):
    contacts =[]
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            contact ={
                'first name':row[0] ,
                'last name':row[1] ,
                'phone number':row[2],
                'Email': row[3]
            }
            contacts.append(contact)
    print("-"*50)
    print("My Cantacts :")
    print('{:<20} {:<20}{:<20}{:<20}'.format('first name',"last name",'Phone number',"Email"))
    for dictionary in contacts:
        print('{:<20} {:<20}{:<20}{:<20}'.format(dictionary["first name"], dictionary['last name'], dictionary[ 'phone number'] , dictionary['Email']))
    print("-"*50)

def add_contact(file_path):
    contacts = []
    first_name = input("Enter First name: ").title()
    Last_name = input("Enter Last name: ").title()
    Phone_number = input("Enter phone number : ")
    Email = input("Enter Email: ")
    new_contact = {
        'firstname': first_name,
        'Lastname': Last_name,
        'Phonenumber': Phone_number,
        'Email': Email
    }
    contacts.append(new_contact)
    with open(file_path, mode="a", newline='') as file:
      writer = csv.DictWriter(file,fieldnames=new_contact.values())
      writer.writeheader()
    show_contact(file_path)
    file.close()
def remove_contacts(contacts, phone_number):
    # matching_contacts = [contact for contact in contacts if contact['phonenumber'] == phone_number]
    contacts = [contact for contact in contacts if contact['phonenumber'] != phone_number]
    return contacts

def write_contacts_to_csv(file_path, contacts):
    with open(file_path, mode='w') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact['firstname'], contact['lastname'], contact['phonenumber'], contact['Email']])
        print("{:<20} {:<20} {:<20} {:<20}".format("First Name", "Last Name", "Phone Number", "Email"))
    for dictionary in contacts:
        print("{:<20} {:<20} {:<20} {:<20}".format(dictionary['firstname'], dictionary['lastname'], dictionary['phonenumber'], dictionary['Email']))
    file.close()
def find_contact(contacts ,Search):
    matching_contact = [contact for contact in contacts if contact['phonenumber']==Search  or contact['firstname']==Search]
    return matching_contact