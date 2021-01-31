import pyttsx3    # pip install pyttsx3
import speech_recognition as sr   # pip install speechRecognition
import datetime  #  to work with the date as well as time with this module. It comes built into Python, so there is no need to install it externally.
import wikipedia   # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')   # The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within windows application.
voices = engine.getProperty('voices') 
# print(voices[0].id)   # this voices we comment out bcz its for checking about audio's
engine.setProperty('voice', voices[0].id) # here in this voice library we have only ZIRA's voice at index 0



def speak(audio):   #This functon taking arguent as audio and then speak
    engine.say(audio)   # This function will convert the text to speech (text is the input from the user)
    engine.runAndWait()  #This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.

    
def wishMe():  # This function will wish me with time set through speak function
    hour = int(datetime.datetime.now().hour)  # to get time in hour 

    if hour>=0 and hour<12:
        speak("Good Morning! ")

    elif hour>=12 and hour<16:
        speak("Good Afternoon! ")

    elif hour>=16 and hour<20:
        speak("Good Evening! ")

    else:
        speak("Good Night!")

    speak("Hello Kamal Sir, I am Jarvis. Please tell me how may I help You")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()   # Recognizer class use to recognize audio
    with sr.Microphone() as source:   # to use source Microphone
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)  

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)   # in project we r not using bcz it prints error msg on run time so avoiding

        print("Say that again please...")
        return "None"
    return query

 # for this function enable less secure apps
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":     # this is main method
    # speak("Hello everyone, Hare Krishna")   # here we give string in speak function
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()  # To convert take command in lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")   # if in our query present wikipedia then speak function say Searching wikipedia
            query = query.replace("wikipedia", " ")  # this will replace wikipedia with blank in query
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:  # you tube already have in query
            webbrowser.open("youtube.com")

        elif 'open google' in query:  # google already have in query
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:  # you tube already have in query
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Favourite Songs'  # here \\ is use for escape sequence character
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  # here we can use random function

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\nicka\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to kamal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kamalyouremail.gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend kamal bhai, I am not able to send this email")

        elif 'quit' in query:
            exit()










