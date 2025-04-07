import speech_recognition as sr
import webbrowser
import pyttsx3
 
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text )
    engine.runAndWait()
 
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    pass
    
 
if __name__ == "__main__":
     speak("Initialising jarvis.....")
     r = sr.Recognizer()

     with sr.Microphone() as source:
        print("Adjusting for ambient noise. Please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening for 'Jarvis'...")

        while True:
            try:
                with sr.Microphone() as source:
                    # obtain audio from the microphone
                    audio = r.listen(source, timeout=5, phrase_time_limit=10)
                    print("recognizing...")
                word = r.recognize_google(audio)
                # Listen for the wake word "jarvis "
                if word.lower() == "jarvis":
                    speak("Hello sir")
                else:
                    print("Wake word not detected. Listening again...")
                    
                # Listen For command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                print(command)
                processCommand(command)
                
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))              