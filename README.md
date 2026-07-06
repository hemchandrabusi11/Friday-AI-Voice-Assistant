@"
# Friday AI Assistant

A Python-based Friday AI assistant that understands voice commands, opens apps, and answers questions using OpenRouter.

## Features
- Voice command recognition
- Opens applications like Notepad
- Opens websites like YouTube and Google in Chrome
- Answers questions using OpenRouter
- Saves command history into a log file

## Tech Stack
- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- OpenRouter API

## Project Structure
- `main.py` - main voice assistant loop
- `speech.py` - voice input and output
- `skills.py` - local commands and automation skills
- `brain.py` - AI response handling
- `friday.log` - saved command history

## How to Run
1. Install dependencies:
   ```bash
   py -m pip install -r requirements.txt
   ```

2. Create a `.env` file:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```

3. Run the project:
   ```bash
   py main.py
   ```

## Example Commands
- Friday open notepad
- Friday open youtube
- Friday what time is it
- Friday search wikipedia artificial intelligence

## Notes
- Do not upload `.env` to GitHub
- Make sure your microphone permissions are enabled in Windows
"@ | Set-Content README.md
