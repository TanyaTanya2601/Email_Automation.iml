#  Voice-Based Email Automation using Python

## Overview

Voice-Based Email Automation is a Python application that allows users to send emails completely through voice commands. The application listens to the user's speech, converts it into text using Speech Recognition, and sends an email through Gmail's SMTP server. It also provides voice feedback using a text-to-speech engine, creating a hands-free email experience.

This project demonstrates the integration of Speech Recognition, Text-to-Speech (TTS), Email Automation, and Python networking libraries to build an intelligent voice assistant.



# Libraries And Technologies 

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* smtplib
* EmailMessage


# Workflow

```
User Speaks

↓

Speech Recognition

↓

Recipient Identification

↓

Subject Recognition

↓

Body Recognition

↓

Email Creation

↓

SMTP Authentication

↓

Email Sent Successfully
```

---

# Code Explanation

## 1. Import Libraries

```python
import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3
```

### Purpose

* **smtplib** connects to Gmail's SMTP server.
* **speech_recognition** converts voice into text.
* **EmailMessage** creates the email.
* **pyttsx3** converts text into speech.

---

## 2. Speech Recognizer

```python
listener = sr.Recognizer()
```

The recognizer captures audio from the microphone and converts it into text using Google's Speech Recognition service.

---

## 3. Text-to-Speech Engine

```python
tts = pyttsx3.init()
```

The TTS engine provides voice prompts such as:

* "Who do you want to send this email?"
* "Speak the subject."
* "Speak the message."

---

## 4. Voice Output Function

```python
def talking_tom(text):
    tts.say(text)
    tts.runAndWait()
```

This function converts any text into spoken audio.

---

## 5. Voice Input Function

```python
def mic():
    with sr.Microphone() as source:
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        return data.lower()
```

### Working

1. Activates the microphone.
2. Records the user's speech.
3. Sends audio to Google's Speech Recognition API.
4. Returns the recognized text in lowercase.

---

## 6. Contact Dictionary

```python
contacts = {
    "tanya": "tanyashayan26@gmail.com"
}
```

Instead of asking users to speak an email address, the application maps a spoken name to an email address.

Example:

```
User says:

"Tanya"

↓

Program finds

tanyashayan26@gmail.com
```

---

## 7. Sending Email

```python
server = smtplib.SMTP("smtp.gmail.com", 587)
```

The application connects to Gmail's SMTP server using port **587**, enables TLS encryption, logs in to the sender's account, creates an email message, and sends it to the recipient.

---

## 8. Email Creation

```python
email = EmailMessage()

email["From"] = sender
email["To"] = receiver
email["Subject"] = subject

email.set_content(body)
```

The `EmailMessage` class creates a properly formatted email with sender, recipient, subject, and body.

---

## 9. Main Program Flow

```text
Start

↓

Ask recipient

↓

Listen for recipient name

↓

Find email address

↓

Ask for subject

↓

Listen for subject

↓

Ask for message

↓

Listen for message

↓

Create email

↓

Connect to Gmail SMTP

↓

Send email

↓

Success message

↓

Exit
```

---

# Gmail SMTP Configuration

The project uses Gmail's SMTP server.

| Setting     | Value          |
| ----------- | -------------- |
| SMTP Server | smtp.gmail.com |
| Port        | 587            |
| Encryption  | TLS            |

---

The program will:

1. Ask for the recipient.
2. Listen for the recipient's name.
3. Ask for the email subject.
4. Listen for the subject.
5. Ask for the message.
6. Send the email.

---

<img width="1238" height="410" alt="image" src="https://github.com/user-attachments/assets/8fb4027a-f742-4534-b488-ba50f437e132" />





