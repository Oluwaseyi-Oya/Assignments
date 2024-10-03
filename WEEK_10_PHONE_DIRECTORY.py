'''
Add new contacts.
Search contacts by name.
Update contact information (like phone number or email).
Delete contacts.

'''

phone_book = {}
#Name, Phonenumbers and emails

def add_contact(name, phone_numbers, emails=None):
    """
    Adds a contact to a contact list with the specified name, phone numbers and optional emails.

    parameter:
    name: str for contact name
    phone_numbers: A list of strings representing the contact's phone numbers.
    emails: An optional list of strings representing the contact's email addresses. If not provided, defaults to None.

    returns:
    none

    """
    phone_book[name] = {}

    contact = phone_book.get(name)

    contact['phone_numbers'] = phone_numbers
    contact['emails'] = emails

    print("Contact saved Successfully")
#     print(f"""
#         Name: {name},
#         Phone Numbers : {'|'.join(phone_numbers)}
#         Emails : {'|'.join(emails)}
# """)

def search(name):
    """"
    searches for contact (name) in the phone_book dict

    parameter:
    name (str): the name to search for

    returns:
    a dict of contact information (name, phone_numbers, emails), if in the phone_book
    none, if name isn't in the phone_book
    """
    contact = phone_book.get(name)
    if contact is None:
        print(f"This person is not available in your contacts")
    else:
        print(name)
        print(contact)


add_contact("Aisha", ["08033124903", "09023467908"], ["aisha@gmail.com","aisha@yahoo.com"])
add_contact("Olamide", ["08033124903", "09023467908"], ["olamide@gmail.com","olamide@yahoo.com"])
search("Aisha")
