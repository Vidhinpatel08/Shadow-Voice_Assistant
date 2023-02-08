import csv
import time
import smtplib
import speech_recognition as sr #pip install speechRecognition

import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

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
    filesendToMail = False

    if "send file" in query or "attach" in query or "with " in query:
        filesendToMail = True

    while not recipient_found:
        if "to" in query or "for" in query:
            recipient = query.split("to", 1)[-1].split("for", 1)[-1].strip()
            recipient = recipient.split("with")[0].split("and")[0].split("attach")[0].split("file")[0].strip()
        else:
            speak("To whom should I send the email?")
            recipient = takeCommand().lower()
            recipient = recipient.split("to", 1)[-1].split("for", 1)[-1].strip()
            if "send file" in recipient or "attach" in recipient or "with" in recipient or "file" in recipient:
                filesendToMail = True
                recipient = recipient.split("with", 1)[-1].split("and", 1)[-1].split("attach", 1)[-1].split("send file", 1)[-1].strip()
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
                    if filesendToMail:
                        print("sir please enter path of file")
                        speak("sir please enter path of file")
                        filePath = input("path of file : ").replace('%20',' ').replace('"','').replace("'",'')
                        print('Sending....')
                        speak('Wait a second')
                        result = sendEmailWithAttachment(recipient_email, message, filePath)
                        speak("Email has been sent!") if result else speak("Sorry sir, I am not able to send this email.")
                        break
                    else:
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
            print('error',e)
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

def sendEmailWithAttachment(recipient_email, message, file_path):
    try:
        with open(r'ShadowGui\features\secure\email.txt') as f :
            user_email=f.readline()
            password=f.readline()

        msg = MIMEMultipart()
        msg['From'] = user_email
        msg['To'] = recipient_email
        msg['Subject'] = message.split('\n\n      ')[0]

        msg.attach(MIMEText(message.split('\n\n      ')[1], 'plain'))

        filename = file_path.split("/")[-1]
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        msg.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(user_email, password)
            server.sendmail(user_email, recipient_email, msg.as_string())
        return True
    except Exception as e:
        print(e)
        return False

if __name__ =='__main__':
    mailQuery('send email to jeet ')

