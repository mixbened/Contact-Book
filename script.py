import json

print("Welcome to your Contact Book :-)")

# receiving contacts from the contacts.txt
with open("contacts.txt", "r") as contacts_file:
    contacts = json.loads(contacts_file.read())

while True:
    # choose action
    action = input("What do you want to do?: (add / list)")

    # different actions
    if action == "list":
        print("These are your contacts: \n")
        # loops through list and prints name
        for contact in contacts:
            print(contact)
    elif action == "add":
        new_contact = input("Type in new Contact: ")
        # adds name to list
        contacts.append(new_contact)
    # not list or add
    else:
        print("Please type 'add' oder 'list'")
        continue

    # break out of the loop if y
    close = input("Close Program? (y/n)")
    if close == "y":
        print("Thanks, see you.")
        # add list to contacts file
        with open("contacts.txt", "w") as contacts_file:
            contacts_file.write(json.dumps(contacts))
        break