from auth import login
from employee import *

while True:
    print("""
          1. Login
          2. Exit
          """)
    choices = int(input("Enter your choice: "))
    
    if choices == 1:
        f, user = login()
        print(f)
        print(user)
        # Admin login
        if f == 1:
            while True:
                print("""
                      1. Add Employee
                      2. Update Employee
                      3. Delete Employee 
                      4. Display Employee Details
                      5. Logout
                      """)

                sub_choices = int(input("Enter your choice: "))
                
                if sub_choices == 1:
                    add_emp()
                elif sub_choices == 2:
                    emp_update()
                elif sub_choices == 3:
                    delete_emp()
                elif sub_choices == 4:
                    display_emp()
                elif sub_choices == 5:
                    print("Logging out......")
                    break

        elif f == 0:
            print("# Invalid Username and Password #")
        # User login page
        elif f==2:
            while True:
                if user['dob'] == user['password']:
                    print("Create a New Password")
                    passwd = input("Enter new Password: ")
                    user['password'] = passwd
                    print("Password changed successfully......")
                else:
                    print("""
                        1. View Profile
                        2. Edit Profile
                        3. Logout
                        """)
                    sub_choices_u = int(input("Enter your choice: "))
                    
                    if sub_choices_u == 1:
                        view_profile(user)
                    elif sub_choices_u == 2:
                        edit_profile(user)
                    elif sub_choices_u == 3:
                        print("Logging out........")
                        break
    elif choices == 2:
        print("Exiting....")
        break
    else:
        print("Invalid choice.......")
