print("**********BANK MANGEMENT SYSTEM**********")
bank = []

while True:
    print("""
    1. Add Customer
    2. Display Customers
    3. Update Customer
    4. Remove Customer
    5. Search a Customer
    6. Exit
    """)
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        ac_number = int(input("Enter A/C Number: "))
        name = input("Enter Name: ")
        mobile_no = int(input("Enter Mobile Number: "))
        aadhar = int(input("Enter Aadhar Number: "))
        bank.append([ac_number, name, mobile_no, aadhar])
        print("Customer added successfully!")

    elif choice == 2:
        if bank:
            print('_' * 70)
            print('{:<10}{:<20}{:<15}{:<15}'.format('AC NO', 'NAME', 'MOBILE NO', 'AADHAR NUMBER'))
            print('_' * 70)
            for i in bank:
                print('{:<10}{:<20}{:<15}{:<15}'.format(i[0], i[1], i[2], i[3]))
        else:
            print("No customers to display.")

    elif choice == 3:
        ac_number = int(input("Enter A/C Number of the customer to update: "))
        for i in bank:
            if i[0] == ac_number:
                print("1. Update Name")
                print("2. Update Mobile Number")
                print("3. Update Aadhar Number")
                update_choice = int(input("Enter choices"))
                if update_choice == 1:
                    i[1] = input("Enter new Name: ")
                elif update_choice == 2:
                    i[2] = int(input("Enter new Mobile Number: "))
                elif update_choice == 3:
                    i[3] = int(input("Enter new Aadhar Number: "))
                print("Customer details updated successfully!")
                break
        else:
            print("not found.")

    elif choice == 4:
        ac_number = int(input("Enter A/C Number of the customer to remove: "))
        for i in bank:
            if i[0] == ac_number:
                bank.remove(i)
                print("Customer removed successfully!")
                break
        else:
            print("Customer not found.")

    elif choice == 5:
        ac_number = int(input("Enter A/C Number to search: "))
        for i in bank:
            if i[0] == ac_number:
                print('_' * 70)
                print('{:<10}{:<20}{:<15}{:<15}'.format('AC NO', 'NAME', 'MOBILE NO', 'AADHAR NUMBER'))
                print('_' * 70)
                print('{:<10}{:<20}{:<15}{:<15}'.format(i[0], i[1], i[2],i[3]))
                break
        else:
            print("Customer not found.")

    elif choice == 6:
        print("Existing .........Goodbye!")
        break

    else:
        print("Invalid Choice.")
