## for this first i install the SpeechRecognition==3.8.1 in the CMD 
## next pip install PyAudio==0.2.11  in CMD 
## FOR THE ABOVE pyaudio i didn't install it so i install the  Microsoft C++ Build Tools 


# import speech_recognition as sr

# def speech_to_text():
#       r =  sr.Recognizer()
#       with sr.Microphone() as source:
#            audio = r.listen(source) # methord 
#       try:
#           #  voice_data = ""
#            voice_data = r.recognize_google(audio)
#            return voice_data
#       except sr.UnknownValueError:
#           #     print("error")
#             print("Error: Could not understand audio")
#             return ""
#       except sr.RequestError:
#               print("No internet connection. please turn on you internet")  
#               return ""




# import speech_recognition as sr

# def speech_to_text(language='en-US'):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)  # Method
#     try:
#         voice_data = r.recognize_google(audio, language=language)
#         return voice_data
#     except sr.UnknownValueError:
#         print("Error: Could not understand audio")
#         return ""
#     except sr.RequestError:
#         print("No internet connection. Please turn on your internet")
#         return ""
# voice_data_tamil = speech_to_text(language='ta-IN')
# print("You said (Tamil):", voice_data_tamil)

# voice_data_english = speech_to_text(language='en-US')
# print("You said (English):", voice_data_english)







import speech_recognition as sr

def speech_to_text(language='en-US'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)  # Method
    try:
        voice_data = r.recognize_google(audio, language=language)
        return voice_data
    except sr.UnknownValueError:
        print("Error: Could not understand audio")
        return ""
    except sr.RequestError:
        print("No internet connection. Please turn on your internet")
        return ""

