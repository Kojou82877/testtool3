import fbchat
from fbchat import Client
from fbchat.models import *

import time
import os

# Define your Facebook email and password
username = input("Enter your Facebook email: ")
password = input("Enter your Facebook password: ")

# Define a function to send a message to a Facebook user or group
def send_facebook_message(message, thread_id, thread_type):
    client = fbchat.Client(username, password)

    try:
        # Send the message
        client.send(fbchat.models.Message(message), thread_id=thread_id, thread_type=thread_type)
        print("Message sent successfully")

    except fbchat.models.FBchatUserError:
        print("Invalid Facebook user or group ID")

    except fbchat.models.FBchatFacebookError:
        print("Error sending message")

    client.logout()

# Define a function to send a message from a text file to a Facebook user or group
def send_facebook_message_from_file(file_path, thread_id, thread_type):
    # Check that the file exists
    if not os.path.isfile(file_path):
        print("Invalid file path")
        return

    # Read the contents of the file
    with open(file_path, "r") as f:
        message = f.read()

    # Send the message
    send_facebook_message(message, thread_id, thread_type)

# Log in to Facebook
client = fbchat.Client(username, password)

# Define the ID of the Facebook user or group to send the message to
thread_id = input("Enter the ID of the Facebook user or group to send the message to: ")

# Define the type of thread (user or group)
thread_type = input("Enter the type of thread (USER or GROUP): ")

# Convert the thread_type input to the appropriate enum value
if thread_type.lower() == "user":
    thread_type = fbchat.models.ThreadType.USER
elif thread_type.lower() == "group":
    thread_type = fbchat.models.ThreadType.GROUP
else:
    print("Invalid thread type")
    client.logout()
    exit()

# Define the message to send
message = input("Enter the message to send: ")

# Send the message
send_facebook_message(message, thread_id, thread_type)

# Wait for 5 seconds before sending another message
time.sleep(5)

# Define the path to the text file containing the message to send
file_path = input("Enter the path to the text file containing the message to send: ")

# Send the message from the text file
send_facebook_message_from_file(file_path, thread_id, thread_type)

# Log out of Facebook
client.logout()
