import datetime
import requests
import time as tt
import random
import string
import psutil 
import clipboard
import pyautogui # pip install pyautogui

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")  

    print("I am Shadow Sir. Please tell me how may I help you") 
    speak("I am Shadow Sir. Please tell me how may I help you") 
         
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'./features/screenshots/{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+ usage)
    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def aboutFunction():
    speak("I am Shadow 2.0 An advanced AI model.")
    speak("I am developed by Vidhin , Jeet and Jeneesh Patel") 
    speak("I am here to assist you to use this app easily")
    tt.sleep(0.5)
    speak("In this software, I will be assisting you in few tasks like")
    speak("doing google search")
    tt.sleep(0.2)
    speak("opening any software")
    tt.sleep(0.2)
    speak("and a lot more.")
    tt.sleep(0.5)
