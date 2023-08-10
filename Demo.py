import os
import openai
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import YanAPI

class GPT:
    def __init__(self,key,lang="en-US"):
        openai.api_key = key
        self.lang = lang
        
    def speech_to_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Nói gì đi...")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language=self.lang)
            print("You said: ", text)
            return text
        except: 
            return ""

    def text_to_speech(self,text):
        
        tts = gTTS(text=text, lang=self.lang)
        tts.save('output.mp3')
        YanAPI.upload_media_music('output.mp3')
        YanAPI.sync_play_music('output.mp3')
        YanAPI.delete_media_music('output.mp3')
        
        

    def ask_gpt(self,question):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            timeout=5

        )
        answer = response.choices[0].text.strip()
        return answer
    
    def Run(self):
        endList = ['finished','finish','end','goodbye','bye','stop','kết thúc']
        while True:
                user_input = self.speech_to_text() 
                if len(user_input)!=0:
                    if user_input.lower() in endList:
                        print("Bot: Goodbye!")
                        self.text_to_speech('Goodbye')
                        break
                    elif user_input.lower() == 'repeat again':
                        self.text_to_speech(bot_response)
                    else:
                        try:
                            bot_response = self.ask_gpt(user_input)
                            print("Bot: " + bot_response)
                            self.text_to_speech(bot_response)
                        except:
                            None
with open('apikey.txt') as f:
    key = f.read()
gpt = GPT(key,lang="vi") #,lang="en-US"s
gpt.Run()
