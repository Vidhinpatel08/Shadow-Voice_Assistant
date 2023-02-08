import csv
import time
import smtplib
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

def mailQuery(query):
    recipient_found = False
    while not recipient_found:
        if "to" in query or "for" in query:
            recipient = query.split("to", 1)[-1].split("for", 1)[-1].strip()
        else:
            speak("To whom should I send the email?")
            recipient = takeCommand().lower()
            print("Recipient:   ", recipient)
        
        if any(word in ["no", "cancel", "not", "don't",'doesn\'t'] for word in recipient.split()):
            speak("Ok, I will not send the email.")
            return
        else:
            recipient_email = ""
            with open(r'ShadowGui\features\secure\recipients.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row["Name"].lower() == recipient.lower() or row["Email"].lower() == recipient.lower():
                        recipient_email = row["Email"]
                        recipient_found = True
                        break
            if recipient_email == "":
                speak("Sorry, I couldn't find the recipient's email address. Please try again.")

    if recipient_found:
        try:
            speak("What is you subject of mail")
            subject = takeCommand().lower()
            print('Subject: ',subject)
            speak("What should I say?")
            content = takeCommand().lower()
            print('Content: ',content)
            message = f"Subject: {subject}\n\n      {content}"
            print(f'\nEmail Message:\nSubject: {subject}\nContent: {content}')
            speak("Please, read the displayed email, sir.")
            while True:
                speak("Are you sure you want to send this email? yes or no")
                confirmation = takeCommand().lower()
                if any(word in ["yes", "haa", "sure", "definitely"] for word in confirmation.split()):
                    print('Sending....')
                    speak('Wait a second')
                    result = sendEmail(recipient_email, message)
                    speak("Email has been sent!") if result else speak("Sorry sir, I am not able to send this email.")
                    break
                elif any(word in ["no", "error", "missing", "cancel", "not", "don't",'doesn\'t'] for word in confirmation.split()):
                    speak("What is the new subject of the email?")
                    subject = takeCommand().lower()
                    print('Subject: ',subject)
                    speak("What should I say in the new content?")
                    content = takeCommand().lower()
                    print('Content: ',content)
                    message = f"Subject: {subject}\n\n      {content}"
                    print(f'\nEmail Message:\nSubject: {subject}\nContent: {content}')
                elif any(word in ["wait", "minute", "second", "sometime"] for word in confirmation.split()):
                    speak('Sure,take your Time')
                    time.sleep(5)
                    continue
                else:
                    speak("I am waiting for your response.")
        except Exception as e:
            speak("Sorry sir, I am not able to send this email")  

def sendEmail(recipient_email, message): 
    try:
        with open(r'ShadowGui\features\secure\email.txt') as f :
            user_email=f.readline()
            password=f.readline()
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user_email, password)
        server.sendmail(user_email, recipient_email, message)
        server.close()
        return True

    except Exception as e:
        print(e)
        return False

if __name__ =='__main__':
    mailQuery('send email to jeet')


