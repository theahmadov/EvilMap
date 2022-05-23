import requests
from colorama import *
import os 
import time
import random

init(convert=True)

os.system('cls' if os.name == 'nt' else 'clear') 

https_file = open("./output/https.txt","a") 
socks4_file = open("./output/socks4.txt", "a")
http_file = open("./output/http.txt", "a")
socks5_file = open("./output/socks5.txt", "a")

rhttps = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rhttp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rs4 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4')
rs5 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5')


https = []
https = rhttps.text
https = https.split()
lines = len(https)



http = []
http = rhttp.text
http = http.split()
hlines = len(http)


socks4 = []
socks4 = rs4.text
socks4 = socks4.split()
slines = len(socks4)


socks5 = []
socks5 = rs5.text
socks5 = socks5.split()
sslines = len(socks5)
number = random.randint(1, 5)

def getsocks4():
    for i in range(number):
        print(Fore.BLUE + "[ " + Fore.LIGHTCYAN_EX + "HTTPS" + Fore.BLUE + " ] " + Fore.BLUE + https[number])
        time.sleep(0.1)




def getsocks5():
    for b in range(number):
        print(Fore.BLUE + "[ " + Fore.RED + "SOCKS5" + Fore.BLUE + " ] " + Fore.BLUE + socks5[number])
        time.sleep(0.1)



def main():
    print(Fore.BLUE + """

""")
    time.sleep(3)
    print(Fore.BLUE + "[ " + Fore.BLUE  + "1" + Fore.BLUE + " ] " + Fore.BLUE + "HTTPS")
    print(Fore.BLUE + "[ " + Fore.BLUE  + "2" + Fore.BLUE + " ] " + Fore.BLUE + "HTTP")
    print(Fore.BLUE + "[ " + Fore.BLUE  + "3" + Fore.BLUE + " ] " + Fore.BLUE + "SOCKS4")
    print(Fore.BLUE + "[ " + Fore.BLUE  + "4" + Fore.BLUE + " ] " + Fore.BLUE + "SOCKS5")
    print(Fore.RESET + ' ')
    a = input(Fore.BLUE + "Choose Type of Proxy : ")
    if(a == "1"):
        for i in range(lines):
            print(Fore.BLUE + "[ " + Fore.BLUE + "Success -> HTTPS" + Fore.BLUE + " ] " + Fore.BLUE + https[i])
            https_file.write('\n' + https[i])
            time.sleep(0.1)
    elif(a == "2"):
        for a in range(hlines):
            print(Fore.BLUE + "[ " + Fore.BLUE + "Success -> HTTP" + Fore.BLUE + " ] " + Fore.BLUE + http[a])
            http_file.write('\n' + http[a])
            time.sleep(0.1)
    elif(a == "3"):
        for b in range(slines):
            print(Fore.BLUE + "[ " + Fore.BLUE + "Success -> SOCKS4" + Fore.BLUE + " ] " + Fore.BLUE + socks4[b])
            socks4_file.write('\n' + socks4[b])
            time.sleep(0.1)
    elif(a == "4"):
        for c in range(sslines):
            print(Fore.BLUE + "[ " + Fore.BLUE + "Success -> SOCKS5" + Fore.BLUE + " ] " + Fore.BLUE + socks5[c])
            socks5_file.write('\n' + socks5[c])
            time.sleep(0.1)
    else:
        print(Fore.RED+f"No Option Found Named -> '{a}' ")
        
if __name__ == "__main__":

    main()
    print(Fore.GREEN+"[+] All Proxy's Successfully Generated And Saved To File!")
