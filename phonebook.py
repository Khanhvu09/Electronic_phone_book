entry = {
    "1": "Look up an entry",
    "2": "Set an entry",
    "3": "Delete an entry",
    "4": "List all entries",
    "5": "Search for an entry",
    "6": "Quit"
    }
entry = len(entry)
i = 0
phonebook = dict()
electronic_phonebook = True
while i in range(0, entry):
    i = int(raw_input(
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
    if i == 1:
        name = raw_input("Name: ")
        phonebook[name] = phonebook[name]
        print "Found entry for %s: " % name + phonebook[name] 
        print "\n"
    elif i == 2:
        name = raw_input("Name: ")
        phone_number = raw_input("Phone number: ")
        phonebook[name] = phone_number
        print "Entry stored for %s." % name
        print "\n"
    elif i == 3:
        name = raw_input("Choose name of entry to delete: ")
        del phonebook[name]
        print "Deleted entry for %s" % name
        print "\n"
    elif i == 4:
        key = []
        for key, value in phonebook.iteritems():
            print "Found entry for %s: " % key + value
        print "\n"
    elif i == 5:
        phone_number = raw_input("Enter data to search for: ")
        keys = []
        for key, value in phonebook.iteritems():
            if value == phone_number:
                print "Found: \n" + key + ", %s" % phone_number
                print "\n"
    elif i == 6:
        electronic_phonebook = False
        print "Bye"