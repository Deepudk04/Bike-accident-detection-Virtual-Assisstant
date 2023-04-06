import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import geocoder
import smtplib
import ssl
from email.message import EmailMessage
import noisereduce as nr 
import wavfile

#load data 
#rate, data = wavfile.read("mywav.wav") 
# select section of data that is noise 
#noisy_part = data[10000:15000] 
# perform noise reduction 
#reduced_noise = nr.reduce_noise(audio_clip=data,noise_clip=noisy_part, verbose=True) 
# Defining email sender and receiver

email_sender = 'demoacc1802@gmail.com'
email_password = 'fjzmaamsgagfmmyp'
email_receiver = '201401012@rajalakshmi.edu.in'



ipadress=geocoder.ip('me')
location=ipadress.latlng
res1 = "".join(str(location))



subject = 'EMERGENCY HELP ME'
body ="COORDINATES: Latitude and Longitude  "+str(res1)
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

name ='deepak'  
talk('Are you okay'+name)
print("Are you okay "+name)
talk('                 ')
talk('Are you okay'+name)
print("Are you okay "+name)
talk('                 ')
talk('Are you okay'+name)
print("Are you okay "+name)

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'croot' in command:
                command = command.replace('croot', '')
                print(command)
    except :
        print('NO REPLY')
        talk('I am contacting your family for help please manage untill they send help'+name)
        print("I am contacting your family for help please manage untill they send help "+name)
        print(location)
        print("Sending mail...")
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver,em.as_string())
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'ok' in command:
        talk('Take care  '+name+'  I am here to help you any time')
        print("Take care   "+name+"   I am here to help you any time") 
               
 
    elif 'no' in command:
        talk('I am contacting your family for help please manage untill they send help '+name)
        print("I am contacting your family for help please manage untill they send help "+name)

        print(location)
        print("Sending mail...")
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver,em.as_string())
             
    else:
        talk('I am contacting your family for help please manage untill they send help '+name)
        print("I am contacting your family for help please manage untill they send help "+name)
        print(location)
        print("Sending mail...")
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver,em.as_string())
             

run_alexa()

