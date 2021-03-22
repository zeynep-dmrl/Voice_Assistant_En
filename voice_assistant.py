import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voice[1].id')                  # voice[0].id = Male voice
                                                            # voice[1].id = Female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =  int(datetime.now().hour)
    if(hour >= 6 and hour<12):
        speak("Hello,Good Morning")
        print("Good Morning :)")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
        print("Good Afternoon :)")
    elif(hour>=18 and hour<22):
        speak("Good Evening")
        print("Good Evening:)")
    else:
        speak("Good Night")
        print("Good Night...")

def takeCommand():
    response = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        response.pause_threshold = 1
        audio = response.listen(source)

        try:
            print("Recognizing...")
            statement = response.recognize_google(audio, language="en-in")
            print(f"User said: {statement}\n")
        except Exception as e:
            print("Sorry say that again please!")
            return "None"
        return statement

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login( 'mailadress','password')
    server.sendmail('mailadress', to, content)
    server.close()

speak("Loading your AI assistanat...")
wishMe()

if __name__ == "__main__":
    speak("Hello! Hope you all are doing well")
    speak("How can I help you?")

    while True:
        statement = takeCommand().lower()

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(f"{statement},sentences=2")
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement or 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
        elif 'open google' in statement or 'google' in statement :
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
        elif 'open gmail' in statement or 'gmail' in statement :
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
            speak("Your Google Mail account open now")
        elif 'time' in statement:
            time_now = datetime.now().strftime("%H:%M:%S")
            speak(f"Now, the time is {time_now}")
        elif 'send mail' in statement:
            try:
                speak("What should I say?")
                print("Content:")
                content = takeCommand()
                speak("Whom should I send mail?")
                print("To:")
                to = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
        elif 'close' in statement or 'exit' in statement or 'stop' in statement or 'goodbye' in statement:
            speak("I am closing")
            print("Closing...")
            speak("Have good day...")
            break
        elif 'what is your name' in statement:
            speak("My name is asisstant")
        elif 'how old are you'in statement:
            speak("We are at the same age. Did you forget?")
        elif 'how are you' in statement:
            speak("Fine thanks and you?")
        elif 'who are you' in statement:
            speak("I am your voice assistant created by you.")
        elif 'search' in statement:
            speak("what ı search for you?")
            q = takeCommand()
            webbrowser.open_new_tab("https://www.google.com/search?q=+"+q)
            speak("I am searching...")
