import webbrowser 
import os 
import datetime 
import pywhatkit 
from ai import ask_ai
from voice import speak 
def execute_command(command):

    if command == "":
        speak("Please say something")
        return True
    if "who" in command or "what" in command or "tell" in command:
        response = ask_ai(command)
        speak(response)

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "chatgpt" in command:
        speak("Opening chatgpt")
        webbrowser.open("https://chatgpt.com/")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open" in command:
        site = command.replace("open", "").strip()
        if site != "":
            speak(f"Opening {site}")
            webbrowser.open(f"https://{site}.com")
        else:
            speak("Please tell me what to open")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye")
        return False

    else:
        speak("Sorry, I don't know that command yet")

    return True