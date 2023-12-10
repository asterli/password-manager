#ask user for the main password to access the password manager
pwd = input("Enter the main password: ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username:", user, "| Password:", passw)

def add():
    username = input("Username: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(username + "|" + pwd + "\n")

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