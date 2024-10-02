emp = []

def login():
    usrname = input("Enter your Username :")
    passwd = input("Enter your Password :")
    f = 0
    user = ''
    if usrname == 'deepak' and passwd == '7034':
        f = 1
        print("Login successfully.......")
    for i in emp:
        if i['id'] == usrname and i['password'] == passwd:
            f = 2
            user = i
    return f, user
