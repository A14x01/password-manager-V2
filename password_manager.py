from cipher import rot13
from func import view, add, remove, login

try:
    with open("master.txt", "x") as f:
        f.close()
except:
    pass

with open("master.txt", "r") as f:
    master = f.readlines()
    while True:
        if master == []:
            with open("master.txt", "a") as f:
                master_password = input("Make your master password: ")
                f.write(rot13(master_password))
                print("Welcome to password manager")
                break
        else:
            master_password = input("Master password: ")
            if rot13(master_password) == master[0]:
                print("Welcome")
                break
            print("Wrong password, try again")
try:
    with open('password.txt', 'x') as f:
        f.close()
except:
    pass

while True:
    print("\nIf you want to sign in to your account write login.")
    print("If you want to add a new account write add.\nIf you want to view existing accounts write view.")
    print("If you want to remove existing account write remove.")
    mode = input("Press q to quit\n").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "login":
        login()
    elif mode == "remove":
        remove()
    else:
        print("Wrong mode")
        continue

#code made by https://github.com/A14x01
