import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit as kit # pip install pywhatkit 
import pyjokes  # pip install pyjokes 
from requests import get
import sys
import emailmodule as em
import musiclist

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

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    # wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Done 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # Done 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Sir, what should i search in Google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif "send message" in query:
            # kit.sendwhatsmsg("your number","your message",time in hour,time in min) 
            # give time 2 min before from current time 
            current_hour = int(datetime.datetime.now().strftime("%H"))
            current_minute = int(datetime.datetime.now().strftime("%M")) +1

            kit.sendwhatmsg("+91 6353428687","Jarvis send a message",current_hour,current_minute)


        elif "play songs on youtube" in query:
            speak('Sir, what would you like to listen ?')
            cm = takeCommand().lower()
            kit.playonyt(cm) 

        elif 'play music' in query:
            musiclist.playmusic()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\vidhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            #   vscode path
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\System32\\notepad.exe" 
            #   Notepad path
            os.startfile(codePath)

        elif 'close notepad' in query:
            speak("Okk sir, cloasing  notepad")
            os.system('taskkill /f /im notepad.exe')

        elif 'open command prompt' in query:
            # print("Enterd")
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            print(f"your ip address is {ip}")
            speak(f"your ip address is {ip}")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "vidhin1208@gmail.com"   # To mail id 
                em.sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")  
        
        elif "bye" in query:
            speak('thanks for using me sir, have a good day!')
            sys.exit()
        
        elif "tell me joke" in query :
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        # elif "shutdown the system" in query:
        #     os.system("shutdown /s /t 5")
            
        # elif "restart the system" in query:
        #     os.system("shutdown /r /t 5")

        # elif "sleep the system" in query:
        #     os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

        speak("\nsir, do you have any other work ?")


