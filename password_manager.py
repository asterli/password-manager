from cryptography.fernet import Fernet
import os

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    if os.stat('passwords.txt').st_size == 0:
        print("No passwords to view!")
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            label, user, pwd = data.split("|")
            print("Credentials for:", label, "| Username:", user, "| Password:", fer.decrypt(pwd.encode()).decode())

def add():
    label = input("What website/org/company/etc is this password for?: ")
    user = input("Username: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(label + "|" + user + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    option = input("What would you like to do? \n Type 'view' if you would like to view existing passwords. \n Type 'add' if you would like to add a new password. \n Type 'q' to quit. \n")
    if option == "q":
        print("Logging out... ")
        break

    if option == "view":
        view()
    elif option == "add":
        add()
    else:
        print("Invalid! Please write 'view', 'add', or 'q'") 
        continue