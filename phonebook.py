user_input = 0
phonebook = dict()
electronic_phonebook = True
while user_input in range(0, 7):
    user_input = int(raw_input(
    "Electronic Phone Book\n"
    "=====================\n"
    "1. Look up an entry\n"
    "2. Set an entry\n"
    "3. Delete an entry\n"
    "4. List all entries\n"
    "5. Search for an entry\n"
    "6. Quit\n"
    "What do you want to do? "
    ))
    if user_input == 1:
        name = raw_input("Name: ")
        phonebook[name] = phonebook[name]
        print "Found entry for %s: " % name + phonebook[name] 
        print "\n"
    elif user_input == 2:
        name = raw_input("Name: ")
        phone_number = raw_input("Phone number: ")
        phonebook[name] = phone_number
        print "Entry stored for %s." % name
        print "\n"
    elif user_input == 3:
        name = raw_input("Choose name of entry to delete: ")
        del phonebook[name]
        print "Deleted entry for %s" % name
        print "\n"
    elif user_input == 4:
        key = []
        for key, value in phonebook.iteritems():
            print "Found entry for %s: " % key + value
        print "\n"
    elif user_input == 5:
        phone_number = raw_input("Enter phone number to search for: ")
        keys = []
        for key, value in phonebook.iteritems():
            if value == phone_number:
                print "Found: \n" + key + ", %s" % phone_number
                print "\n"
    elif user_input == 6:
        electronic_phonebook = False
        print "Bye"
    