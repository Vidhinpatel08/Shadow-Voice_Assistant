import datetime
import random
import string
import time as tt
import webbrowser
import instadownloader
import time
import clipboard
import psutil
import pyautogui  # pip install pyautogui
import requests
import speedtest
import PyPDF2
import operator
import os
from bs4 import BeautifulSoup
import speech_recognition as sr #pip install speechRecognition
import features.TTS as TTS

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        TTS.speak_Print("Good Morning!")
    elif hour>=12 and hour<18:
        TTS.speak_Print("Good Afternoon!")   
    else:
        TTS.speak_Print("Good Evening!")  
    TTS.speak_Print("I am Shadow Sir. Please tell me how may I help you") 
         
def text2speech():
    text = clipboard.paste()
    TTS.speak_Print(text)

def screenshot():
    name_img = tt.time()
    name_img = f'ShadowGui/features/screenshots/{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def cpu():
    usage = str(psutil.cpu_percent())
    TTS.speak_Print(f'CPU USage is at {usage}')
    battery = psutil.sensors_battery()
    TTS.speak_Print(f'battery is at {battery.percent}')

def batteryPer():
    battery = psutil.sensors_battery().percent
    TTS.speak_Print(f'sir our system have {battery} percent battery')
    if battery >=75 :
        TTS.speak_Print('we have enough power to continue our work')
    elif battery >=40:
        TTS.speak_Print('we should connect our system to charging point to charge battery')
    elif battery >=15:
        TTS.speak_Print('we don\'t have enough power to work, please connect to charging..')
    else:
        TTS.speak_Print('we have very low power, please connect to charging the system will shutdown very soon !!')

def passwordgen(passlen=8):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = r"@#$_-+"

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print('Password Is: ',newpass)
    clipboard.copy(newpass)
    TTS.speak_Print(newpass)

def aboutFunction():
    TTS.speak("I am Shadow 2.0 An advanced AI model.")
    TTS.speak("I am here to assist you to use this app easily")

def temperature(at='Visnagar'):
    search = 'temperature in '+at
    url = f'https://www.google.com/search?q={search}'
    r= requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div",class_="BNeawe").text
    TTS.speak_Print(f"current {search} is {temp}")

def internetspeed():
    TTS.speak_Print("Wait for Sometime, I'm fetching now...")
    st = speedtest.Speedtest()
    dl, up = st.download(), st.upload()
    TTS.speak_Print(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')

def Mylocation():
    TTS.speak("wait sir, let me check") 
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        # print("Ip Address", ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        # print(geo_data)
        city =  geo_data['city']
        state = geo_data['region']
        country=  geo_data['country'] 
        TTS.speak_Print(f"sir i am not sure, but i think we are in {city} city of {state} in {country} ")
    except Exception as e:
        TTS.speak_Print("Sorry sir, Due to network issue i am not able to find where we are.")
        pass

def InstaDownload():
    TTS.speak_Print("sir please enter the user name correctly.")
    name = input("Enter username here :")
    webbrowser.open(f"www.instagram.com/{name}")
    TTS.speak(f"Sir here is the profile of the user {name}")
    time.sleep(5)
    TTS.speak("sir would you like to download profile picture of this account.")
    condition = TTS.takeCommand().lower()
    if "yes" in condition:
        mod = instadownloader.instaloader.Instaloader() #pip install instadownloader
        os.chdir(r"ShadowGui\features\secure\InstaImage\\")
        mod.download_profile(name, profile_pic_only=True)
        TTS.speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
    else:
        pass

def pdf_reader():
    try:
        TTS.speak_Print("sir please enter path of pdf")
        # pdfName = "D:/College/Python%20-%205/E-book/LEARN%20PYTHON%20THE%20HARD%20WAY.pdf".replace('%20',' ')
        pdfName = input("path of pdf : ").replace('%20',' ')
        book = open(pdfName, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(book) 
        pages = pdfReader.numPages
        TTS.speak_Print(f"Total numbers of pages in this book {pages} ")
        TTS.speak_Print("sir please enter the page number i have to read")
        pg = int(input("Please enter the page number: "))-1
        # try:
        #     pg = int(takeCommand().lower())-1
        # except Exception as  e :
        #     speak('sorry sir, but Input geting as sentence Please enter the page number')
        #     pg = int(input("Please enter the page number: "))-1
        try:
            page = pdfReader.getPage(pg)
            text = page.extractText()
            TTS.speak(text)
        except Exception as  e :
            TTS.speak_Print('sorry sir, pagenumber not match')

    except Exception as e :
        TTS.speak(f'something wrong, try again')
        pdf_reader()

def command_whatsup():
    st_msgs = [
        "Just doing my thing!",
        "I am fine!",
        "Nice!",
        "I am nice and full of energy",
    ]
    TTS.speak(random.choice(st_msgs)+ 'what\'s About you')

def appendnote():
    note = TTS.takeCommand()
    file = open(r'ShadowGui\features\remeberNote.txt', 'a')
    # strTime = datetime.datetime.now().strftime("%H:%M:%S")
    strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    file.write('\n')
    file.write(strTime)
    file.write(" :- ")
    file.write(note)
    print(note)
    TTS.speak('Note appending successfully')
    file.close()

def writenote():
    note = TTS.takeCommand()
    file = open(r'ShadowGui\features\remeberNote.txt', 'w')
    strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    file.write(strTime)
    file.write(" :- ")
    file.write(note)
    print(note)
    TTS.speak('Note Added successfully')
    file.close()

def shownote():
    file = open(r"ShadowGui\features\remeberNote.txt", "r")
    fileData = file.readlines()
    print(''.join(fileData))
    fileData = 'next Note is'.join(fileData)
    TTS.speak(fileData)
    file.close()

def calculate():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            TTS.speak("Say what you want to calculate, example: 3 plus 3") 
            print("listening.....") 
            r.adjust_for_ambient_noise (source)
            audio = r.listen(source) 
        my_string=r.recognize_google(audio) 
        print(my_string) 
        def get_operator_fn(op):
            return {
                '+': operator.add, #plus
                '-' : operator.sub, #minus
                'x': operator.mul, #multiplied by
                '/' :operator.__truediv__  #divided
            }[op]
        def eval_binary_expr (op1, oper, op2): # 5 plus 8 
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)

        message = f"your result is {eval_binary_expr(*(my_string.split()))}"
        TTS.speak_Print(message)	
    except Exception as e :
        print(e)
        TTS.speak("Sorry Sir try Again")

if __name__ == "__main__":
    # shownote()
    calculate()
    pass
