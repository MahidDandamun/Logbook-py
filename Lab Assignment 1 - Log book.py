from tabulate import tabulate

Fname = ['0']*50
Lname = ['0']*50
Address = ['0']*50
Contact = ['0']*50

def menu():

    print("""
X------------------------Address Book-----------------------X
|  What Would Like to do?                                   |  
|  1. Add a Contact                                         |
|  2. Edit a Contact                                        |  
|  3. Delete Contact                                        | 
|  4. View Contacts                                         |
|  5. Search Address Book                                   |
|  6. Exit                                                  |
X-----------------------------------------------------------X""")

def Mainmenu():

    count = 0
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == '1':
            if count != len(Fname):
                if Addcontacts(count):
                    count += 1
            else:
                print("The logbook is already full!")
            print("The current Address Book log: ", count)

        elif choice == '2':
            if count != 0:
                Editcontacts(count)
            else:
                print("There's nothing on the list that you can edit")

        elif choice == '3':
            if count > 0:
                if Deletecontacts(count) == True:
                    count -= 1
                    print("The current log is: ", count, "People")
            else:
                print("There's nothing on the list to delete")

        elif choice == '4':
            viewContentList(count)
        elif choice == '5':
            if count > 0:
                SearchContacts()
            else:
                print("There's nothing on the list to search")
        elif choice == '6':
            print("Good bye and Have a nice day!")
            exit()
        else:
            print("Invalid selection of Choice")

def Addcontacts(count):
    if count< len(Fname):
        x, y, z, j = input("Enter FirstName:"), input("Enter LastName:"), input("Enter Address:"), input("Enter Contact: ")
        if (x and y and z and j) != '':
            Fname[count] = x
            Lname[count] = y
            Address[count] = z
            Contact[count] = j
        else:
            print("You Entered Nothing or you left some fields unfilled")
            return
        return True
    else:
        print("The log is already full")

def EditValidation(list,count):
        try:
            i = int(input("Enter the index of element: Or you can Enter nothing to Exit "))
            if (i != '') and (i >= 0 and i < count):
                y = input("Enter the Element:")
                if y != '':
                    list[i] = y
                    print("The list is now Updated")
            else:
                print("The index that you've entered contains nothing or it is outside of list range")
        except ValueError:
            print("You have inputted nothing to exit or a wrong value")
            return

def Editcontacts(count):
    NewFname = [n for n in Fname if n != '0']
    NewLname = [x for x in Lname if x != '0']
    NewAddress = [y for y in Address if y != '0']
    NewContact = [t for t in Contact if t != '0']
    try:
        while True:
            Choices(count)
            choice = input("""                            
    Kindly Enter the number of your choice of which of following sections you want to edit:""")
            if choice == '1':
                print(tabulate({"First Names": NewFname}, headers="keys", showindex=True, tablefmt="rounded_outline"))
                EditValidation(Fname, count)
            elif choice == '2':
                print(tabulate({"Last Names": NewLname}, headers="keys", showindex=True, tablefmt="rounded_outline"))
                EditValidation(Lname, count)
            elif choice == '3':
                print(tabulate({"Addresses": NewAddress}, headers="keys", showindex=True, tablefmt="rounded_outline"))
                EditValidation(Address, count)
            elif choice == '4':
                print(tabulate({"Contacts": NewContact}, headers="keys", showindex=True, tablefmt="rounded_outline"))
                EditValidation(Contact, count)
            elif choice == '5':
                print("You chose (5) to exit ")
                return
            elif choice == '':
                print("You entered nothing")
                return
            else:
                print("Invalid input of Choice")
    except ValueError:
        print("You have inputted nothing to exit or a wrong value")
        return

def Deletecontacts(count):

    viewContentList(count)
    try:
        x = int(input("Kindly enter the index that you want to delete:"))
        if (x != "") and (x <= count-1 and x>=0):
            Fname.pop(x), Lname.pop(x), Address.pop(x), Contact.pop(x)
            Fname.append('0'), Lname.append('0')
            Address.append('0'), Contact.append('0')
            print("The list is now updated")
            return True
        else:
            print("You inputted wrong index")
            return
    except ValueError:
        print("Sorry you have inputted a wrong value")
        return

def Choices(count):
    viewContentList(count)
    print("X------------------Choose which of these you want to Edit or Delete ------------------------X")
    print("(1) =", "First Names")
    print("(2) =", "Last Names")
    print("(3) =", "Addresses")
    print("(4) =", "Contacts")
    print("(5) or " + "''=" + " (Press 5 or Enter to Exit)")


def SearchContacts():

    while True:
        print("Search Contact on the Address Book by the following means: ")
        print("""
        1.By First Name
        2.By Last Name
        3.By Address
        4.By Contact number
        5.Exit( or press enter twice)
        """)
        x = input("Input Your choice: ")
        try:
            if x == '1':
                i = input("Enter the Firstname of you want to search: ")
                SearchMatch(Fname, i)
            elif x == '2':
                i = input("Enter the Lastname that you want to search: ")
                SearchMatch(Lname, i)
            elif x == '3':
                i = input("Enter Address that you want to search: ")
                SearchMatch(Address, i)
            elif x == '4':
                i = input("Enter the Contact that you want to search: ")
                SearchMatch(Contact, i)
            elif x == '5' or x == "":
                print("Returning to main menu")
                return
        except ValueError:
            print("Sorry you have inputted invalid choice, this thread will now exit")
            return


def SearchMatch(list, i):

    if i in list:
        y = [j for j, x in enumerate(list) if x == i]
        Fname2, Lname2, Address2, Contact2 = [], [], [], []
        for e in y:
            Fname2.append(Fname[e])
            Lname2.append(Lname[e])
            Address2.append(Address[e])
            Contact2.append(Contact[e])
        print("The element ", i, " appeared ", list.count(i), " times in the Address book")
        print(tabulate({"First Names": Fname2, "Last Names": Lname2,
                        "Addresses": Address2, "Contacts":Contact2}, headers="keys", showindex=True, tablefmt= "rounded_outline"))
    else:
        print("The", i, " Does not exist in the AddressBook")

def viewContentList(count):
    NewFname = [n for n in Fname if n != '0']
    NewLname = [n for n in Lname if n != '0']
    NewAddress = [n for n in Address if n != '0']
    NewContacts = [n for n in Contact if n != '0']
    print(tabulate({"FirstNames": NewFname, "LastNames": NewLname, "Addresses": NewAddress, "Contacts": NewContacts}, headers="keys", showindex=True, tablefmt="rounded_outline"))

    print("The current log is: ", count)

Mainmenu()

