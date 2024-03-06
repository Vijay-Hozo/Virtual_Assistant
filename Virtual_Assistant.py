import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)

    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk("I'm your Nancy...What can I do for you")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'nancy' in command:
                command =command.replace('nancy','')
                print(command)
    except:
        pass
    return command

def run_nancy():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace("play","")
        talk('playing ' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'love you' in command:
        print('Sorry, I am just your virtual assistant(nancy)')
        talk('Sorry, I am just your virtual assistant(nancy)')
    elif 'come for a date' in command:
        print('Sorry, I am just your virtual assistant(nancy)')
        talk('Sorry, I am just your virtual assistant(nancy)')
    elif 'are you single' in command:
        print('Sorry, I am just your virtual assistant(nancy)')
        talk('Sorry, I am just your virtual assistant(nancy)')


    elif 'joke' in command:
        y=pyjokes.get_joke()
        print(y)
        talk(y)

    elif 'catch you later' in command:
        print('bye bye I miss you so much')
        talk('bye bye I miss you so much')
        exit()


    else:
        talk('please say the command again')


while True:
    run_nancy()