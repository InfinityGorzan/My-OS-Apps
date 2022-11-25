import os

print("""
██╗███╗░░██╗███████╗██╗███╗░░██╗██╗████████╗██╗░░░██╗██╗░░██╗  ░█████╗░░██████╗██╗░░██╗
██║████╗░██║██╔════╝██║████╗░██║██║╚══██╔══╝╚██╗░██╔╝╚██╗██╔╝  ██╔══██╗██╔════╝╚██╗██╔╝
██║██╔██╗██║█████╗░░██║██╔██╗██║██║░░░██║░░░░╚████╔╝░░╚███╔╝░  ██║░░██║╚█████╗░░╚███╔╝░
██║██║╚████║██╔══╝░░██║██║╚████║██║░░░██║░░░░░╚██╔╝░░░██╔██╗░  ██║░░██║░╚═══██╗░██╔██╗░
██║██║░╚███║██║░░░░░██║██║░╚███║██║░░░██║░░░░░░██║░░░██╔╝╚██╗  ╚█████╔╝██████╔╝██╔╝╚██╗
╚═╝╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░╚═╝░░╚═╝
""")

input("Press any key to open BIOS\n")
f = open("bios-settings.txt", "r")
fr = f.read()
fw = open("bios-settings.txt", "w")

print("""[0] Exit BIOS settings
[1] Additional protection by PCLocker.x is """ + fr)

bios = input(str("[?]: "))

while True:
    if bios == "0":
        break
    elif bios == "1":
        print("""
[1] Enable
[2] Disable
""")
        option = input(str("[?]: "))
        if option == "1":
            fw.write("Enabled")
        elif option == "2":
            fw.write("Disabled")
        break
    else:
        input("Press any key to go back to BIOS.\n")
        break

if bios != "0":
    os.startfile("bios.py")