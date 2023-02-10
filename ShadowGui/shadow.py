import os
import sys
import time
import datetime
import webbrowser
import pyjokes 
import pyautogui 
import wikipedia #pip install wikipedia
import pywhatkit as kit # pip install pywhatkit 
import features.emailmodule as em
import features.whatsapp as wp
import features.mynewsapi as news
import features.musiclist as musiclist
import features.feature as f
# import features.chatWith as chat
import features.alarmtime as alarm
from requests import get
from shadowUi import Ui_ShadowUI
import features.TTS as TTS

from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate, Qt 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainThread(QThread):
    def __init__(self):
        super (MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        os.system('cls')
        TTS.speak_Print('Sir please say "wake up" to continue')
        while True:
            permission = TTS.takeCommand()
            if 'wake up' in permission or 'are you there' in permission or 'hello' in permission :
                print()
                f.wishMe()
                while True:
                    query = TTS.takeCommand()
                    if "how are you" in query:
                        f.command_whatsup()

                    elif "fine" in query:
                        TTS.speak_Print("Glad to hear that sir!!")

                    elif "m good" in query:
                        TTS.speak_Print("Glad to hear that sir!!")

                    elif 'wikipedia' in query:
                        TTS.speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        TTS.speak("According to Wikipedia")
                        TTS.speak_Print(results)

                    elif 'open google' in query:
                        TTS.speak_Print('Sir, what should i search in Google')
                        cm = TTS.takeCommand()
                        webbrowser.open(f"{cm}")

                    if 'search on google' in query or 'search it' in query or 'google' in query:
                        TTS.speak('Searching on google...')
                        query = query.replace('search on google', "").replace('search it','').replace('google ','')
                        webbrowser.open(f"https://www.google.com/search?q={query}")

                    elif 'open youtube' in query:
                        TTS.speak_Print('What should I Search on Youtube ?')
                        cm = TTS.takeCommand().lower()
                        kit.playonyt(cm) 

                    elif "play songs on youtube" in query:
                        TTS.speak_Print('Sir, what would you like to listen ?')
                        cm = TTS.takeCommand().lower()
                        kit.playonyt(cm) 

                    elif "open facebook" in query:
                        webbrowser.open("www.facebook.com")

                    elif 'open stack overflow' in query:
                        webbrowser.open("stackoverflow.com")   

                    elif "send message" in query or "send a message" in query or "whatsapp message" in query or "send a message on whatsapp" in query  or "send message on whatsapp" in query or "send whatsapp message" in query:
                        wp.message(query)

                    elif 'play music' in query or 'music of' in query or "play " in query:
                        musiclist.playmusic(query)

                    elif 'stop music' in query or 'top music' in query or 'close music' in query or "pause" in query:
                        musiclist.stopMusic()

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
                            recipient = query.split("current temperature in")[-1].strip().replace("weather","").replace("temperature",'').replace("temperature",'')
                            f.temperature(at=recipient)
                        else:
                            f.temperature()

                    elif 'temperature' in query or "weather" in query:
                        if "in" in query or "at" in query:
                            recipient = query.split("in")[-1].strip().replace("weather","").replace("temperature",'').replace("temperature",'')
                            f.temperature(at=recipient)
                        else: 
                            f.temperature()

                    elif 'internet speed' in query or 'internetspeed' in query :
                            f.internetspeed()

                    elif "add reminder" in query or "adding reminder" in query or "add a note" in query or "add note" in query or "adding a note" in query:
                        if 'reminder' in query:
                            TTS.speak_Print("What should I adding in reminder")
                        else :
                            TTS.speak_Print("What should I add note")
                        f.appendnote()
                        
                    elif "remember that" in query or "write a note" in query or "write note" in query or "right note" in query or "right a note" in query or "new note" in query:
                        if 'remember' in query:
                            TTS.speak_Print("What should I remember")
                        else :
                            TTS.speak_Print("What should I write")
                        f.writenote()
                        
                    elif "do you remember anything" in query or "show a note" in query or "show note" in query:
                        if 'remember' in query:
                            TTS.speak_Print("You told me to remember that")
                        else :
                            TTS.speak_Print("showing our Note")
                        f.shownote()

                    elif 'what is time' in query or 'current time'in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        TTS.speak_Print(f"Sir, the time is {strTime}")
        
                    elif "instagram profile" in query or "profile on instagram" in query:
                        f.InstaDownload()
                    
                    elif 'current date' in query or 'what is date' in query or 'what is the date' in query:
                        year = datetime.datetime.now().year
                        month = datetime.datetime.now().month
                        date = datetime.datetime.now().day
                        TTS.speak_Print(f"the current date is: {date}date,{month}month,{year}year.")
                                
                    elif 'open code' in query:
                        codePath = r"C:\Users\vidhi\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                        os.startfile(codePath)

                    elif 'close vs code' in query or 'close vscode' in query:
                        TTS.speak_Print("Okk sir, cloasing  notepad")
                        os.system('taskkill /f /im code.exe')

                    elif 'open notepad' in query:
                        codePath = "C:\\Windows\\System32\\notepad.exe" 
                        os.startfile(codePath)

                    elif 'close notepad' in query:
                        TTS.speak_Print("Okk sir, cloasing  notepad")
                        os.system('taskkill /f /im notepad.exe')

                    elif 'open command prompt' in query or 'cmd' in query:
                        os.system("start cmd")

                    elif 'read my pdf' in query or 'this pdf' in query or 'read pdf' in query:
                        f.pdf_reader()

                    elif 'ip address' in query:
                        ip = get("https://api.ipify.org").text
                        TTS.speak_Print(f"your ip address is {ip}")
    
                    elif "where i am" in query or "where we are" in query or "my location" in query: 
                        f.Mylocation()

                    elif 'email to' in query or 'mail to' in query or 'send a mail' in query or 'send a email' in query or 'send email' in query or 'send  mail' in query :
                        em.mailQuery(query)

                    elif "set alarm" in query or "set an alarm" in query or "set the alarm" in query or "alarm" in query:
                        TTS.speak("Sir now can excess the terminal to set alarm")
                        alarm.alaramplay()
                        TTS.speak_Print("Okk sir, your alarm command completed now")

                    elif 'set timer' in query or 'stopwatch' in query:
                        TTS.speak_Print("For how many minutes?")
                        timing = TTS.takeCommand()
                        if timing != None or timing != 'none':
                            timing =timing.replace('minutes', '')
                            timing = timing.replace('minute', '')
                            timing = timing.replace('for', '')
                            timing = float(timing)
                            timing = timing * 60
                            TTS.speak_Print(f'I will remind you in {timing} seconds')
                            time.sleep(timing)
                            TTS.speak_Print('Your time has been finished sir')

                    elif "tell me joke" in query or "tell joke" in query or "tell me  a joke" in query or "tell a joke" in query:
                        joke = pyjokes.get_joke()
                        # (language='en', category='neutral')    category: str => Choices: 'neutral', 'chuck', 'all', 'twister'
                        TTS.speak_Print(joke)
                    
                    elif 'switch the window' in query:
                        pyautogui.keyDown("alt")  
                        time.sleep(1)          
                        pyautogui.press("tab")            
                        pyautogui.keyUp("alt")            
                        
                    elif "do some calculation" in query or "can you calculate" in query or "calculate the" in query:
                       f.calculate()
                    
                    elif "tell me news" in query or "tell me somenews" in query or "read news" in query or "play news" in query or "news of" in query or "news" in query :
                        news.play_news(query)

                    elif 'hi' in query or 'hello' in query or "hey" in query or "who are you" in query or  "your intro" in query:
                        f.aboutFunction()

                    elif "sleep shadow" in query or "sleep now" in query or 'you can sleep' in query or "nothing" in query or "abort" in query or "stop" in query:
                        TTS.speak_Print('okay sir, I am going to sleep you can call me anytime. ')
                        break

                    elif 'thanks' in query or 'thank you' in query :
                        TTS.speak("It's my pleasure sir")

                    elif "goodbye" in query or "good bye" in query  or "bye" in query  or "quit" in query :
                        TTS.speak_Print('Thanks for using me sir, have a good day')
                        TTS.speak('Sorry but Can you click on EXIT to Stop me.')
                        quit()
                    
                    # elif 'None' == query:
                    #     continue
                    
                    # else :
                    #     chat.chat_with_AI(query)

            elif "goodbye" in permission or "good bye" in permission  or "bye" in permission or "nothing" in permission or "abort" in permission or "stop" in permission or "quit" in permission:
                TTS.speak_Print('Thanks for useing me sir, have a good day')
                TTS.speak('Sorry but Can you click on EXIT to Stop me.')
                sys.exit()

startExecution = MainThread()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ShadowUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)        
        self.ui.pushButton_2.clicked.connect(self.close)  

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


