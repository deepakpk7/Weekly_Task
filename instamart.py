print("**********INSTAMART MANAGEMENT SYSTEM**********")

employees = []
products = []

while True:
    print("""
          1.Employee Management 
          2.Product Management 
          3.Exist
        
    """)
    
    choice = int(input("Enter Your Choice: "))
    if choice==1:
        usrname=input("Enter your Username :")
        passwd=input("Enter your Password :")
        f=0
        if usrname=='deepak' and passwd=='7034':
            f=1
            while True:
                print("""
                    1.Add Employee
                    2.Display Employee
                    3.Update Employee 
                    4.Search Employee
                    5.Remove Employee
                    6.Logout
                    """)
                sub_choice=int(input("Enter Your Choice: "))

                if sub_choice == 1:
                    emp_id = int(input("Enter Employee ID: "))
                    emp_name = input("Enter Name: ")
                    emp_mob = int(input("Enter Mobile Number: "))
                    emp_position = input("Enter Position: ")
                    emp_salary = float(input("Enter Salary: "))
                    employees.append({'emp_id': emp_id,'name': emp_name,'mob': emp_mob,'position': emp_position,'salary': emp_salary})
                    print("Employee added successfully!")
                elif sub_choice==2:
                    if not employees:
                        print("No employees to display.")
                    else:
                        print('_' * 70)
                        print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format('Emp_ID', 'Name', 'Mobile', 'Position', 'Salary'))
                        print('*' * 70)
                        for i in employees:
                            print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format(i['emp_id'], i['name'], i['mob'], i['position'], i['salary']))
                elif sub_choice==3:
                    emp_id = int(input("Enter Employee ID to Update: "))
                    for i in employees:
                            if i['emp_id'] == emp_id:
                                print("Current Details: ", i)
                                i['name'] = input("Enter New Name: ") 
                                i['mob'] = int(input("Enter New Mobile Number: "))
                                i['position'] = input("Enter New Position: ")
                                i['salary'] = float(input("Enter New Salary: "))
                                print("Employee details updated successfully!")
                                break
                            else:
                                print("Employee not found!")
                elif sub_choice==4:
                    id =int(input("Enter the employee ID Search: "))
                    for i in employees:
                        if i['emp_id'] == id:
                            print('_' * 70)
                            print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format('Emp_ID', 'Name', 'Mobile', 'Position', 'Salary'))
                            print('*' * 70)
                            for i in employees:
                                print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format(i['emp_id'], i['name'], i['mob'], i['position'], i['salary']))
                                break
                        else:
                            print("***Product not found***")
                elif sub_choice==5:
                    id =int(input("Enter the employee ID to remove : "))
                    for i in employees:
                        if i['emp_id'] == id:
                            employees.remove(i)
                            print("Employee removed successfully.")
                            break
                        else:
                            print("Employee not in the Database")
                elif sub_choice==6:
                    print("Logouting......")
                    break
                else :
                    print("Enter valid choices.....")
        else:
            print("*****Invalid username & password*****")
            
    # PRODUCT SECTION
    elif choice==2:
        print("________PRODUCT MANGEMENT______")
        while True:
            print("""
            1. Add product 
            2. Display product Details
            3. Update product
            4. Delete product
            5. Search a product
            6. Exit
            """)
            choice = int(input("Enter Your Choice: "))
            
            if choice == 1:
                name = input("Enter a product name: ")
                bar_code = int(input("Enter bar_code: "))
                price = int(input("Enter price: "))
                products.append({'name': name, 'bar_code': bar_code, 'price': price})
                print(products)
            elif choice == 2:
                print('_' * 30)
                print('{:<10}{:<10}{:<10}'.format('Product', 'bar_code', 'price'))
                print('*' * 30)
                for i in products:
                    print('{:<10}{:<10}{:<10}'.format(i['name'], i['bar_code'], i['price']))
            elif choice == 3:
                name = input("Enter the product name to update: ")
                for i in products:
                    if i['name'] == name:
                        bar_code = int(input("Enter a new bar_code: "))
                        price = int(input("Enter a new price: "))
                        i['bar_code'] = bar_code
                        i['price'] = price
                        print("Product updated successfully.")
                        break
                else:
                    print("Product not found")
            elif choice == 4:
                name = input("Enter the product name to Delete: ")
                for i in products:
                    if i['name'] == name:
                        products.remove(i)
                        print("Product removed successfully.")
                        break
                else:
                    print("Product not in the Database")
            
            elif choice == 5:
                name = input("Enter the product name to Search: ")
                for i in products:
                    if i['name'] == name:
                        print('_' * 30)
                        print('{:<10}{:<10}{:<10}'.format('Name', 'bar_code', 'price'))
                        print('*' * 30)
                        print('{:<10}{:<10}{:<10}'.format(i['name'], i['bar_code'], i['price']))
                        break
                    else:
                        print("***Product not found***")
            elif choice == 6:
                print("Existing .......")
                break
            else:
                print("Invalid Choice")
    
    elif choice==3:
        print(".....................")
        break
    else :
        print("Invalid Choices  ")
        print("Enter a valid choices.....")