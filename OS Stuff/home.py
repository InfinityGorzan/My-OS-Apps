import time
import os
import socket

print("""
██╗███╗░░██╗███████╗██╗███╗░░██╗██╗████████╗██╗░░░██╗██╗░░██╗  ░█████╗░░██████╗██╗░░██╗
██║████╗░██║██╔════╝██║████╗░██║██║╚══██╔══╝╚██╗░██╔╝╚██╗██╔╝  ██╔══██╗██╔════╝╚██╗██╔╝
██║██╔██╗██║█████╗░░██║██╔██╗██║██║░░░██║░░░░╚████╔╝░░╚███╔╝░  ██║░░██║╚█████╗░░╚███╔╝░
██║██║╚████║██╔══╝░░██║██║╚████║██║░░░██║░░░░░╚██╔╝░░░██╔██╗░  ██║░░██║░╚═══██╗░██╔██╗░
██║██║░╚███║██║░░░░░██║██║░╚███║██║░░░██║░░░░░░██║░░░██╔╝╚██╗  ╚█████╔╝██████╔╝██╔╝╚██╗
╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░╚═╝░░╚═╝
""")

login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

def bios():
    print("Opening BIOS")
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("[1] Username: " + l_n)
    print("[2] Password: " + l_p)
    print("Host name: " + host_name)
    print("Local IP: " + host_ip)
    edit_b = input("Enter [?] to change setting: ")
    if edit_b == '1':
        edit_n = input("Enter new username: ")
        with open('user/username.txt', "w") as f:
            f.writelines(edit_n)
        print("Username changed to " + edit_n)
        input("Press enter to close window.\n")
        pass

    if edit_b == '2':
        edit_p = input("Enter new password: ")
        with open('user/password.txt', "w") as f:
            f.writelines(edit_p)
        print("Password changed to " + edit_p)
        input("Press enter to close window.\n")
        pass

print("WELCOME " + l_n)
print("The date is " + time.strftime("%d/%m/%y"))
print("""
[1] To open Google
[2] To open Text Editor
[3] To open File Manager
[4] To configure and open BIOS
[5] To close OS safely
""")

cmds = ["$sudo BIOS-open = 1"]
select = input("[?]: ")

def checkCMD(i):
    if i == 0:
        bios()

if select == '1':
    os.startfile('brows.py')

elif select == '2':
    os.startfile('edit.py')

elif select == '3':
    os.startfile('file.py')

elif select == '4':
    while True:
        b_login = input(str("Please enter the password to " + l_n + " to open BIOS: "))
        if b_login == l_p:
            print("Opening BIOS")
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("[1] Username: " + l_n)
            print("[2] Password: " + l_p)
            print("Host name: " + host_name)
            print("Local IP: " + host_ip)
            edit_b = input("Enter [?] to change setting: ")
            if edit_b == '1':
                edit_n = input("Enter new username: ")
                with open('user/username.txt', "w") as f:
                    f.writelines(edit_n)
                print("Username changed to " + edit_n)
                input("Press enter to close window.\n")
                break

            if edit_b == '2':
                edit_p = input("Enter new password: ")
                with open('user/password.txt', "w") as f:
                    f.writelines(edit_p)
                print("Password changed to " + edit_p)
                input("Press enter to close window.\n")
                break

        else:
            print("Wrong password to " + l_n)

elif select == '5':
    pass

else:
    i = 0
    if i < 1:
        if select == cmds[i]:
            checkCMD(i)
        else:
            i = i+1
            