import os

def sendMessage(receiver, textMessage):
    os.system('''osascript -e 'tell application "Messages" to send "''' + textMessage + '''" to buddy "'''+ receiver + '''"''' + "'")
