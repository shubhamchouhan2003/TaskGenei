# Test.py

import datetime

def run_send_messages():
    # Read the contents of send_messages.py
    with open("E:/LW AI INTERN 2024/whatsapp-bulk/send_messages.py", "r") as file:
        send_messages_code = file.read()

    # Execute the code from send_messages.py, passing the required modules as globals
    exec(send_messages_code, globals())

# Call the function to run send_messages.py
run_send_messages()
