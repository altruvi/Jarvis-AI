import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
       import speech_recognition as sr

r = sr.Recognizer()

while True:
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source)
                query = r.recognize_google(audio)
                print("You said:", query)
        except Exception as e:
            print("Some error occurred:", e)

            print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
        
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Some error occurred: {e}")
