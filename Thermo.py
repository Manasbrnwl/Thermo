import datetime
import os     
import pyttsx3      
import speech_recognition as sr         
import webbrowser as wb         
import wikipedia       
import pyautogui as ui  
import wolframalpha as wa   
from googlesearch import search 
import pocketsphinx              
from time import sleep
import urllib.request
import rotatescreen as rs
import keyboard
import subprocess
import smtplib
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from playsound import playsound
#from lsHotword import ls


#Voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

#Chatbot
chatbot = ChatBot('Thermo')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def login():
    hour = int(datetime.datetime.now().hour)
    if (hour>=6 and hour< 12):
        speak("Good Morning !")
    elif (hour>= 12 and hour<18):
        speak ("Good Afternoon !")
    else:
        speak("Good Evening !")
    date()
    speak("I am Thermo , Please guide me how may i help you")


def logout():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning"+ name)
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon"+ name)
    elif (hour >= 18 and hour < 20):
        speak("Good Evening"+ name)
    else:
        speak("Good Night.. Sweet Dreams"+ name)


def reciver():

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening......")
         r.adjust_for_ambient_noise(source)
         r.pause_threshold = 1
         r.energy_threshold = 3000
         #r.non_speaking_duration = 60
         audio = r.listen(source)
         
    try:
         print("Recognizing......")
         query = r.recognize_google(audio, language="en-in")
         print(f"You said: {query}\n")

    except Exception as e:
         print(e)
         print("Parden please......")
         return"None"
    return query

def Wakeup():

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening......")
         r.adjust_for_ambient_noise(source)
         r.pause_threshold = .3
         r.energy_threshold = 3000
         r.non_speaking_duration = .3
         audio = r.listen(source)
         
    try:
         print("Recognizing......")
         query = r.recognize_google(audio, language="en-in")
         print(f"You said: {query}\n")

    except Exception as e:
         print(e)
         print("Parden please......")
         return"None"
    return query


def portrait():

    screen = rs.get_primary_display()
    screen.rotate_to(90)


def landscape():
    screen = rs.get_primary_display()
    screen.rotate_to(0)


def offline():

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening......")
         r.adjust_for_ambient_noise(source)
         r.pause_threshold = 1.3
         r.energy_threshold = 300
         audio = r.listen(source)
         
    try:
         print("Recognizing......")
         query = r.recognize_sphinx(audio, language="en-IN")
         print(f"You said: {query}\n")

    except Exception as e:
         print(e)
         print("Parden please......")
         return"None"
    return query


def screenCapture():
    speak('name your screenshot')
    query = reciver()
    myScreenshot = ui.screenshot()
    myScreenshot.save(r'D:\\Python\\ThermO\\Screenshot\\'+query+'.png')


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {Time}")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def information():
    speak("I am Thermo, version 2.0, I am an Computer Assistent, I am developed by Manas Baranwal on 4 November 2020 in INDIA")
    speak("Now i hope you know me")

if __name__ == "__main__":

    print("         =====================================================================================================         ")
    print("                   _______     _     _     _____     __________    ___         ___       ______                        ")
    print("                  !___ ___!   ! !   ! !   ! ____!   !   __    /   !   \       /   !     (      )                       ")
    print("                     ! !      ! !___! !   ! !__     !  !_/   /    ! !\ \     / /! !    (   ()   )                      ")
    print("                     ! !      !  ___  !   !  __!    !     __/     ! ! \ \   / / ! !   (   (  )   )                     ")
    print("                     ! !      ! !   ! !   ! !___    ! !\  \       ! !  \ \_/ /  ! !    (   ()   )                      ")
    print("                     !_!      !_!   !_!   !_____!   !_!  \__\     !_!   \___/   !_!     (______)                       ")
    print("         =====================================================================================================         ")
    print("                                                                                         A COMPUTER ASSISTANT          ")   
    print("                                                                                        ======================         ")   
    print("                                                                               Developed By :- Manas Baranwal          ")  
    print("                                                                              --------------------------------         ")                      
    print("\n")
    login()

    def connect(host='http://google.com'):

        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False
    # test
    speak( 'You are connected to internet!' if connect() else 'you are not connected on internet' )

#When you are connected to internet
    
    if connect():
        
    #User's name 
        
        speak("can i know your good name ?")

        name = reciver().lower()

        name = name.replace("my name is", " ")

        speak('Hello' + name)

        print('Speak :- ( Hello Thermo , Hey Thermo or Activate Thermo ) to Wakeup the Thermo.')

        while(True):
                #print('speak thermo')
                #ls.lsHotword_loop()
                query = Wakeup().lower()
                
                if('thermo' in query or 'activate' in query 
                or 'hello' in query or 'hey' in query):
                    playsound('Thermo.mp3')


                    query = reciver().lower()
                
        #Open Visual Stdio Code

                    if ('open code' in query or 'visual stdio' in query 
                    or 'v s code' in query):
                        speak("opening visual stdio code")
                        codePath = "C:\\Users\\Manas Baranwal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        vs = os.startfile(codePath)
                        continue
                    
                    elif 'close vs code' in query:
                        os.system("taskkill /f /im Code.exe")
                        continue
                    
        #Open Microsoft Word

                    elif ('open word' in query or 'ms word' in query 
                    or 'microsoft word' in query):
                        speak("opening microsoft word")
                        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                        word = os.startfile(codePath)
                        continue
                    
                    elif 'close word' in query:
                        os.system("taskkill /f /im WINWORD.EXE")
                        continue
                    
        #Open Microsoft Excel

                    elif ('open excel' in query or 'ms excel' in query 
                    or 'microsoft excel' in query or 'xl' in query
                    or 'data sheet' in query):
                        speak("opening microsoft excel")
                        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                        excel = os.startfile(codePath)
                        continue
                    
                    elif 'close excel' in query or 'close xl' in query:
                        os.system("taskkill /f /im EXCEL.EXE")
                        continue
                    
        #Open Microsoft Powerpoint

                    elif ('open powerpoint' in query or 'ms powerpoint' in query 
                    or 'microsoft powerpoint' in query or 'ppt' in query):
                        speak("opening microsoft powerpoint")
                        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                        ppt = os.startfile(codePath)
                        continue
                    
                    elif 'close powerpoint' in query:
                        os.system("taskkill /f /im POWERPOINT.EXE")
                        continue
                    
        #Open Microsoft Access

                    elif ('open access' in query or 'ms access' in query 
                    or 'microsoft access' in query):
                        speak("opening microsoft access")
                        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
                        access = os.startfile(codePath)
                        continue
                    
                    elif 'close access' in query:
                        os.system("taskkill /f /im MSACCESS.EXE")
                        continue

        #Open Microsoft Teams

                    elif ('open team' in query or 'ms team' in query 
                    or 'microsoft team' in query):
                        speak("opening microsoft team")
                        codePath = "C:\\Users\\Manas Baranwal\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
                        access = os.startfile(codePath)
                        continue
                    
                    elif 'close team' in query:
                        os.system("taskkill /f /im Update.exe")
                        continue
                    
        #Open Blender
        
                    elif('open blender' in query):
                        speak("opening blender")
                        codePath = "C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe"
                        blender = os.startfile(codePath)
                        continue
                    
                    elif 'close blender' in query:
                        os.system("taskkill /f /im blender.exe")
                        continue
                    
        #Open Spotify

                    elif ('open spotify' in query):
                        speak("opening spotify")
                        codePath = "C:\\Users\\Manas Baranwal\\AppData\\Roaming\\Spotify\\Spotify.exe"
                        spotify = os.startfile(codePath)
                        sleep(2)
                        ui.press('space')
                        continue

                    elif 'close spotify' in query:
                        os.system("taskkill /f /im Spotify.exe")
                        continue

        #Searching on Wikipedia

                    elif ('wikipedia' in query or 'who' in query
                    or 'when' in query or 'where' in query):
                        try:
                            speak("searching...")
                            query = query.replace("wikipedia", "")
                            query = query.replace("according to", "")
                            query = query.replace("search", "")
                            query = query.replace("when", "")
                            query = query.replace("where", "")
                            query = query.replace("who", "")
                            query = query.replace("is", "")
                            result = wikipedia.summary(query, sentences=2)
                            speak("According to wikipedia")
                            print(result)
                            speak(result)
                        except Exception:
                            speak("Sorry i am to search your query")

        #Ask any question

                    elif ('what is' in query or "how much is" in query 
                    or 'joke' in query):
                        try:
                            speak("searching...")
                            query=query.replace("what is", "")
                            query=query.replace("how much is", "")
                            app_id="XWVQYR-3REARW7W5A"
                            client = wa.Client('XWVQYR-3REARW7W5A')
                            res = client.query(query)
                            answer = next(res.results).text
                            print(answer)
                            speak(answer)
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Open Google

                    elif 'google' in query:
                        try:
                            speak("opening google")
                            wb.open("www.google.com")
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Open Youtube

                    elif 'youtube' in query:
                        try:
                            speak("opening youtube")
                            wb.open("youtube.com")    
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Open Stackoverflow

                    elif ('stackoverflow' in query or 'stack over flow' in query):
                        try:
                            speak("opening stack over flow")
                            wb.open("stackoverflow.com")    
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Open Github

                    elif ('github' in query or 'git hub' in query):
                        try:
                            speak("opening github")
                            wb.open("github.com")
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Open Instagram

                    elif 'instagram' in query:
                        try:
                            speak("opening instagram")
                            wb.open("instagram.com")
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Open Whatsapp Web

                    elif ('whatsappweb' in query or 'whatsapp web' in query
                    or 'whats app web' in query):
                        try:
                            speak("opening whatsapp web")
                            wb.open("web.whatsapp.com")  
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Websearch

                    elif 'search' in query:
                        try:
                            speak("Searching...")
                            query = query.replace("search"," ")
                            search(query, tld="co.in", num=10, stop=10, pause=2)
                            wb.open("https://google.com/search?q=%s" % query)
                        except Exception:
                            speak("Sorry i an unable to search your query")

                    elif 'close browser' in query:
                        os.system("taskkill /f /im msedge.exe")
                        continue
                    
        #Add Reminder

                    elif ("create a reminder list" in query or "reminder" in query):
                        speak("What is the reminder?")
                        try:
                            data = reciver()
                            speak("You said to remember that" + data)
                            reminder_file = open("thermo reminder.txt", 'a')
                            reminder_file.write('\n')
                            reminder_file.write(data)
                            reminder_file.close()
                        except Exception:
                            speak("Sorry i an unable to search your query")

        #Thermo Features
        
                    elif ("powers" in query or "features" in query or 'what can you do' in query):
                        features = '''                    i can help to do lot many things like...
                        i can tell you the current time,
                        i can create the reminder list,
                        i can shut down or restart your system,
                        i can tell you non funny jokes,
                        i can open any website (like google ,github ,stack over flow ,youtube  etc),
                        i can search anything on google,
                        i can search the thing on wikipedia,
                        i can answer to computational and geographical questions,
                        i can open application (like MS Word ,ms excel ,ms powerpoint ,spotify ,visual stdio  etc)
                        And yes one more thing, My creator is working on me to add more features...,
                        tell me what can i do for you??
                        '''
                        #print(features)
                        speak(features)
                        continue

        #Chatbot perform

                    elif ("let's talk" in query or 'want to talk' in query
                    or 'talk' in query):
                        #trainer = ChatterBotCorpusTrainer(chatbot)

                        #trainer.train('chatterbot.corpus.english')
                        speak("Ok! let's talk")
                        while True:
                            query=reciver().lower()
                            speak(chatbot.get_response(query))
                            if 'exit' in query:
                                speak('it was nice to talk to you!'+ name)
                                break
        #Introduce Itself

                    elif ("tell me about yourself" in query or "about you" in query 
                    or "who are you" in query or "yourself" in query):
                        information()
                        continue

        #Provide Time

                    elif 'time' in query:
                        time()
                        speak("Thank you")
                        continue

        #Screen Portrait

                    elif 'screen portrait' in query:
                        portrait()
                        speak('done!')
                        continue

        #Screen Landscape

                    elif 'screen landscape' in query:
                        landscape()
                        speak('done!')
                        continue
                    
        #Provide Date

                    elif 'date' in query:
                        date()
                        speak("thank you")
                        continue

        #Screenshot

                    elif ("screenshot" in query):
                        screenCapture()
                        speak("Done!")
                        continue

        #Appreciation
                    
                    elif "nice one" in query or "nice approach" in query:
                        speak("thank you sir for your appreciation")
                        continue

        #Close Application

                    elif 'close' in query:
                        keyboard.press_and_release('alt+F4')
                        speak('done!')
                        
        #Restart Computer

                    elif 'restart' in query or 'restart the pc' in query:
                        speak("do you want to restart this p. c.")
                        q = reciver()
                        if "yes" in q:
                            logout()
                            os.system("shutdown /r /t 1")  
                            break
                        else:
                            speak("ok sir")
                            continue

        #Shutting Down Computer

                    elif 'shutdown' in query or 'shut down' in query:
                        speak("do you want to shutdown this p. c.")
                        q = reciver()
                        if "yes" in q:
                            logout()
                            os.system("shutdown /s /t 1")  
                            break
                        else:
                            speak("ok sir")
                            continue
                        
        #Logout
        
                    elif ('i am done' in query or 'go offline' in query
                        or 'offline' in query or 'bye' in query):
                        logout()
                        break

                    elif " " in query:
                        continue

#When you are not connected through internet

    else:
        print('\n')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print('                                                     WARNING                                                           ')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print('\n')
        print('                                    This is less accurate in voice recognition ')

        speak('This is less accurate in voice recognition')
        print('\n')
        
        sleep(1)
        speak("can i know your good name ?")
        name = input('Your good name  :- ')
        print("\n")
        print("                                           1.  To Open Visual Stdio Code")
        print("                                           2.  To Open Microsoft Word")
        print("                                           3.  To Open Microsoft Powerpoint")
        print("                                           4.  To Open Microsoft Access")
        print("                                           5.  To Open Microsoft Excel")
        print("                                           6.  To Open Blender")
        print("                                           7.  To Open Spotify")
        print("                                           8.  To Add Reminder")
        print("                                           9.  Whats the Time")
        print("                                          10.  Whats the Date")
        print("                                          11.  To Shutdown the Computer")
        print("                                          12.  To Restart the Computer")
        print("                                          13.  Logout from Thermo")

        speak("Due to less accuracy I can do task by the call of above index numbers.")

        while(True):
            print("\n")
            #choice = int(input('Which one from above you will choose = '))

            choice = offline().lower()
            choice = choice.replace("thermo"," ")

    #Open Visual Stdio Code

            if(choice == 1 or 'vs code' in choice or 
                'v s code' in choice or '1' in choice or 
                'one' in choice):
                speak("opening visual stdio code")
                codePath = "C:\\Users\\Manas Baranwal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

    #Open Microsoft Word

            elif(choice == 2 or 'word' in choice or
                '2' in choice or 'two' in choice):
                speak("opening microsoft word")
                codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(codePath)

    #Open Microsoft Powerpoint

            elif(choice == 3 or 'powerpoint' in choice or 
                'power point' in choice or 'ppt' in choice or
                '3' in choice or 'three' in choice):
                 speak("opening microsoft powerpoint")
                 codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                 os.startfile(codePath)
                 
    #Open Microsoft Access
            
            elif(choice == 4 or 'access' in choice or
                '4' in choice or 'four' in choice):
                 speak("opening microsoft access")
                 codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
                 os.startfile(codePath)
                 
    #Open Microsoft Excel

            elif(choice == 5 or 'excel' in choice or 
                'xl' in choice or '5' in choice or 
                'five' in choice):
                 speak("opening microsoft excel")
                 codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"  
                 os.startfile(codePath) 
                
    #Open Blender

            elif(choice == 6 or 'blender' in choice or 
                '6' in choice or 'six' in choice):
                 speak("opening blender")
                 codePath = "C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe"
                 os.startfile(codePath)
                 
    #Open Spotify
      
            elif(choice == 7 or 'spotify' in choice or
                '7' in choice or 'seven' in choice):
                 speak("opening spotify")
                 codePath = "C:\\Users\\Manas Baranwal\\AppData\\Roaming\\Spotify\\Spotify.exe"
                 os.startfile(codePath)
                
    #Add Reminder

            elif(choice == 8 or 'reminder' in choice or 
                '8' in choice or 'eight' in choice):
                speak("add reminders ")
                speak("What is the reminder?")
                data = input("What is the reminder :- \n")
                speak("You said to remember that" + data)
                reminder_file = open("Thermo reminder.txt", 'a')
                reminder_file.write('\n')
                reminder_file.write(data)
                reminder_file.close()
                continue

    #Current Time

            elif(choice == 9 or 'time' in choice or 
                '9' in choice or 'nine' in choice):
                 speak("the current time")
                 time()
                 continue

    #Current Date

            elif(choice == 10  or 'date' in choice or
                '10' in choice or 'ten' in choice):
                speak("the current date")
                date()
                continue

    #Shutdown computer

            elif(choice == 11 or 'shutdown' in choice or 
                'shut down' in choice or '11' in choice or
                'eleven' in choice):
                 speak("shutdown the computer")
                 logout()
                 os.system("shutdown /s /t 1")
                 break

    #Restart computer

            elif(choice == 12 or 'restart' in choice or
                '12' in choice or 'twelve' in choice):
                 speak("restart the computer")
                 logout()
                 os.system("shutdown/r /t 1")
                 break

    #logout

            elif(choice == 13 or '13' in choice or
                'offline' in choice or 'thirteen' in choice):
                 logout()
                 speak("Thank you"+"It was nice to work with you")
                 break 
