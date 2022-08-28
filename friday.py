import pyttsx3
engine = pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voices',voice[0].id)
print(voice)
engine.say("hello")
engine.runAndWait()