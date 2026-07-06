import os
import datetime
import webbrowser
import pyautogui
import wikipedia
import pywhatkit as kit

def open_in_chrome(url):
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('chrome').open(url)
            return True

    return False

def handle_skill(command):
    command = command.lower().strip()

    if "time" in command:
        return datetime.datetime.now().strftime("It's %I:%M %p")

    elif "notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "youtube" in command:
        if open_in_chrome("https://www.youtube.com"):
            return "Opening YouTube in Chrome"
        return "Chrome not found, so I could not open YouTube in Chrome."

    elif "google" in command:
        if open_in_chrome("https://www.google.com"):
            return "Opening Google in Chrome"
        return "Chrome not found, so I could not open Google in Chrome."

    elif "search" in command and "wikipedia" in command:
        topic = command.replace("search", "").replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(topic, sentences=2)
            return result
        except Exception:
            return "I couldn't find that on Wikipedia."

    elif "play" in command:
        song = command.replace("play", "").strip()
        kit.playonyt(song)
        return f"Playing {song} on YouTube"

    elif "screenshot" in command:
        img = pyautogui.screenshot()
        path = os.path.join(os.path.expanduser("~"), "Desktop", "friday_screenshot.png")
        img.save(path)
        return "Screenshot saved to Desktop"

    elif "shutdown" in command:
        return "SHUTDOWN"

    return None