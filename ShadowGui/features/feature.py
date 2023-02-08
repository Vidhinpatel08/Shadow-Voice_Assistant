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
import os
from bs4 import BeautifulSoup
import speech_recognition as sr #pip install speechRecognition


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def takeCommand():
    """takeing Command as query for the Microphone and return string as output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 2 # time of stop between your speech to exection 
        r.energy_threshold = 200  # increment if backgroud voice high.. & decrement if voice not peroper listening.. 
        audio = r.listen(source)

    try :
        query = r.recognize_google(audio,language= 'en-in')

    except Exception as e :
        print('Say that again Please...')
        return 'None'
    
    return query.lower().strip()


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
    name_img = f'ShadowGui/features/screenshots/{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def cpu():
    usage = str(psutil.cpu_percent())
    print(f'CPU USage is at {usage}')
    speak(f'CPU USage is at {usage}')
    battery = psutil.sensors_battery()
    print(f'battery is at {battery.percent}')
    speak(f'battery is at {battery.percent}')

def batteryPer():
    battery = psutil.sensors_battery().percent
    print(f'sir our system have {battery} percent battery')
    speak(f'sir our system have {battery} percent battery')
    if battery >=75 :
        speak('we have enough power to continue our work')
    elif battery >=40:
        speak('we should connect our system to charging point to charge battery')
    elif battery >=15:
        speak('we don\'t have enough power to work, please connect to charging..')
    else:
        speak('we have very low power, please connect to charging the system will shutdown very soon !!')


def passwordgen():
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = r"@#$_-+"

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print('Password Is: ',newpass)
    clipboard.copy(newpass)
    speak(newpass)

def aboutFunction():
    speak("I am Shadow 2.0 An advanced AI model.")
    speak("I am here to assist you to use this app easily")
    # speak("I am developed by Vidhin Patel, Jeet Patel and Jeneesh Patel") 

def temperature(at='Visnagar'):
    search = 'temperature in '+at
    url = f'https://www.google.com/search?q={search}'
    r= requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div",class_="BNeawe").text
    print(f"current {search} is {temp}")
    speak(f"current {search} is {temp}")

def internetspeed():
    speak('sir please, Waiting for 1 second I\'m feaching speed.....')
    st = speedtest.Speedtest()
    dl, up = st.download(), st.upload()
    print(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')
    speak(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')


def Mylocation():
    speak("wait sir, let me check") 
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
        print(f"sir i am not sure, but i think we are in {city} city of {state} in {country} ")
        speak(f"sir i am not sure, but i think we are in {city} city of {state} in {country} ")
    except Exception as e:
        speak("Sorry sir, Due to network issue i am not able to find where we are.")
        pass

def InstaDownload():
    speak("sir please enter the user name correctly.")
    name = input("Enter username here:")
    webbrowser.open(f"www.instagram.com/{name}")
    speak(f"Sir here is the profile of the user {name}")
    time.sleep(5)
    speak("sir would you like to download profile picture of this account.")
    condition = takeCommand().lower()
    if "yes" in condition:
        mod = instadownloader.instaloader.Instaloader() #pip install instadownloader
        os.chdir(r"ShadowGui\features\secure\InstaImage\\")
        mod.download_profile(name, profile_pic_only=True)
        speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
    else:
        pass

if __name__ == "__main__":
    InstaDownload()
    pass
