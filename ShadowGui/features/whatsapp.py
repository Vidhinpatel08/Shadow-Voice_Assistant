import speech_recognition as sr #pip install speechRecognition
import datetime
import pywhatkit as kit # pip install pywhatkit 
import csv
import pyautogui 
import time


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

    
myContact = {}
with open(r'ShadowGui\features\secure\myContact.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        myContact[row[0]] = row[1]

def message(query):
    recipient_found = False
    while not recipient_found:
        if "to" in query or "for" in query:
            recipient = query.split("to", 1)[-1].split("for", 1)[-1].strip()
        else:
            print("Who should I send a message to?")
            speak("Who should I send a message to?")
            recipient = takeCommand().lower()
            print("Recipient:   ", recipient)


        if recipient in myContact.keys():
            recipient_found = True
        elif any(word in ["no", "cancel", "not", "don't", 'doesn\'t'] for word in recipient.split()):
            speak("Ok, I will not send the message.")
            return
        else:
            print(f"{recipient} is not found in Contact List")
            speak(f"{recipient} is not found in Contact List")
    
    if recipient_found:
        try:
            print("What do you want to send?")
            speak("What do you want to send?")
            sendMessage = takeCommand().lower()
            print(f"\nWhatsapp Message:   {sendMessage}")
            print("Please, read the displayed message, Is this correct?")
            speak("Please, read the displayed message, Is this correct?")
            while True:
                speak("Are you sure you want to send this Mesage? yes or no")
                confirmation = takeCommand().lower()
                if any(word in ["yes", "haa", "sure", "definitely"] for word in confirmation.split()):
                    print('Sending....')
                    speak('Wait a second')
                    result = sending(myContact[recipient], sendMessage)
                    speak("Message has been sent!") if result else speak("Sorry sir, I am not able to send this Message.")
                    break
                elif any(word in ["no", "error", "missing", "cancel", "not", "don't",'doesn\'t'] for word in confirmation.split()):
                    speak("What do you want to send?")
                    sendMessage = takeCommand().lower()
                    print(f'\nWhatsapp Message:   {sendMessage}')
                elif any(word in ["wait", "minute", "second", "sometime"] for word in confirmation.split()):
                    speak('Sure,take your Time')
                    time.sleep(5)
                    continue
                else:
                    speak("I am waiting for your response.")
 
        except Exception as e:
            speak("Sorry sir, I am not able to send this Whatsapp Message")  

def sending(sendNumber, sendMessage)  :
    try:
        send_time = datetime.datetime.now() + datetime.timedelta(minutes=1, seconds=15) # send message 1 minute later
        send_hour, send_minute = send_time.hour,send_time.minute
        kit.sendwhatmsg(sendNumber, sendMessage, send_hour, send_minute)       
        pyautogui.keyDown("alt")  
        time.sleep(1)          
        pyautogui.press("tab")            
        pyautogui.keyUp("alt")
        return True
    except Exception as e :
        print(e)
        speak("Sorry sir Time Mismatching...")
        return False

if __name__ =='__main__':
    message('send whatsapp message')


               