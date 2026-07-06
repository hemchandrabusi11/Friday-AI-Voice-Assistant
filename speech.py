import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)  # index 1 is often female voice on Windows

def speak(text):
    print(f"FRIDAY: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 0.8
            try:
                r.adjust_for_ambient_noise(source, duration=0.5)
            except Exception:
                pass

            print("Listening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=8)
            except (sr.WaitTimeoutError, OSError, Exception):
                return ""
    except (OSError, Exception):
        return ""

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        return ""