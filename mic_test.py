import speech_recognition as sr

r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
print("Available microphones:", mic_list)

with sr.Microphone() as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source, timeout=5)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)