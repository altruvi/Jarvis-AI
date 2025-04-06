import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Use the correct device index for your microphone
device_index = 14  # Replace this with the index of your microphone

try:
    print("Listening.....")
    # Ensure proper usage of Microphone within 'with' statement
    with sr.Microphone(device_index=device_index) as source:
        r.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
        print("Say something...")
        audio = r.listen(source)  # Listen for audio input

    # Recognize speech using Google Web Speech API
    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

except Exception as e:
    print(f"An error occurred: {e}")
