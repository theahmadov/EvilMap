import requests
from colorama import *
import os 
import time
import random

def menu():
    print(Fore.RED+"""       
 _____       _ _   __  __             
| ____|_   _(_) | |  \/  | __ _ _ __  
|  _| \ \ / / | | | |\/| |/ _` | '_ \ 
| |___ \ V /| | | | |  | | (_| | |_) |
|_____| \_/ |_|_| |_|  |_|\__,_| .__/ 
                             |_|    
""")
    print(Fore.BLUE+"""       
                             
[1] > Proxy Generator         
    [c1] > Rotate Ip (Using fake ip)

                # © Error
""")
def evilmap():
    menu()
    n = input("[?] Please Select : ")
    
    if n=="1":
        os.system("python3 ./main/proxygenerator.py")
        print(Fore.RED+"Outputs saved to ./output folder")
    elif n == "c1":
        os.system("python3 ./main/connectproxy.py")
        
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') 
    evilmap()
    