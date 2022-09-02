from socket import timeout
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
import features.emailmodule as em
import features.mynewsapi as news
import features.musiclist as musiclist
import pyautogui # pip install pyautogui
import features.feature as f
import features.alarmtime as alarm

from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from shadowUi import Ui_ShadowUI


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am shadow Sir. Please tell me how may I help you")       


class MainThread(QThread):
    def __init__(self):
        super (MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening...")
            r.pause_threshold = 2
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        query=query.lower()
        return query


    def TaskExecution(self):
        wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand()
            # Done 
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            # Done 
            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif 'open google' in self.query:
                speak('Sir, what should i search in Google')
                cm = self.takeCommand()
                webbrowser.open(f"{cm}")

            elif 'open stack overflow' in self.query:
                webbrowser.open("stackoverflow.com")   

            elif "send message" in self.query:
                # kit.sendwhatsmsg("your number","your message",time in hour,time in min) 
                # give time 2 min before from current time 
                current_hour = int(datetime.datetime.now().strftime("%H"))
                current_minute = int(datetime.datetime.now().strftime("%M")) +1

                kit.sendwhatmsg("+91 63xxxxxxxx","Shadow send a message",current_hour,current_minute)


            elif "play songs on youtube" in self.query:
                speak('Sir, what would you like to listen ?')
                cm = self.takeCommand().lower()
                kit.playonyt(cm) 

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

            elif 'open' in self.query:
                os.system('explorer c://{}'.format(self.query.replace('open','')))

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())

            elif 'what is time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
  
            elif 'date' in self.query:
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                date = datetime.datetime.now().day
                speak(f"the current date is: {date}date,{month}month,{year}year.")
                        

            elif 'open code' in self.query:
                codePath = "C:\\Users\\vidhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
                #   vscode path
                os.startfile(codePath)

            elif 'close vs code' in self.query or 'close vscode' in self.query:
                speak("Okk sir, cloasing  notepad")
                os.system('taskkill /f /im code.exe')

            elif 'open notepad' in self.query:
                codePath = "C:\\Windows\\System32\\notepad.exe" 
                #   Notepad path
                os.startfile(codePath)

            elif 'close notepad' in self.query:
                speak("Okk sir, cloasing  notepad")
                os.system('taskkill /f /im notepad.exe')

            elif 'open command prompt' in self.query:
                # print("Enterd")
                os.system("start cmd")

            elif 'ip address' in self.query:
                ip = get("https://api.ipify.org").text
                print(f"your ip address is {ip}")
                speak(f"your ip address is {ip}")

            elif 'email' in self.query:
                try:
                    speak('what is your subject ?')
                    subject = self.takeCommand().lower()
                    time.sleep(1)
                    speak("What should I say?")
                    content = self.takeCommand().lower()
                    speak("Please Wait Sir...")
                    em.sendEmail(subject,content)
                    speak("Email has been sent!")
                except Exception as e:
                    # print(e)
                    speak("Sorry my sir  I am not able to send this email")  


            #############################################################
            #to set an alarm
            elif "set alarm" in self.query or "set an alarm" in self.query or "set the alarm" in self.query or "alarm" in self.query:
                speak("Sir now can excess the terminal to set alarm")
                alarm.alaramplay()
                speak("Okk sir, your alarm command completed now")

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takeCommand()
                timing =timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')

            elif 'hi' in self.query or 'hello' in self.query:
                speak('Hello sir, how may I help you?')

            elif "tell me joke" in self.query :
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
            
            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")  
                time.sleep(1)          
                pyautogui.press("tab")            
                pyautogui.keyUp("alt")            

            elif "tell me news" in self.query or "tell me some news" in self.query or "news" in self.query :
                speak("please Wait sir, feteching the latest news.")
                news.news()

            elif "who are you" in self.query or  "your intro" in self.query:
                speak("I am shadow Sir. I'm Voice Assistent of Vidhin")       

            # elif "bye" in self.query or "no thanks" in self.query or 'offline' in self.query:
            #     speak('thanks for using me sir, have a good day!')
            #     sys.exit()
            
            # Dangerorus commands 
            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")
                
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

            speak("\nsir, I'm Ready to Next Command ?")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShadowUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)        
        self.ui.pushButton_2.clicked.connect(self.close)  

    def starttask(self):
        self.ui.movie = QtGui.QMovie("../images/Main.gif")      # path of main bg_image (Labal-1)
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../images/Initial.gif")      # path of (Labal-2)
        self.ui.label_2.setMovie(self.ui.movie)
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




app = QApplication(sys.argv)
shadow = Main()
shadow.show()
exit(app.exec_())