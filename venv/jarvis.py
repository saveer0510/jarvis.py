import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
from datetime import date
import time as tim

today = date.today()
print("Today's date:", today)

listner= sr.Recognizer()
engine =pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say('i am jarvis')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wish():
 print("ew")
 hour = int(datetime.datetime.now().hour)
 if 0<=hour<12:

     talk("good morning sir")
 elif 12<=hour<16:
        talk("good afternoon sir")
 else:

        talk("good evening sir")
def war():
    hour = int(datetime.datetime.now().hour)
    if 21<=hour:
        talk('boss go to sleep')
def dat():
 try:
    with sr.Microphone() as source:

        print("what to write....")
        talk("what to write")
        voice=listner.listen(source)

        command = listner.recognize_google(voice)
        command=command.lower()
        print(command)
 except Exception as e:
  print('could not understand ')
 pass

 return command

def se():
 try:
         with sr.Microphone() as source:

             print("what to search....")
             talk("what to search")
             voice = listner.listen(source)
             command = listner.recognize_google(voice)
             commander = command.lower()
             print(commander)
 except Exception as e:
         print('could not understand ')
 pass


 return commander


def file_name():
    try:
        with sr.Microphone() as source:

            print("what is the name....")
            talk("what is the name")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            file = command.lower()
            print(file)
    except Exception as e:
        print('could not understand ')
    pass

    return file
def take():
 try:
    with sr.Microphone(0) as source:


        print("listening sir....")
        talk("how can i help you")
        voice=listner.listen(source)
        command = listner.recognize_google(voice)
        command=command.lower()
        print(command)
        #if ('siri')  in command:
            #print(command)
           # command1=command.replace('siri','')
            #print(command1)

        #else:
         #   talk("you do not  call siri")
          #  run()
 except Exception as e:
  talk('there is an error ')
  run()

 pass

 return command

def run():
    war()
    com=take()
    if 'play' in com:
        song = com.replace('play','')
        print('playing'+song)
        pywhatkit.playonyt(song)

        run()
    elif 'time' in  com:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(time)
        tim.sleep(5)

        run()


    elif 'date' in com:
        d2 = today.strftime("%d %B, %Y")
        print("d2 =", d2)
        talk(d2)
        tim.sleep(5)

        run()


    elif 'joke' in com:
        talk(pyjokes.get_joke())
        run()
        tim.sleep(5)

    elif 'create text file' in com:
        fn = file_name()
        n=fn+".txt"
        data= dat()
        fh=open(n,'w')
        fh.write(data)
        fh.close()
        tim.sleep(5)

        run()
    elif 'create word document' in com:
        fn = file_name()
        nf=fn+".rtf"
        fh = open(nf, 'w')
        data= dat()

        fh.write(data)
        fh.close()
        tim.sleep(5)

        run()
    elif  'about '  in com:
        about=com
        info=wikipedia.summary(about,1)
        print(info)
        talk(info)
        run()
    elif 'open pycharm' in com:
        path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2020.3.lnk'
        os.startfile(path)
        talk('opening pycharm')
        tim.sleep(5)

    elif ' open vlc' in com:
        path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player.lnk'
        os.startfile(path)
        talk('VLC')
        tim.sleep(5)
    elif 'open notepad' in com:
        path='C:\\Users\sirisha\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\\Notepad.lnk'
        os.startfile(path)


    elif  (' go to bharat ane nenu'or 'go to bharatanenenu')in com:
        path = "D:\Bharat Ane Nenu (2018) Telugu v2 True HQ HDRip - 720p - x264 - AAC - 1.4GB.mkv"
        os.startfile(path)
        talk("playing bharat ane nenu")
        run()
    elif ' k' in com:
        path="D:\\"
        os.startfile(path)
        run()

    elif 'open' in com:
        op = com.replace("open ", 'www.')
        cp = op.replace('www.', '')

        talk("opening" + cp)
        c = ".com"

        url = op + c
        print(url)
        ch = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk %s'
        webbrowser.open(url)
        run()
    elif 'search' in com:
        opp=se()
        op ='/search?q='
        ad=opp.replace(' ','+')
        print(ad)
        cp = "www.google.com"

        talk("searching" + opp)

        url =  cp+op+ad
        print(url)
        ch = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk %s'
        webbrowser.open(url)
        tim.sleep(5)
        run()

    elif 'stop' in com:
        print('stop')
        war()
        tim.sleep(20)

    elif ('shut down' or 'shutdown' or 'power off')  in com:
        shut_down()


    else:
        talk('say that again')

        run()


def shut_down():

    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

    if shutdown == 'no':
        exit()
    else:
        os.system("shutdown /s /t 1")
wish()
war()
run()

