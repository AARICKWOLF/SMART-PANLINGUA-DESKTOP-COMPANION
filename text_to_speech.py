## IN THIS I HAVE TO INSTALL THE pip install pyttsx3 FOR THE "CONVERSION OF TEXT TO SPEECH"
import pyttsx3
def text_to_speech(text):
     engine = pyttsx3.init()
     rate = engine.getProperty('rate')
     engine.setProperty('rate', 'rate-70')
     engine.say(text)
     engine.runAndWait()

#text_to_speech("hello world")


