import requests
from colorama import *
import os 
import time
import random
url = input("[?] URL : ") 
proxy = input("[?] Proxy : ") # 69.163.161.209:38713
proxies = {
    'https' : 'https://'+proxy
}
txt = requests.get(url,proxies=proxies)
print(Fore.RED+txt.text) 