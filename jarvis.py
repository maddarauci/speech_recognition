'''
this project will be using ttsx -- python text to speech
and speech_recognition
'''

import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os, sys, random
import webbrowser

# making rhe sapi5 the main engine
'''
The Speech Application Programming Interface or SAPI is an API developed by Microsoft
to allow the use of speech recognition and speech synthesis within Windows applications.
'''
engine = pyttsx3.init('sapi5')
#engine = pyttsx3.init()

def speak(audio):
    print('computer: '+ audio)
    engine.say(audio)
    engine.runAndWait()

def greetings():
    current_hour = int(datetime.datetime.now().hour)
    if current_hour >= 0 and current_hour < 12:
        speak('good mornging!')
    elif current_hour >= 12 and current_hour < 18:
        speak('good afternoon')
    elif current_hour >= 18 and current_hour !=0:
        speak('good evening')

greetings()

speak('Hello Sir, I am your digital assistant!')
speak('How may I help you?')

def make_Command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

if __name__ == '__main__':
    while True:
        query = make_Command()
        query = query.lower()

        # using webbrowser to open youtube
        if 'open youtube' in query:
            speak('bet say no more!')
            webbrowser.open('www.youtube.com')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello')

        elif 'bye' in query:
            speak('Bye Mate, have a good day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')

            speak("what's next now! Sir!")
