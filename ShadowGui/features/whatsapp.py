import speech_recognition as sr #pip install speechRecognition
import datetime
import pywhatkit as kit # pip install pywhatkit 
import csv
import pyautogui 
import time
import features.TTS as TTS


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
            TTS.speak_Print("\nWho should I send a message to?")
            recipient = TTS.takeCommand_template().lower()
            if "to" in recipient or "for" in recipient:
                recipient = recipient.split("to", 1)[-1].split("for", 1)[-1].strip()
            print("Recipient:   ", recipient)


        if recipient in myContact.keys():
            recipient_found = True
        elif any(word in ["no", "cancel", "not", "don't", 'doesn\'t'] for word in recipient.split()):
            TTS.speak_Print("Ok, I will not send the message.")
            return
        else:
            TTS.speak_Print(f"{recipient} is not found in Contact List")
    
    if recipient_found:
        try:
            TTS.speak_Print("\nWhat do you want to send?")
            sendMessage =TTS.takeCommand_template().lower()
            print(f"\nWhatsapp Message:   {sendMessage}\n")
            TTS.speak_Print("Please, read the displayed message, Is this correct?")
            while True:
                TTS.speak_Print("Are you sure you want to send this Mesage? yes or no\n")
                confirmation =TTS.takeCommand_template().lower()
                if any(word in ["yes", "haa", "sure", "definitely"] for word in confirmation.split()):
                    print('Sending....')
                    TTS.speak('give me sometime...')
                    result = sending(myContact[recipient], f"{sendMessage}\n~ Send by Shadow")
                    TTS.speak_Print("Message has been sent!") if result else TTS.speak_Print("Sorry sir, I am not able to send this Message.")
                    break
                elif any(word in ["no", "error", "missing", "cancel", "not", "don't",'doesn\'t'] for word in confirmation.split()):
                    TTS.speak_Print("What do you want to send?")
                    sendMessage =TTS.takeCommand_template().lower()
                    print(f'\nWhatsapp Message:   {sendMessage}\n')
                elif any(word in ["wait", "minute", "second", "sometime"] for word in confirmation.split()):
                    TTS.speak('Sure,take your Time')
                    time.sleep(5)
                    continue
                else:
                    TTS.speak("I am waiting for your response.")
 
        except Exception as e:
            TTS.speak_Print("Sorry sir, I am not able to send this Whatsapp Message")  

def sending(sendNumber, sendMessage)  :
    try:
        send_time = datetime.datetime.now() + datetime.timedelta(minutes=1, seconds=15) # send message 1 minute later
        send_hour, send_minute = send_time.hour,send_time.minute
        kit.sendwhatmsg(sendNumber, sendMessage, send_hour, send_minute)       
        time.sleep(3)          
        pyautogui.keyDown("alt")  
        time.sleep(1)          
        pyautogui.press("tab")            
        pyautogui.keyUp("alt")
        return True
    except Exception as e :
        print(e)
        TTS.speak("Sorry sir Time Mismatching...")
        return False

if __name__ =='__main__':
    message('send whatsapp message')
