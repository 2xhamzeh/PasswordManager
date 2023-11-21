import passwordManager

# test key is ThisIsATest


def listPasswords():
    # print out all the passwords available
    print("\nIndex --- Website --- Username --- Password")
    i = 0
    for l in passwordManager.listOfPasswords:
        print(str(i) + " --- " + l[0] + " --- " + l[1] + " --- " + l[2])
        i += 1
    print()


# get the key
key = input("Enter The Key: ")
# make sure the entered key has no typo
if key != input("Enter The Key again: "):
    print("Keys don't match")
    exit()
# if the key is an empty string use DEFAULT instead
if key == "":
    key = "DEFAULT"
    print("\nDEFAULT key being used!\n")

passwordManager.getPasswords(key)

while True:
    action = input("""What would you like to do?
1. List
2. Add
3. Remove
4. Exit
""")

    action = action.lower().strip()

    if (action == "1" or action == "list"):
        listPasswords()

    elif (action == "2" or action == "add"):
        inWebsite = input("Enter Website Name: ")
        inUsername = input("Enter Username: ")
        inPassword = input("Enter Password: ")
        passwordManager.insertPassword(inWebsite, inUsername, inPassword)
        print("\nPassword Added Successfully\n")

    elif (action == "3" or action == "remove"):
        inPassIndex = input("Enter password index: ")
        if inPassIndex.isdigit():
            inPassIndex = int(inPassIndex)
            if (inPassIndex >= 0 and inPassIndex < len(passwordManager.listOfPasswords)):
                inAreYouSure = input("Are you sure? y/n: ")
                if inAreYouSure.lower().strip() == 'y':
                    passwordManager.deletePassword(inPassIndex)
                    print("\n Password removed.\n")
                else:
                    print("\nOperation cancelled.\n")
            else:
                print("\nIndex doesn't exist\n")
        else:
            print("\nInput invalid!\n")

    elif (action == "4" or action == "exit"):
        passwordManager.saveAndExit(key)
        break
