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
import features.chatWith as chat
import features.alarmtime as alarm
from requests import get
from shadowUi import Ui_ShadowUI
import features.TTS as TTS

from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate, Qt 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Commands Lists

permission_phrases = ["wake up", "are you there", "hello", "hey assistant", "hey there", "open up", "are you here", "hi"]
how_are_you_phrases = ["how are you", "fine", "m good", "how's it going", "how you doing", "how r u", "hows you"]
wikipedia_phrases = ["wikipedia", "look up on wikipedia", "search in wikipedia", "what is", "tell me about", "wikipidia", "wikipedea", "wiki pedia"]
google_phrases = ["open google", "search on google", "search it", "google", "look up on google", "google search", "goggle", "googal"]
youtube_phrases = ["open youtube", "play songs on youtube", "youtube", "search on youtube", "youtube search", "you tube", "utube"]
facebook_phrases = ["open facebook", "facebook", "visit my facebook", "check facebook", "face book", "fecebook", "facebok"]
stackoverflow_phrases = ["open stack overflow", "stackoverflow", "look up on stack overflow", "check stack overflow", "stack overflow", "stackoverflow.com"]
whatsapp_phrases = ["send message", "send a message", "whatsapp message", "send a message on whatsapp", "send message on whatsapp", "send whatsapp message", "send text", "send a text", "text on whatsapp", "whats app", "what's up", "watsapp", "whatsap"]
music_phrases = ["play music", "music of", "play ", "listen to music", "song", "music player", "music playlist", "play song", "music", "musics", "play musics"]
stop_music_phrases = ["stop music", "top music", "close music", "pause", "pause music", "stop song", "shut off music", "stopp music", "paus music"]
cpu_phrases = ["cpu", "processor", "central processing unit", "computer performance", "central processor unit", "CPU"]
battery_phrases = ["how much power left", "how much power we have", "battery", "battery status", "battery level", "how much charge left", "battery remaining", "battry", "battray"]
screenshot_phrases = ["screenshot", "capture screen", "take a screenshot", "snapshot", "grab screen", "screen shot", "screnshot", "screeshot"]
password_phrases = ["create password", "generate password", "password manager", "password generator", "password security", "generate passward", "password creation"]
clipboard_phrases = ["read clipboard", "clipboard", "copy and paste", "clipboard manager", "clip board", "clipbord"]
temperature_phrases = ["current temperature", "temperature", "weather", "climate", "weather forecast", "tempature", "wheather"]
internet_speed_phrases = ["internet speed", "internetspeed", "network speed", "internet connection", "bandwidth", "net speed", "internet velocity"]
reminder_phrases = ["add reminder", "adding reminder", "add a note", "add note", "adding a note", "set reminder", "remind me", "remember this", "set a reminder", "remember to", "remind me to"]
remember_phrases = ["remember that", "write a note", "write note", "right note", "right a note", "new note", "memorize", "store this", "remeber that", "wright note", "memorise"]
show_note_phrases = ["do you remember anything", "show a note", "show note", "recall note", "retrieve note", "view note", "display note", "sho note"]
time_phrases = ["what is time", "current time", "time", "time now", "time of day", "clock", "whats the time", "current time please"]
instagram_phrases = ["instagram profile", "profile on instagram", "instagram", "check instagram", "instagram account", "insta", "instagrm", "insta gram"]
date_phrases = ["current date", "what is date", "what is the date", "today's date", "date today", "date", "todays date", "whats the date"]
code_phrases = ["open code", "close vs code", "close vscode", "open notepad", "close notepad", "open command prompt", "cmd", "open editor", "start coding", "open coding"]
pdf_phrases = ["read my pdf", "this pdf", "read pdf", "pdf reader", "open pdf", "pdf file", "pdf", "open pdf file"]
ip_phrases = ["ip address", "what is my ip", "find ip", "get ip", "my ip", "ip adress", "whats my ip", "whats my ip adress"]
location_phrases = ["where i am", "where we are", "my location", "locate me", "current location", "find me", "wheres my location"]
email_phrases = ["email to", "mail to", "send a mail", "send a email", "send email", "send mail", "compose email", "write email", "email", "e-mail", "emails"]
alarm_phrases = ["set alarm", "set an alarm", "set the alarm", "alarm", "wake up call", "alarm clock", "set an alaram", "alaram"]
timer_phrases = ["set timer", "stopwatch", "countdown", "timer", "timing", "stopwatch app", "stop watch", "timeer"]
joke_phrases = ["tell me joke", "tell joke", "tell me a joke", "tell a joke", "joke", "funny joke", "humor", "joks"]
switch_window_phrases = ["switch the window", "change window", "window switcher", "toggle window", "alt tab", "switch windows", "swich window"]
calculation_phrases = ["do some calculation", "can you calculate", "calculate the", "math", "calculate this", "math problem", "calculations", "calculator", "calculate"]
news_phrases = ["tell me news", "tell me some news", "read news", "play news", "news of", "news", "latest news", "news update", "whats the news", "news please", "get news"]
greeting_phrases = ["hi", "hello", "hey", "who are you", "your intro", "greetings", "nice to meet you", "halo", "heya"]
sleep_phrases = ["sleep shadow", "sleep now", "you can sleep", "nothing", "abort", "stop", "quit", "shut down", "turn off", "go to sleep", "sleepy", "got sleep", "gotosleep"]
thanks_phrases = ["thanks", "thank you", "thank you so much", "thanks a lot", "appreciate it", "thank", "thnx", "thnk you"]
goodbye_phrases = ["goodbye", "good bye", "bye", "quit", "see you later", "farewell", "good by", "bye bye", "byee"]

# Combine all command phrases into a single list
all_phrases = [permission_phrases, how_are_you_phrases, wikipedia_phrases, google_phrases, youtube_phrases,
               facebook_phrases, stackoverflow_phrases, whatsapp_phrases, music_phrases, stop_music_phrases,
               cpu_phrases, battery_phrases, screenshot_phrases, password_phrases, clipboard_phrases,
               temperature_phrases, internet_speed_phrases, reminder_phrases, remember_phrases, show_note_phrases,
               time_phrases, instagram_phrases, date_phrases, code_phrases, pdf_phrases, ip_phrases,
               location_phrases, email_phrases, alarm_phrases, timer_phrases, joke_phrases, switch_window_phrases,
               calculation_phrases, news_phrases, greeting_phrases, sleep_phrases, thanks_phrases, goodbye_phrases]

# Flatten the list of lists
all_phrases_flat = [phrase for sublist in all_phrases for phrase in sublist]

class MainThread(QThread):
    def __init__(self):
        super (MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        os.system('cls')
        TTS.speak_Print('Sir please say "wake up" to continue')

        # If any command not work then check oldwhileloop.txt for reference because it's old version of this
        while True:
            # Main loop to handle commands
            permission = TTS.takeCommand()
            if any(phrase in permission for phrase in permission_phrases):
                print()
                f.wishMe()
                while True:
                    query = TTS.takeCommand().lower()
                    if any(phrase in query for phrase in all_phrases_flat):
                        if any(phrase in query for phrase in how_are_you_phrases):
                            f.command_whatsup()

                        elif any(phrase in query for phrase in wikipedia_phrases):
                            TTS.speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=2)
                            TTS.speak("According to Wikipedia")
                            TTS.speak_Print(results)

                        elif any(phrase in query for phrase in google_phrases):
                            TTS.speak('Searching on google...')
                            query = query.replace('search on google', "").replace('search it','').replace('google ','')
                            webbrowser.open(f"https://www.google.com/search?q={query}")

                        elif any(phrase in query for phrase in youtube_phrases):
                            TTS.speak_Print('What should I Search on Youtube ?')
                            cm = TTS.takeCommand().lower()
                            kit.playonyt(cm)

                        elif any(phrase in query for phrase in facebook_phrases):
                            webbrowser.open("www.facebook.com")

                        elif any(phrase in query for phrase in stackoverflow_phrases):
                            webbrowser.open("stackoverflow.com")

                        elif any(phrase in query for phrase in whatsapp_phrases):
                            wp.message(query)

                        elif any(phrase in query for phrase in music_phrases):
                            musiclist.playmusic(query)

                        elif any(phrase in query for phrase in stop_music_phrases):
                            musiclist.stopMusic()

                        elif any(phrase in query for phrase in cpu_phrases):
                            f.cpu()

                        elif any(phrase in query for phrase in battery_phrases):
                            f.batteryPer()

                        elif any(phrase in query for phrase in screenshot_phrases):
                            f.screenshot()

                        elif any(phrase in query for phrase in password_phrases):
                            f.passwordgen()

                        elif any(phrase in query for phrase in clipboard_phrases):
                            f.text2speech()

                        elif any(phrase in query for phrase in temperature_phrases):
                            if "in" in query or "at" in query:
                                recipient = query.split("current temperature in")[-1].strip().replace("weather","").replace("temperature",'').replace("temperature",'')
                                f.temperature(at=recipient)
                            else:
                                f.temperature()

                        elif any(phrase in query for phrase in internet_speed_phrases):
                            f.internetspeed()

                        elif any(phrase in query for phrase in reminder_phrases):
                            if 'reminder' in query:
                                TTS.speak_Print("What should I adding in reminder")
                            else :
                                TTS.speak_Print("What should I add note")
                            f.appendnote()

                        elif any(phrase in query for phrase in remember_phrases):
                            if 'remember' in query:
                                TTS.speak_Print("What should I remember")
                            else :
                                TTS.speak_Print("What should I write")
                            f.writenote()

                        elif any(phrase in query for phrase in show_note_phrases):
                            if 'remember' in query:
                                TTS.speak_Print("You told me to remember that")
                            else :
                                TTS.speak_Print("showing our Note")
                            f.shownote()

                        elif any(phrase in query for phrase in time_phrases):
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            TTS.speak_Print(f"Sir, the time is {strTime}")

                        elif any(phrase in query for phrase in instagram_phrases):
                            f.InstaDownload()

                        elif any(phrase in query for phrase in date_phrases):
                            year = datetime.datetime.now().year
                            month = datetime.datetime.now().month
                            date = datetime.datetime.now().day
                            TTS.speak_Print(f"the current date is: {date}date,{month}month,{year}year.")

                        elif any(phrase in query for phrase in code_phrases):
                            codePath = r"C:\Users\vidhi\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                            os.startfile(codePath)

                        elif any(phrase in query for phrase in pdf_phrases):
                            f.pdf_reader()

                        elif any(phrase in query for phrase in ip_phrases):
                            ip = get("https://api.ipify.org").text
                            TTS.speak_Print(f"your ip address is {ip}")

                        elif any(phrase in query for phrase in location_phrases):
                            f.Mylocation()

                        elif any(phrase in query for phrase in email_phrases):
                            em.mailQuery(query)

                        elif any(phrase in query for phrase in alarm_phrases):
                            TTS.speak("Sir now can excess the terminal to set alarm")
                            alarm.alaramplay()
                            TTS.speak_Print("Okk sir, your alarm command completed now")

                        elif any(phrase in query for phrase in timer_phrases):
                            TTS.speak_Print("For how many minutes?")
                            timing = TTS.takeCommand()
                            if timing != None or timing != 'none':
                                timing = timing.replace('minutes', '')
                                timing = timing.replace('minute', '')
                                timing = timing.replace('for', '')
                                timing = float(timing)
                                timing = timing * 60
                                TTS.speak_Print(f'I will remind you in {timing} seconds')
                                time.sleep(timing)
                                TTS.speak_Print('Your time has been finished sir')

                        elif any(phrase in query for phrase in joke_phrases):
                            joke = pyjokes.get_joke()
                            TTS.speak_Print(joke)

                        elif any(phrase in query for phrase in switch_window_phrases):
                            pyautogui.keyDown("alt")
                            time.sleep(1)
                            pyautogui.press("tab")
                            pyautogui.keyUp("alt")

                        elif any(phrase in query for phrase in calculation_phrases):
                            f.calculate()

                        elif any(phrase in query for phrase in news_phrases):
                            news.play_news(query)

                        elif any(phrase in query for phrase in greeting_phrases):
                            f.aboutFunction()

                        elif any(phrase in query for phrase in sleep_phrases):
                            TTS.speak_Print('okay sir, I am going to sleep you can call me anytime.')
                            break

                    # else:
                    #     chat.chat_with_AI(query)

            elif any(phrase in permission for phrase in goodbye_phrases):
                TTS.speak_Print('Thanks for using me sir, have a good day')
                TTS.speak('Sorry but Can you click on EXIT to Stop me.')
                sys.exit()

# If any command not work then check oldwhileloop.txt for reference because it's old version of this

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


