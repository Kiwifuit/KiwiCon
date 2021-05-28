import datetime, random, wmi, requests, subprocess, os, getpass, string
from psutil import sensors_battery, cpu_count, boot_time, users
from cmd import Cmd
from morse_code import encrypt, decrypt

# Program-specific variables
_version = "0.0.1"
_build = "Portation Build"
_author = "Kiwifruit"


# Splash text list (randomized)
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
    "CONdolences to your dead cat Andrew. He needed a KIWI.",
    "Batch to Python conversion is pretty poggers",
    "Hello {0}, hope you are doing alright".format(getpass.getuser()),
    "[sad microwave noises]",
]
# Device information
battery = sensors_battery()
cpuCount = cpu_count()
boot = boot_time()
userList = users()
c = wmi.WMI()
sys = c.Win32_ComputerSystem()[0]
plugged = "Yes" if battery.power_plugged is True else "No"

banner = """
██╗  ██╗██╗██╗    ██╗██╗     ██████╗ ██████╗ ███╗   ██╗     Manufacturer/Brand: {1}
██║ ██╔╝██║██║    ██║██║    ██╔════╝██╔═══██╗████╗  ██║     Device Name: {2}
█████╔╝ ██║██║ █╗ ██║██║    ██║     ██║   ██║██╔██╗ ██║     Battery Percentage: {3}%
██╔═██╗ ██║██║███╗██║██║    ██║     ██║   ██║██║╚██╗██║     Is Plugged: {4}
██║  ██╗██║╚███╔███╔╝██║    ╚██████╗╚██████╔╝██║ ╚████║     Device Booted on: {5}
╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝     Active Users: {6}
    Made by Kiwifruit | {0}

""".format("Empathy Banana coming your way" if random.randint(1, 10) == 8 else random.choice(splash), sys.Manufacturer, sys.Name, battery.percent, plugged, datetime.datetime.fromtimestamp(boot).strftime("%Y-%m-%d %H:%M:%S"), len(userList))

class main(Cmd):
    prompt = "> "
    intro = banner
    doc_header = "Use 'help [command] for help on that command\nLegend:\n<name> = Option Parameter. Non-Customizable\n[name] = Input Parameter.Customizable\nAvailable Commands."
    undoc_header = "Experimental or Underdeveloped commands"
    def do_say(msg):
        """
Syntax: say [msg]
Repeats the message
        """
        try:
            print(msg)
        except:
            pass
    def do_ping(link):
        """
Syntax: ping [link]
Continuously pings a webpage in the internet. This can be used to check for:
a) Device connectivity (whether or not you are connected)
b) Webpage status (whether or not you can connect to said webpage)
        """
        output = subprocess.check_output("ping {0} -t".format(link))
        print(output)
    def do_shell(command):
        """
Syntax: shell [command]
Perform shell/Command prompt commands like echo, robocopy, del, ect.
        """
        output = subprocess.check_output(command)
        print(output)
    def do_quit(*args):
        """
Syntax: quit
Quits the program
        """
        print("See you later {0}. I hope we meet soon (^人^)".format(getpass.getuser()))
        exit()
    def do_morse(action, message, *args, ** kwargs):
        """
Syntax: morse <encode/decode> [message]
Encodes/Decodes a message depending on the action
        """
        try:
            action = str(action)
            message = str(message)
            if action == "encode":
                msg = encrypt(message)
                print(msg)
            elif action == "decode":
                msg = decrypt(message)
                print(msg)
            else:
                print("\nUnkown: {0}".format(action))
        except TypeError:
            pass
    def do_ranPass(length, *args):
        """
Syntax: ranPass [length]
Creates a random password using 'length' as the length of the password
you want
        """
        if isinstance(length, str):
            try:
                length = int(length)
                chars = string.ascii_letters + string.digits + ".@!#"
                charDump = []
                for i in range(length):
                    currentChosen = random.choice(chars)
                    charDump.append(currentChosen)
                print("\n".join(charDump))
            except:
                print("\nUnable to do that. Please check that param \"length\" is an integer\n")
        else:
            chars = string.ascii_letters + string.digits + ".@!#"
            charDump = []
            for i in range(length):
                currentChosen = random.choice(chars)
                charDump.append(currentChosen)
            print("\n".join(charDump))
    def do_debug(arg1, arg2):
        print("param1: {0}\param2: {0}".format(arg1, arg2))

main().cmdloop()
