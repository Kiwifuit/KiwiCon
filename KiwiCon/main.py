import datetime, random, wmi, getpass
from psutil import sensors_battery, cpu_count, boot_time, users
from morse_code import encrypt, decrypt
from time import sleep
import re
import sys

speedBuffer = 0.25

def retroIterate(content=list):
    for line in content:
        print(line)
        sleep(speedBuffer)

splash = [
    "Alt+F4 to solve all problems",
    "YEE YEE ASS HAIRCUT",
    "Also Try Terraria",
    "Also Try Minecraft",
    "Me, a developer listing splashes like a meme: Hmmmmmmmm",
    "Also try your MOM",
    "e3.mahkiwi123.repl.co",
    "Ah shit, here we go again",
    "Shre, you're a cool guy",
    "Wassup fuckers",
    "Wassup fuckees",
    "This is a splash",
    "Venti",
    "Batch to Python conversion is pretty poggers",
    "Hello {0}, hope you are doing alright".format(getpass.getuser()),
    "[sad microwave noises]",
    "Empathy Banana coming your way"
]

battery = sensors_battery()
cpuCount = cpu_count()
boot = boot_time()
userList = users()
c = wmi.WMI()
computer = c.Win32_ComputerSystem()[0]
plugged = "Yes" if battery.power_plugged is True else "No"
banner = """
██╗  ██╗██╗██╗    ██╗██╗     ██████╗ ██████╗ ███╗   ██╗     Manufacturer/Brand: {1}
██║ ██╔╝██║██║    ██║██║    ██╔════╝██╔═══██╗████╗  ██║     Device Name: {2}
█████╔╝ ██║██║ █╗ ██║██║    ██║     ██║   ██║██╔██╗ ██║     Battery Percentage: {3}%
██╔═██╗ ██║██║███╗██║██║    ██║     ██║   ██║██║╚██╗██║     Is Plugged: {4}
██║  ██╗██║╚███╔███╔╝██║    ╚██████╗╚██████╔╝██║ ╚████║     Device Booted on: {5}
╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝     Active Users: {6}
    Made by Kiwifruit | {0}

""".format(random.choice(splash), computer.Manufacturer, computer.Name, battery.percent, plugged, datetime.datetime.fromtimestamp(boot).strftime("%Y-%m-%d %H:%M:%S"), len(userList))

retroIterate(banner.split("\n"))
availableCommands = [
    "help <command | None>",
    "morse [encode | decode] [text]",
    "echo [text]",
    "write [file name] [text]",
    "read [file name]",
    "hash [method] [text]",
    "set [variable] <content>"
]

while True:
    command = input("> ").lower()
    match command:
        case "help":
            if len(command.split()) != 1:
                args = command.split()
                if args in availableCommands:
                    print(f"Syntax {availableCommands[args]}")
                    sleep(3)
                    match availableCommands.index(args):
                        case 0:
                            print("\nShows all available commands")
                            break
                        case 1:
                            print("\nEncodes or decodes 'text' depending on the mode")
                            break
                        case 2:
                            print("\nDisplays 'text'")
                            break
                        case 3:
                            print("\nWrites to a file with 'file name' as the file's name and 'text' as the new file's content")
                            break
                        case 4:
                            print("\nSame as WRITE, minus the text part")
                            break
                        case 5:
                            print("Hashes with 'mode' as hashing algorithm and 'text' as the text to hash")
                            break
                        case 6:
                            print("sets 'variable' as a variable and 'content' as it's value.\nNOTE: Variable is temporary")
                            break
                        case _:
                            print("UNKNOWN")
                            break
                else:
                    print(f"Unknown Command \"{command}\". Please use \"help\" for list of all commands")
            else:
                retroIterate(["Available Commands. Type \"help <command>\" for more information about the command", "======================================================================================="])
                retroIterate(content= availableCommands)
        case _:
            print(f"Unknown Command \"{command}\". Please use \"help\" for list of all commands")
