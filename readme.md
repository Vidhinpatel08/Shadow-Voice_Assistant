# Voice Assistance

## Overview

Voice Assistance is an advanced AI-powered system designed to provide voice-activated interaction and assistance to users. It enables users to perform various tasks and obtain information simply by speaking commands to the system.

## Features

- **Wake-Up Command**: Activate the assistant by speaking a wake-up phrase.
- **Greetings**: Greet the assistant with common phrases like "hello" or "hi".
- **Information Retrieval**: Obtain information by asking questions or issuing commands.
- **Wikipedia Search**: Search for information on Wikipedia using voice commands.
- **Web Search**: Perform web searches using Google or YouTube.
- **Social Media**: Interact with social media platforms like Facebook and Instagram.
- **Development Tools Integration**: Open code editors, command prompts, or other development tools.
- **Utility Functions**: Perform tasks like taking screenshots, managing passwords, and checking battery status.
- **Entertainment**: Play music, tell jokes, or read the latest news.
- **System Management**: Control system functions like shutting down or restarting the device.

## Usage

To use Voice Assistance, simply activate the system by speaking a wake-up phrase, then issue commands or ask questions using natural language. The system will respond accordingly and execute the requested actions.

## Installation

Voice Assistance can be installed on various devices, including computers, smartphones, and smart speakers. Installation instructions may vary depending on the platform.

### Setup Instructions

1. **Extract Folder**: 
   - Extract the "Shadow-Voice_Assistant.zip" folder to your desired location.

2. **Open in VS Code**:
   - Open Visual Studio Code (VS Code).
   - Set the root folder to "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant".

3. **Set Up Music Directory**:
   - Set the music directory to "D:\Audio\music_dir".
   - Create subfolders within "music_dir" based on different categories like "Bhajans", "Aartis", "Shlokas", "Ghazals", "Bollywood", "General".

4. **Email Configuration**:
   - Update your email ID and mail authentication key in "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\secure\email.txt".

5. **Contact List**:
   - Before starting the project, make sure you are logged into WhatsApp Web.
   - Update the contact list with names and mobile numbers (with country code) in "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\secure\myContact.csv".

6. **Recipients List**:
   - Update the recipients list with names and email IDs in "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\secure\recipients.csv".

7. **Email Module Setting**:
   - In "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\emailmodule.py", set the server as:
     ```python
     server = smtplib.SMTP('smtp.mailosaur.net', 587)  # If you're using a testing ID
     ```

8. **News API Key**:
   - Set the News API key in "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\secure\NewsAPI.txt" (provided).

9. **Alarm Configuration**:
   - Set up the alarm sound file path in "D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\alarmtime.py":
     ```python
     os.startfile(r"D:\Files\Shadow-Voice_Assistant\Shadow-Voice_Assistant\ShadowGui\features\AI_alarm05.mp3")  # Update as per your requirements
     ```

10. **Edit Paths**:
    - Update file paths as needed, for example:
      ```python
      codePath = r"C:\Users\usera\AppData\Local\Programs\Microsoft VS Code\Code.exe"  # For opening VS Code
      ```

11. **Install Requirements**:
    - Open the terminal in VS Code.
    - Run the command:
      ```
      pip install -r requirements.txt
      ```

12. **Run the Application**:
    - Run the command:
      ```
      python .\ShadowGui\shadow.py
      ```

## Contribution

Contributions to Voice Assistance are welcome! If you'd like to contribute, please follow the guidelines outlined in the CONTRIBUTING.md file.

## Support

For support or assistance with Voice Assistance, please contact [vidhin1208@gmail.com](mailto:vidhin1208@gmail.com).

## License

Voice Assistance is licensed under the [MIT License](LICENSE).
