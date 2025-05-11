import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is down.")
        return ""

def voice_assistant():
    speak("Hello! I am your simple voice assistant. How can I help you?")

    while True:
        query = listen()

        if 'hello' in query:
            speak("Hi there! How can I help you today?")
        elif 'your name' in query:
            speak("I am your voice assistant created in Python.")
        elif 'how are you' in query:
            speak("I am functioning as expected. Thank you!")
        elif 'bye' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day!")
            break
        elif query != "":
            speak("Sorry, I can't understand that yet.")

if __name__ == "__main__":
    voice_assistant()
