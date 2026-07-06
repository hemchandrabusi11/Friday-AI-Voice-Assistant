from speech import speak, listen
from skills import handle_skill
from brain import think

WAKE_WORD = "friday"

def run():
    speak("Friday online. How can I help you?")
    while True:
        command = listen()
        if not command:
            continue

        if WAKE_WORD in command:
            command = command.replace(WAKE_WORD, "").strip()
            if not command:
                speak("Yes?")
                continue

            skill_response = handle_skill(command)

            if skill_response == "SHUTDOWN":
                speak("Shutting down. Goodbye.")
                break
            elif skill_response:
                speak(skill_response)
            else:
                ai_response = think(command)
                speak(ai_response)

if __name__ == "__main__":
    run()