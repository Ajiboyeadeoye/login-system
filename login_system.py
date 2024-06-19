from stdiomask import getpass
import hashlib
import os

clear = lambda: os.system('cls')


def main():
    clear()
    print('MAIN MENU')
    print('**********')
    print()
    print('1 - Register')
    print('2 - Login')
    print()
    while True:
        print()
        userChoice = input('Choose An Option: ')
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Register()
    else:
        Login()

def Register():
    clear()
    print('REGISTER')
    print('----------')
    print()
    while True:
        userName = input('Enter Your Name: ').title()
        if userName != '':
            break
    userName = sanitizeName(userName)
    while True:
        userPassword = input("Enter Your Password: ")
        if userPassword != '':
            break
    while True:
        confirmPassword = input('Confirm Your Password: ')
        if confirmPassword == userPassword:
            break
        else:
            print("Password Don't Match")
            print()
    if userAlreadyExist(userName, userPassword):
        while True:
            print()
            error = input("You Are Already Registered.\n\n Press (T) To Try Again:\nPress (L) To Login: ").lower()
            if error == 't':
                Register()
                break
            elif error == 'l':
                Login()
                break
        

    addUserInfo([userName, hash_password(userPassword)])

    print()
    print("Registered!")

def Login():
    clear()
    print("LOGIN")
    print("------")
    print()
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            usersInfo.update({line[0]: line[0]})

    while True:
        userName = input("Enter Your Name: ").title()
        userName = '-'.join(userName.split())
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("You Are Not Registered")
            print()
        else:
            break
    print()
    print('Logged in!')

def addUserInfo(userInfo: list):
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            if info is not None and isinstance(info, str):
                file.write(info)
                file.write(' ')
        file.write('\n')

def userAlreadyExist(userName, userPassword):
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            if line[0] == userName and line[1] == hash_password(userPassword):
                usersinfo.update({line[0]: line[1]})
    if usersInfo == {}:
        return False
        

def sanitizeName(userName):
    pass

def hash_password(userPassword):
    return hashlib.sha256(str.encode(userPassword)).hexdigest()

def check_password_hash(userPassword, hash):
    return hash_password(userPassword) == hash


main()
