import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit as kit # pip install pywhatkit 
import pyjokes  # pip install pyjokes 
from requests import get
import sys
import pyautogui # pip install pyautogui
import features.emailmodule as em
import features.whatsapp as wp
import features.mynewsapi as news
import features.musiclist as musiclist
import features.feature as f
import features.alarmtime as alarm
from shadowUi import Ui_ShadowUI

from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate, Qt 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QMovie
# from PyQt5.uic import loadUiType

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
        # f.wishMe()
        while True:
            self.query = self.takeCommand()
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            if 'search' in self.query:
                speak('Searching on google...')
                query = self.query.replace("search", "")
                webbrowser.open(f"{query}")

            elif 'open google' in self.query:
                print('Sir, what should i search in Google')
                speak('Sir, what should i search in Google')
                cm = self.takeCommand()
                webbrowser.open(f"{cm}")

            elif 'open youtube' in self.query:
                print('\nWhat should I Search on Youtube ?',end='')
                speak('What should I Search on Youtube ?')
                cm = self.takeCommand().lower()
                kit.playonyt(cm) 

            elif "play songs on youtube" in self.query:
                speak('Sir, what would you like to listen ?')
                cm = self.takeCommand().lower()
                kit.playonyt(cm) 

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif 'open stack overflow' in self.query:
                webbrowser.open("stackoverflow.com")   

            elif "send message" in self.query or "send a message" in self.query or "send a message on whatsapp" in self.query  or "send message on whatsapp" in self.query:
                if "to" in self.query or "for" in self.query:
                    recipient = self.query.split("to", 1)[-1].split("for", 1)[-1].strip()
                    wp.message(to=recipient)
                else:
                    wp.message(to='')


            elif 'play music' in self.query:
                musiclist.playmusic()

            elif 'covid' in self.query:
                f.covid()

            elif 'cpu' in self.query:
                f.cpu()

            elif 'screenshot' in self.query:
                f.screenshot()

            elif 'password' in self.query:
                f.passwordgen()

            elif 'read' in self.query:
                f.text2speech()


            elif 'what is time' in self.query or 'current time'in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
  
            elif 'date' in self.query or 'what is date' in self.query or 'what is the date' in self.query:
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                date = datetime.datetime.now().day
                speak(f"the current date is: {date}date,{month}month,{year}year.")
                        

            elif 'open code' in self.query:
                codePath = r"C:\Users\vidhi\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(codePath)

            elif 'close vs code' in self.query or 'close vscode' in self.query:
                speak("Okk sir, cloasing  notepad")
                os.system('taskkill /f /im code.exe')

            elif 'open notepad' in self.query:
                codePath = "C:\\Windows\\System32\\notepad.exe" 
                os.startfile(codePath)

            elif 'close notepad' in self.query:
                speak("Okk sir, cloasing  notepad")
                os.system('taskkill /f /im notepad.exe')

            elif 'open command prompt' in self.query or 'cmd' in self.query:
                os.system("start cmd")

            elif 'ip address' in self.query:
                ip = get("https://api.ipify.org").text
                print(f"your ip address is {ip}")
                speak(f"your ip address is {ip}")

            elif 'email to' in self.query or 'send email' in self.query or 'send a email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand().lower()
                    speak("Please Wait Sir...")
                    em.sendEmail(content)
                    speak("Email has been sent!")
                except Exception as e:
                    # print(e)
                    speak("Sorry my sir  I am not able to send this email")  

            elif "set alarm" in self.query or "set an alarm" in self.query or "set the alarm" in self.query or "alarm" in self.query:
                speak("Sir now can excess the terminal to set alarm")
                alarm.alaramplay()
                speak("Okk sir, your alarm command completed now")

            elif 'set timer' in self.query or 'stopwatch' in self.query:
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


            elif "tell me joke" in self.query or "tell joke" in self.query or "tell me  a joke" in self.query or "tell a joke" in self.query:
                joke = pyjokes.get_joke()
                # (language='en', category='neutral')    category: str => Choices: 'neutral', 'chuck', 'all', 'twister'
                print(joke)
                speak(joke)
            
            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")  
                time.sleep(1)          
                pyautogui.press("tab")            
                pyautogui.keyUp("alt")            

            elif "tell me news" in self.query or "tell me somenews" in self.query or "news" in self.query :
                speak("please Wait sir, feteching the latest news.")
                news.news()

            elif 'hi' in self.query or 'hello' in self.query or "hey" in self.query or "who are you" in self.query or  "your intro" in self.query:
                f.aboutFunction()

            elif "bye" in self.query or "no thanks" in self.query or 'offline' in self.query:
                speak('thanks for using me sir, have a good day!')
                speak('Sorry but Can you click On EXIT to Stop me.')

            # Dangerorus commands 
            # elif "shutdown the system" in self.query:
            #     os.system("shutdown /s /t 5")
                
            # elif "restart the system" in self.query:
            #     os.system("shutdown /r /t 5")

            # elif "sleep the system" in self.query:
            #     os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

            # speak("\nsir, I'm Ready to Next Command ?")

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
