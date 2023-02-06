import speech_recognition as sr #pip install speechRecognition
import datetime
import pywhatkit as kit # pip install pywhatkit 
import csv


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
            print("Recognizing...")
            query = r.recognize_google(audio,language= 'en-in')
            print(f'User Said : {query}')

        except Exception as e :
            print('Say that again Please...')
            return 'None'
        
        return query.lower().strip()



def message(to):
    myContact = {}
    with open(r'ShadowGui\features\myContact.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            myContact[row[0]] = row[1]

    try:
        print(myContact)
        while True:
            if to == '':
                print('Who Should I Send a Message to?')
                speak('Who Should I Send a Message to?')
                person = takeCommand()
            else: 
                person = to
            if person in myContact.keys()  :
                sendNumber = myContact[person]
                print('What do you want to send ?')
                speak('What do you want to send ?')
                sendMessage = takeCommand()
                sending(sendNumber, sendMessage) 
                break
            elif person.lower() == "no":
                break
            else:
                print(f'{person} is not Found in Contact List')
                speak(f'{person} is not Found in Contact List')
    except Exception as e:
        print(e)  

def sending(sendNumber, sendMessage)  :
    try:
        send_time = datetime.datetime.now() + datetime.timedelta(minutes=1, seconds=15) # send message 1 minute later
        send_hour, send_minute = send_time.hour,send_time.minute
        speak("Wait for some time  I'll send a message")
        kit.sendwhatmsg(sendNumber, sendMessage, send_hour, send_minute)
    except Exception as e :
        print(e)
        speak("Sorry sir Time Mismatching...")

if __name__ =='__main__':
    message()


               