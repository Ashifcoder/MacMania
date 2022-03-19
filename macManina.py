from platform import platform
import sys, subprocess, os
import random as ra

print('''
+-+-+-+-+-+-+-+-+-+-+ 
|M|a|c|-|M|a|n|i|n|a| 
+-+-+-+-+-+-+-+-+-+-+ 
       -by Ashifcoder
''')


def mac_changer(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def choose_interface():
    interfaces = os.listdir('/sys/class/net/')
    i_id = 0
    for interface_name in interfaces:
        print("Press {} for {} ".format(i_id, interface_name))
        i_id += 1
    global cinterface
    cinterface = interfaces[int(input("Choice: "))]
    return cinterface


def mac_gen():
    """mac generator using random function """
    mnum = []
    scharacter = ra.choice('26AE')
    for _ in range(11):
        mnum.append(ra.randint(0, 9))

    return f"{mnum[0]}{scharacter}:{mnum[1]}{mnum[2]}:{mnum[3]}{mnum[4]}:" \
           f"{mnum[5]}{mnum[-5]}:{mnum[-4]}{mnum[-3]}:{mnum[-2]}{mnum[-1]}"


if sys.platform == 'linux':
    print("Linux System Found!")
    if os.geteuid() == 0:
        print("[*] Welcome to MAC-Mania M^2 [*]")
        choose_interface()
        print(f"The older MAC of {cinterface}")
        os.system(f"cat /sys/class/net/{cinterface}/address")
        mac_changer(cinterface, mac_gen())
        print(f"New MAC-Mania of {cinterface}")
        os.system(f"cat /sys/class/net/{cinterface}/address")
    else:
        exit(
            "Please use the magic word :)\nPlease try again, using 'sudo'.\n**root privileges required to run this script**")
elif sys.platform == "darwin":
    print("Mac Os System Found!")
    if os.geteuid() == 0:
        print("[*] Welcome to MAC-Mania M^2 [*]")
        choose_interface()
        print(f"The older MAC of {cinterface}")
        os.system(f"cat /sys/class/net/{cinterface}/address")
        mac_changer(cinterface, mac_gen())
        print(f"New MAC-Mania of {cinterface}")
        os.system(f"cat /sys/class/net/{cinterface}/address")
    else:
        exit(
            "Please use the magic word :)\nPlease try again, using 'sudo'.\n**root privileges required to run this "
            "script**")

elif sys.platform == 'win32':
    print("Windows System Found!\nSystem Not Supported Yet :(")
    sys.exit()
else:
    print("Os determination Failed")
    sys.exit()
