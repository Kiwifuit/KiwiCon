import datetime, random, wmi
from psutil import sensors_battery, cpu_count, boot_time, users
from cmd import Cmd

splash = [
    "Alt+F4 to solve all problems",
    "Go suck cock",
    "YEE YEE ASS HAIRCUT",
    "Also Try Terraria",
    "Also Try Minecraft",
    "Me, a developer listing splashes like a meme: Hmmmmmmmm",
    "e3.mahkiwi123.repl.co",
    "Ah shit, here we go again",
    "Shre, you're a cool guy",
    "Wassup fuckers",
    "Wassup fuckees",
    "This is a splash",
    "Venti"
]
battery = sensors_battery()
cpuCount = cpu_count()
boot = boot_time()
userList = users()
c = wmi.WMI()
sys = c.Win32_ComputerSystem()[0]

banner = """

██╗  ██╗██╗██╗    ██╗██╗     ██████╗ ██████╗ ███╗   ██╗     Manufacturer/Brand: {1}
██║ ██╔╝██║██║    ██║██║    ██╔════╝██╔═══██╗████╗  ██║     Device Name: {2}
█████╔╝ ██║██║ █╗ ██║██║    ██║     ██║   ██║██╔██╗ ██║     Battery Percentage: {3}%
██╔═██╗ ██║██║███╗██║██║    ██║     ██║   ██║██║╚██╗██║     Is Plugged: {4}
██║  ██╗██║╚███╔███╔╝██║    ╚██████╗╚██████╔╝██║ ╚████║     Device Booted on: {5}
╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝     Active Users: {6}
    Made by Kiwifruit | {0}

""".format(random.choice(splash), sys.Manufacturer, sys.Name, battery.percent, battery.power_plugged, datetime.datetime.fromtimestamp(boot).strftime("%Y-%m-%d %H:%M:%S"), len(userList))


class main(Cmd):
    prompt = "> "
    intro = banner
    def test(self, arg):
        """Test Function"""
        print(*parse(arg))


main().cmdloop()