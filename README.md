# Voice_Assistent
> Installation & Step by Step Process

This is an amazing virtual assistant program. which can perform some very interesting pre-defined tasks. it can perform online as well as system based tasks. Here addition functionality is Face Authentication by use of Face Recognition

# Installing / Getting started
### Setting up Dev

Here's a brief intro about what a developer must do in order to start developing
the project further:
<!-- 
```shell
gh repo clone Vidhinpatel08/Voice_assistent
cd voice_assistent/

``` -->

Step 1: Download Zip File Of Project.

Step 2: Extract Zip File At your Drive.

Step 3 : open Shadow-voice_assitent Folder.

Step 4 : goto ShadowGui Folder and Open wih your IDE.

Step 5 : oprn yor terminal and type the Command.
```
pip install -r ./requirement.txt
```
now, after Successfully Download all Modules. Go for next step

Step 6 : goto facerecognition folder & open Sample_genrator.py
**Note: Allow to Excess your Camera Permition**
- Run this file
- enter your ID number in Integer Number in terminal.
- your Camera capture your picture and store in Samples folder.
- goto Sample folder and see some *face."yourid".1.jpg* Images created.
- Completed your 1st Step.

Step 7 : goto facerecognition folder & open Modle_trainer.py
- Run this file.
- goto trainer folder
- see your trainer.yml file created.

Step 8 : open Shadow.py

step 9 : Changes in Someline of code.
Now, you need to change some line as per your Shadow.py :

##### Speech Voices Changes 
```
voices = engine.getProperty('voices')
# print(voices[0].id) # for male voice
# print(voices[1].id) # for female voice
engine.setProperty('voice', voices[0].id)
```
##### Whatsapp Message Send
**Note: Need to login in web whatsapp in your Browser**
```
elif "send message" in self.query:
                # kit.sendwhatsmsg("your number","your message",time in hour,time in min) 
                current_hour = int(datetime.datetime.now().strftime("%H"))
                current_minute = int(datetime.datetime.now().strftime("%M")) +1

                kit.sendwhatmsg("+91 63xxxxxxxx","Shadow send a message",current_hour,current_minute)

```
you can change you Friend Number and Message.

##### VScode Location Changes 
```
elif 'open code' in self.query:
                codePath = "C:\\Users\\vidhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
                #   vscode path
                os.startfile(codePath)
```

##### Notepad Location Changes 
```
elif 'open notepad' in self.query:
    codePath = "C:\\Windows\\System32\\notepad.exe" 
    #   Notepad path
    os.startfile(codePath)
```

Now, you need to change some line as per your features folder :
###### open feature.py
```
def screenshot():
    name_img = tt.time()
    name_img = f'D:\\screenshots\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()
```
set your screenshots Save Location

###### open musiclist.py
```
def playmusic():
    music_dir = 'D:\\Audio' # music directry path 
```
set your music DirectoryLocation

***Note: you can change you code as per your Requirement.***

Step 10 : Run And Testing
- open shadow.py
- run file  

