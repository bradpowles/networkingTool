from sys import version_info
import subprocess
import time
import re
import os
os.system("cls")
os.system("color a")
proc = str(subprocess.Popen(["ipconfig","/all"], stdout=subprocess.PIPE, shell=True).communicate())
ipv4 = (str(re.findall("(?<=IPv4 Address. . . . . . . . . . . : )(\d+\.\d+\.\d+\.\d+)",proc)))
dhcp = (str(re.findall("(?<=DHCP Server . . . . . . . . . . . : )(\d+\.\d+\.\d+\.\d+)",proc)))
submask = (str(re.findall("(?<=Subnet Mask . . . . . . . . . . . : )(\d+\.\d+\.\d+\.\d+)",proc)))

def menu():
    print("\n\n\n************************************************************\n\n")
    print("         1 - Custom command ")
    print("         2 - Display IP configuration ")
    print("         3 - Trace route to any website/IP")
    print("         4 - Ping an IP/website with customization")
    print("         5 - Display all important network information")
    print("         6 - Find all IPV4 addresses connected to your LAN ")
    print("\n         e - Exit Program")
    print("\n")
    print("************************************************************")
def takeInput(message):
    try:
        reply = raw_input(message)
    except:
        reply = input(message)
    return reply
def main():
    menu()
    opt = takeInput("> ")
    if opt == "e":
        print("\n\nProgram closing")
        os.system("color 7")
        os.system("cls")
    elif opt == "1":
        opt = input("Command> ")
        os.system(opt)
        main()
    elif opt == "2":
        os.system("ipconfig /all")
        main()
    elif opt == "3":
        opt2 = input("Address or exit (e)> ")
        if opt2 == "e" or opt2 == "exit":
            main()
        else:
            full = "tracert "+opt2
            os.system(full)
            main()
    elif opt == "4":
        opt2 = input("Address or exit (e)> ")
        if opt2 == "e" or opt2 == "exit":
            main()
        else:
            print("\nInput how much time in ms until the ping times out")
            print("Tip for average ping times in ms - Good ping:<5 | Medium ping:30 | Bad ping:>100")
            opt3 = input("Time? (0-255 ms) or exit (e)> ")
            if opt3 == "e" or opt3 == "exit":
                main()
            else:
                print("\nInput how many times the address will be pinged")
                print("Tip for average tries - If tries have to go above 4, there is usually a network issue. ")
                opt4 = input("Tries? (0-1000) or exit (e)> ")
                if opt4 == "e" or opt4 == "exit":
                    main()
                else:
                    full = "ping "+opt2+" -i "+opt3+" -n "+opt4
                    os.system(full)
                    main()
    elif opt == "5":
        print("Networking Information:\n\n")
        print("Default Gateway: ",dhcp)
        print("Network DHCP server: ",dhcp)
        print("Current subnet mask: ",submask)
        print("Current IPV4 Address: ",ipv4)
        main()
    elif opt == "6":
        os.system("arp -a")
        main()
    else:
        print("Invalid option...")
        main()


main()
