import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import re
import speech_recognition as sr
from threading import Thread, Event
import logging
from logging.handlers import RotatingFileHandler



app = Flask(__name__)
socketio = SocketIO(app)

# Initialize the recognizer
recognizer = sr.Recognizer()
listening = Event()

# Setup logging
logger = logging.getLogger('autotasker')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('autotasker.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(console_handler)

def log_message(message):
    """Emit log message to clients via SocketIO."""
    try:
        logger.debug(message)  # Log at debug level for file
    except PermissionError:
        logger.error("Permission error occurred while rotating the log file. Retrying...")
    socketio.emit('log', {'message': message})

def send_email(receiver_email, custom_subject, custom_message):
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = custom_subject
    message.attach(MIMEText(custom_message, "plain"))

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    smtp_server.sendmail(sender_email, receiver_email, message.as_string())
    smtp_server.quit()

def execute_command(command):
    command = command.strip().lower()
    negation_words = ["not", "don't", "dont", "do not", "never"]
    if any(negation_word in command for negation_word in negation_words):
        return "Command contains negation, not executing."

    command_keywords = {
        "chrome": lambda: os.system("start chrome"),
        "instagram": lambda: os.system("start chrome https://www.instagram.com"),
        "whatsapp": lambda: os.system("start chrome https://web.whatsapp.com/"),
        "telegram": lambda: os.system("start Telegram.exe"),
        "gmail": lambda: open_gmail(),
        "camera": lambda: os.system("start microsoft.windows.camera:"),
        "snapchat": lambda: os.system("start snapchat://"),
        "excel": lambda: os.system("start excel"),
        "powerpoint": lambda: os.system("start powerpnt"),
        "paint": lambda: os.system("start mspaint"),
        "notepad": lambda: os.system("start notepad"),
        "obs studio": lambda: os.system("start obs64"),
        "file manager": lambda: os.system("start explorer"),
        "lw intern folder": lambda: os.system("start explorer E:\\LW AI INTERN 2024"),
        "terminal run jupyter": lambda: os.system("start cmd /k jupyter notebook"),
        "terminal create notebook": lambda: os.system("start cmd /k jupyter notebook"),
        "save notebook": lambda: "Saving current notebook",
        "media player": lambda: os.system("start wmplayer"),
        "linkedin": lambda: os.system("start chrome https://www.linkedin.com")
    }

    for keyword, function in command_keywords.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', command):
            function()
            return f"Executing {keyword}"

    return "Invalid command"

def open_gmail():
    sub_option = input("Choose a sub-option:\n1. Open Gmail in browser\n2. Send Email")
    if sub_option == '1':
        os.system("start chrome https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    elif sub_option == '2':
        receiver_email = input("Enter the recipient's email address:")
        custom_subject = input("Enter the subject:")
        custom_message = input("Enter your message:")
        send_email(receiver_email, custom_subject, custom_message)

def listen_and_execute():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            listening.wait()  # Wait until the listening event is set
            try:
                log_message("Listening for commands...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Adjust the timeout as needed
                log_message("Processing...")
                text = recognizer.recognize_google(audio)
                log_message(f"You said: {text}")
                socketio.emit('recognized_text', {'text': text})
                result = execute_command(text)
                log_message(result)
                socketio.emit('status_update', {'message': result})
            except sr.WaitTimeoutError:
                log_message("Listening timeout, trying again...")
            except sr.UnknownValueError:
                log_message("Could not understand the command, please try again.")
                socketio.emit('recognized_text', {'text': "Could not understand the command, please try again."})
            except Exception as e:
                log_message(f"An error occurred: {str(e)}")
                socketio.emit('recognized_text', {'text': f"An error occurred: {str(e)}"})



from pytube import YouTube
import os

DOWNLOADS_DIR = "path/to/your/downloads"  # Change this path as needed








@app.route('/Speed')
def Speed():
    return render_template('Speed.html')


@app.route('/download_video', methods=['POST'])
def download_video():
    data = request.get_json()
    link = data.get('link')
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        video_dir = os.path.join(DOWNLOADS_DIR, "video")
        os.makedirs(video_dir, exist_ok=True)
        stream.download(output_path=video_dir)
        return jsonify({'title': yt.title, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'})

@app.route('/download_audio', methods=['POST'])
def download_audio():
    data = request.get_json()
    link = data.get('link')
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        audio_dir = os.path.join(DOWNLOADS_DIR, "audio")
        os.makedirs(audio_dir, exist_ok=True)
        stream.download(output_path=audio_dir)
        return jsonify({'title': yt.title, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'})

@app.route('/Yaud')
def Yaud():
    return render_template('Yaud.html')

# Define routes to render templates
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/w1')
def w1():
    return render_template('w1.html')
@app.route('/g3')
def g3():
    return render_template('g3.html')
@app.route('/NoteEditor')
def NoteEditor():
    return render_template('NoteEditor.html')
@app.route('/MemGame')
def MemGame():
    return render_template('MemGame.html')

@app.route('/MusicPlayer')
def MusicPlayer():
    return render_template('MusicPlayer.html')

@app.route('/G2')
def G2():
    return render_template('G2.html')

@app.route('/char')
def char():
    return render_template('char.html')

@app.route('/comp')
def comp():
    return render_template('comp.html')

@app.route('/TodoMemo')
def TodoMemo():
    return render_template('TodoMemo.html')

@app.route('/G4')
def G4():
    return render_template('G4.html')

@app.route('/age')
def age():
    return render_template('age.html')

@app.route('/execute', methods=['POST'])
def handle_execute():
    data = request.get_json()
    command = data.get('command', '')
    message = execute_command(command)
    socketio.emit('status_update', {'message': message})
    return jsonify({'message': message})

@app.route('/start_listening', methods=['POST'])
def start_listening():
    listening.set()
    log_message("Started listening for voice commands.")
    return jsonify({'status': 'Listening started'})

@app.route('/stop_listening', methods=['POST'])
def stop_listening():
    listening.clear()
    log_message("Stopped listening for voice commands.")
    return jsonify({'status': 'Listening stopped'})

if __name__ == '__main__':
    # Start the voice recognition thread
    voice_thread = Thread(target=listen_and_execute)
    voice_thread.daemon = True
    voice_thread.start()

    # Run the Flask app with SocketIO
    socketio.run(app, debug=True)