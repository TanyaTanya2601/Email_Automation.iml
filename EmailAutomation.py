import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3


listenser = sr.Recognizer()
tts= pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print("Program is listening..")
        voice = listenser.listen(source)
        data= listenser.recognize_google(voice)
        print(data)
        return data.lower()


dict= {"tanya":"tanyashayan26@gmail.com"}

def send_mail(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("eautomation143@gmail.com","grdj szlv rsuu xivs")
    email = EmailMessage()
    email["From"]= "eautomation143@gmail.com"
    email["To"] = receiver
    email["Subject"]= subject
    email.set_content(body)
    server.send_message(email)

def main_poc():
    talking_tom("Who do you want to send this email?")
    name= mic()
    receiver = dict[name]
    talking_tom("Speak the subject of the email")
    subject =  mic()
    talking_tom("Speak the message of the email")
    body = mic()
    send_mail(receiver, subject, body)
    print("Your email has been sent.")

main_poc()





