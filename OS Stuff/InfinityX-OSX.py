from time import sleep
from tqdm import tqdm
import time
import os
import sys

print("""
██╗███╗░░██╗███████╗██╗███╗░░██╗██╗████████╗██╗░░░██╗██╗░░██╗  ░█████╗░░██████╗██╗░░██╗
██║████╗░██║██╔════╝██║████╗░██║██║╚══██╔══╝╚██╗░██╔╝╚██╗██╔╝  ██╔══██╗██╔════╝╚██╗██╔╝
██║██╔██╗██║█████╗░░██║██╔██╗██║██║░░░██║░░░░╚████╔╝░░╚███╔╝░  ██║░░██║╚█████╗░░╚███╔╝░
██║██║╚████║██╔══╝░░██║██║╚████║██║░░░██║░░░░░╚██╔╝░░░██╔██╗░  ██║░░██║░╚═══██╗░██╔██╗░
██║██║░╚███║██║░░░░░██║██║░╚███║██║░░░██║░░░░░░██║░░░██╔╝╚██╗  ╚█████╔╝██████╔╝██╔╝╚██╗
╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░╚═╝░░╚═╝
""")

for i in tqdm(range(10)):
    sleep(2)

time.sleep(2)
print("""
[1] Open basic BIOS
[2] Shut down PC
[3] Reset PC
[4] Continue loading OS
""")

def reset():
    os.remove("user/password.txt")
    os.remove("user/username.txt")
    print("PC resetted succesfully")

boot = input("[?]: ")
if boot == "1":
    os.startfile("bios.py")
elif boot == "2":
    sys.exit("Shutting down PC")
elif boot == "3":
    try:
        login_pass = open('user/password.txt')
        login_name = open('user/username.txt')
    except:
        reset()
    else:
        login_pass = open('user/password.txt')
        login_name = open('user/username.txt')
        l_p = login_pass.read()
        l_n = login_name.read()
        r_login = input(str("Please enter the password to " + l_n + " to reset PC: "))
        if r_login == l_p:
            try:
                login_pass.close()
            except:
                pass

            try:
                login_name.close()
            except:
                pass
            reset()
        else:
            print("Continuing back to OS, because password is incorrect.")

else:
    pass    

print("""
[1] Continue with Setup. I didn't setup
[2] I completed Setup. No need to setup
""")

setup = input("[?]: ")

if setup == "1":
    name = input(str("Please enter your username: "))
    psw = input(str("Please enter your password: "))

    with open('user/username.txt', "w") as f:
        f.writelines(name)

    with open('user/password.txt', "w") as f:
        f.writelines(psw)
    print("Setup complete!!!")
    input("Press enter to exit application\n")

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    if setup == '2':
        login = input(str("Please enter the password to " + l_n + ": "))
        if login == l_p:
            os.startfile("home.py")
            break
        else:
            print("Wrong password!!!")
    else:
        break