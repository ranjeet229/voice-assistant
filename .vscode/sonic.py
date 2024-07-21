import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import wikipedia
from datetime import datetime

# Initialize the recognizer and the engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, the service is down.")
            return None

def process_command(command):
    stop_listening = False
    
    if 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Playing {song}")
        kit.playonyt(song)
        stop_listening = True
    elif 'search' in command:
        query = command.replace('search', '').strip()
        speak(f"Searching for {query}")
        kit.search(query)
        stop_listening = True
    elif 'hey buddy' in command:
        speak('Hello')
    elif 'who is' in command:
        query = command.replace('who is', '').strip()
        summary = wikipedia.summary(query, sentences=1)
        speak(summary)
    elif 'current time' in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif 'date' in command:
        today = datetime.now()
        current_date = today.strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif 'how are you' in command:
        speak("I am fine, what about you")
        
    elif 'ruk jao' in command:
        speak("Goodbye!")
        return True
    else:
        speak("I am not sure how to help with that.")
    
    return stop_listening

if __name__ == "__main__":
    speak("Hello, I am your sonic. How can I help you today?")
    while True:
        command = listen()
        if command:
            stop_listening = process_command(command.lower())
            if stop_listening:
                break

