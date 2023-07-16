#!/usr/bin/env python
# coding: utf-8

# # alexa-like-virtual-assistant

# In[2]:


import speech_recognition as sr
import pyttsx3#text to speech
import pywhatkit
import datetime
import wikipedia
import pyjokes


# In[1]:


# Speech Recognition Setup


# In[3]:


listener = sr.Recognizer()  # to listen what user says
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("hey priya i am alexa    your virtual assistane, what can i do for you?")
engine.runAndWait()


# In[2]:


# Text-to-Speech Function


# In[16]:


def talk(text):
    engine.say(text)
    engine.runAndWait()


# In[3]:


# Voice Command Recognition


# In[17]:


def take_command():
    command=''
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                #talk(command)
    except:
        pass
    return command


# In[4]:


# Main Function to Run Alexa


# In[25]:


def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('yes, playing'+song)
        print('yes, playing!!'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        reply='current time is ' + time
        print(reply)
        talk(reply)
    elif 'what is' in command:
        person=command.replace('what is','')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'go on a date' in command:
        print('sorry!!! nerd')
        talk('sorry!!! nerd')
    elif 'are you single' in command:
        talk('no i am dating siri, dont be such a despo!!')
        print('no i am dating siri, dont be such a despo!!')
    elif 'joke' in command:
        jokee=pyjokes.get_joke()
        talk(jokee)
        print(jokee)
        
        
    
    
                                              
        
run_alexa()
    


# In[ ]:





# In[ ]:




