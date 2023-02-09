import pyttsx3
import speech_recognition as sr #pip install speechRecognition


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    """Take String as input and say on audio with help of speakers.."""
    engine.say(audio)
    engine.runAndWait()

def speak_Print(audio):
    """Take String as input and say on audio with help of speakers.."""
    print(audio)
    engine.say(audio)
    engine.runAndWait()

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
    
    engine.runAndWait()
    return query.lower().strip()

def takeCommand_template():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2 # time of stop between your speech to exection 
        r.energy_threshold = 200  # increment if backgroud voice high.. & decrement if voice not peroper listening.. 
        audio = r.listen(source)

    try :
        query = r.recognize_google(audio,language= 'en-in')

    except Exception as e :
        return 'None'
    
    engine.runAndWait()
    return query.lower().strip()