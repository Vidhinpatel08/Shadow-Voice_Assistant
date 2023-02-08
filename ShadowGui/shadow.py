import os
import sys
import time
import datetime
import webbrowser
import pyjokes 
import pyautogui 
# import pyttsx3 
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import pywhatkit as kit # pip install pywhatkit 
import features.emailmodule as em
import features.whatsapp as wp
import features.mynewsapi as news
import features.musiclist as musiclist
import features.feature as f
import features.alarmtime as alarm
from requests import get
from shadowUi import Ui_ShadowUI

from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate, Qt 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)

# def speak(audio):
#     """Take String as input and say on audio with help of speakers.."""
#     # print(f'Computer Said : {audio}')
#     engine.say(audio)
#     engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super (MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        """takeing Command as query for the Microphone and return string as output"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening...")
            r.pause_threshold = 2 # time of stop between your speech to exection 
            r.energy_threshold = 200  # increment if backgroud voice high.. & decrement if voice not peroper listening.. 
            audio = r.listen(source)

        try :
            print("Recognizing...")
            query = r.recognize_google(audio,language= 'en-in')
            print(f'User Said : {query}')

        except Exception as e :
            print('Say that again Please...')
            return 'None'
        
        return query.lower().strip()

    def TaskExecution(self):
        while True:
            permission = self.takeCommand()
            if 'wake up' in permission :
                f.wishMe()
                while True:
                    query = self.takeCommand()
                    if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                    if 'search' in query:
                        speak('Searching on google...')
                        query = query.replace("search", "")
                        webbrowser.open(f"https://www.google.com/search?q={query}")

                    elif 'open google' in query:
                        print('Sir, what should i search in Google')
                        speak('Sir, what should i search in Google')
                        cm = self.takeCommand()
                        webbrowser.open(f"{cm}")

                    elif 'open youtube' in query:
                        print('\nWhat should I Search on Youtube ?',end='')
                        speak('What should I Search on Youtube ?')
                        cm = self.takeCommand().lower()
                        kit.playonyt(cm) 

                    elif "play songs on youtube" in query:
                        speak('Sir, what would you like to listen ?')
                        cm = self.takeCommand().lower()
                        kit.playonyt(cm) 

                    elif "open facebook" in query:
                        webbrowser.open("www.facebook.com")

                    elif 'open stack overflow' in query:
                        webbrowser.open("stackoverflow.com")   

                    elif "send message" in query or "send a message" in query or "send a message on whatsapp" in query  or "send message on whatsapp" in query or "send whatsapp message" in query:
                        wp.message(query)

                    elif 'play music' in query:
                        musiclist.playmusic()

                    # elif 'covid' in query:
                        f.covid()

                    elif 'cpu' in query:
                        f.cpu()

                    elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
                        f.batteryPer()

                    elif 'screenshot' in query:
                        f.screenshot()

                    elif 'create password' in query or 'generate password' in query:
                        f.passwordgen()

                    elif 'read clipboared' in query:
                        f.text2speech()

                    elif 'current temperature' in query:
                        if "in" in query:
                            recipient = query.split("current temperature in")[-1].strip()
                            f.temperature(at=recipient)
                        else:
                            f.temperature()

                    elif 'temperature' in query:
                        if "in" in query or "at" in query:
                            recipient = query.split("in")[-1].strip()
                            f.temperature(at=recipient)
                        else: 
                            f.temperature()

                    elif 'internet speed' in query or 'internetspeed' in query :
                            f.internetspeed()

                    elif 'what is time' in query or 'current time'in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        speak(f"Sir, the time is {strTime}")
        
                    elif 'current date' in query or 'what is date' in query or 'what is the date' in query:
                        year = datetime.datetime.now().year
                        month = datetime.datetime.now().month
                        date = datetime.datetime.now().day
                        speak(f"the current date is: {date}date,{month}month,{year}year.")
                                
                    elif 'open code' in query:
                        codePath = r"C:\Users\vidhi\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                        os.startfile(codePath)

                    elif 'close vs code' in query or 'close vscode' in query:
                        speak("Okk sir, cloasing  notepad")
                        os.system('taskkill /f /im code.exe')

                    elif 'open notepad' in query:
                        codePath = "C:\\Windows\\System32\\notepad.exe" 
                        os.startfile(codePath)

                    elif 'close notepad' in query:
                        speak("Okk sir, cloasing  notepad")
                        os.system('taskkill /f /im notepad.exe')

                    elif 'open command prompt' in query or 'cmd' in query:
                        os.system("start cmd")

                    elif 'ip address' in query:
                        ip = get("https://api.ipify.org").text
                        print(f"your ip address is {ip}")
                        speak(f"your ip address is {ip}")

                    elif 'email to' in query or 'send email' in query or 'send a email' in query:
                        em.mailQuery(query)

                    elif "set alarm" in query or "set an alarm" in query or "set the alarm" in query or "alarm" in query:
                        speak("Sir now can excess the terminal to set alarm")
                        alarm.alaramplay()
                        speak("Okk sir, your alarm command completed now")

                    elif 'set timer' in query or 'stopwatch' in query:
                        speak("For how many minutes?")
                        timing = self.takeCommand()
                        if timing != None or timing != 'none':
                            timing =timing.replace('minutes', '')
                            timing = timing.replace('minute', '')
                            timing = timing.replace('for', '')
                            timing = float(timing)
                            timing = timing * 60
                            speak(f'I will remind you in {timing} seconds')
                            time.sleep(timing)
                            speak('Your time has been finished sir')

                    elif "tell me joke" in query or "tell joke" in query or "tell me  a joke" in query or "tell a joke" in query:
                        joke = pyjokes.get_joke()
                        # (language='en', category='neutral')    category: str => Choices: 'neutral', 'chuck', 'all', 'twister'
                        print(joke)
                        speak(joke)
                    
                    elif 'switch the window' in query:
                        pyautogui.keyDown("alt")  
                        time.sleep(1)          
                        pyautogui.press("tab")            
                        pyautogui.keyUp("alt")            
                        
                    elif "tell me news" in query or "tell me somenews" in query or "news" in query :
                        speak("please Wait sir, feteching the latest news.")
                        news.news()

                    elif 'hi' in query or 'hello' in query or "hey" in query or "who are you" in query or  "your intro" in query:
                        f.aboutFunction()

                    elif "sleep shadow" in query or "sleep now" in query or 'you can sleep' in query:
                        speak('okay sir, I am going to sleep you can call me anytime. ')
                        break

                    elif "goodbye" in query or "good bye" in query  or "bye" in query :
                        speak('Thanks for useing me sir, have a good day')
                        speak('Sorry but Can you click on EXIT to Stop me.')
                        sys.exit()

            elif "goodbye" in permission or "good bye" in permission  or "bye" in permission :
                speak('Thanks for useing me sir, have a good day')
                speak('Sorry but Can you click on EXIT to Stop me.')
                sys.exit()

startExecution = MainThread()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ShadowUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)        
        self.ui.pushButton_2.clicked.connect(self.close)  
        speak(f'sir, Please click on RUN button to start me & click On EXIT to Stop me.')

    def starttask(self):
        self.ui.movie = QtGui.QMovie(r"ShadowGui\images\Main.gif")      # path of main bg_image (Labal-1)
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"ShadowGui\images\Initial.gif")      # path of (Labal-2)
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"ShadowGui\images\Shadow.gif")      # path of (Labal-3)
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer= QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


if __name__=="__main__":
    app = QApplication(sys.argv)
    shadow = Main()
    shadow.show()
    exit(app.exec_())
