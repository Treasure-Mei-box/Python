import getpass
store_username = "admin"
store_password = "secure123"

username = input("Entrer username: ")
password = getpass.getpass("Enter password: ")

if (username == store_username) and (password == store_password):
    print ("Access Granted. Welcome !")
else:
    print("Access Denied! Incorrect username or password")