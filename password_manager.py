from cryptography.fernet import Fernet

#ask user for the main password to access the password manager
main_pwd = input("Enter the main password: ")

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
'''

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("Username:", user, "| Password:", pwd)

def add():
    user = input("Username: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(user + "|" + pwd + "\n")

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