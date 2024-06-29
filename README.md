# TaskGenei
TaskGenei (Automator)

TaskGenei is a web application designed to automate various tasks through voice commands. It includes features such as executing commands, sending emails, downloading YouTube videos and audio, and more.

## Features

- Execute system commands via voice
- Send emails with custom subjects and messages
- Download YouTube videos and audio
- Real-time server logs and status updates
- User authentication and login

## Requirements

- Python 3.7+
- Flask
- Flask-SocketIO
- pytube
- SpeechRecognition
- eventlet
- greenlet

## Installation

### Clone the repository

```bash
git clone [[https://github.com/yourusername/autotasker.git](https://github.com/shubhamchouhan2003/TaskGenei.git)]
cd autotasker

##Setup Virtual Environment
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
Install the required Python packages using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Configuration
Before running the application, make sure to configure your email settings in the send_email function in the app.py file:

python
Copy code
sender_email = "your_email@example.com"
sender_password = "your_email_password"
Replace these values with your actual email and password.

Run the Application
Start the Flask application with SocketIO:

bash
Copy code
python app.py
Open your browser and navigate to http://localhost:5000 to view the application.

#File Structure

TaskThor/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── Image/
│       └── Logo1.png
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── tools.html
│   ├── home.html
│   ├── w1.html
│   ├── g3.html
│   ├── NoteEditor.html
│   ├── MemGame.html
│   ├── MusicPlayer.html
│   ├── G2.html
│   ├── char.html
│   ├── comp.html
│   ├── TodoMemo.html
│   ├── G4.html
│   ├── age.html
│   ├── Speed.html
│   └── Yaud.html
│
├── app.py
├── requirements.txt
├── README.md
└── autotasker.log

Usage
Voice Commands
The application listens for voice commands and executes them. Some of the supported commands include:

"Open Chrome"
"Open Instagram"
"Open WhatsApp"
"Open Telegram"
"Open Gmail"
"Open Camera"
"Open Snapchat"
"Open Excel"
"Open PowerPoint"
"Open Paint"
"Open Notepad"
"Open OBS Studio"
"Open File Manager"
"Open LW Intern Folder"
"Open Terminal and Run Jupyter Notebook"
"Save Notebook"
"Open Media Player"
"Open LinkedIn"

Features/Games:-
 
Age Calculator
Tic-Tac-Toe
Notes
YT Audio/Video Downloader
