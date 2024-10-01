from login import *
from admin import*
while True:
    print('''
        1.login
        2.exit
''')
    choice=int(input('enter the choice: '))
    if choice==1:
        f=login()
        if f==1:
            while True:
                print('''
                    1.add employee
                    2.update employeee
                    3.delete a employee
                    4.diplay employee
                    5.logout
''')
                admin_choice=int(input('enter your choice: '))
                if admin_choice==1:
                    add_emp()
        elif f==0:
            print('invalid user name or password!!!')