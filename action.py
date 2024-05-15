from sndhdr import whathdr
import subprocess
from text_to_speech import text_to_speech
import text_to_speech
import datetime
import webbrowser
import weather
from weather import get_weather
import os
import subprocess

def Action(data):
    user_data =""
    if data is not None:
        user_data = data.lower()
       
    if "what is your name" in   user_data :
      text_to_speech.text_to_speech("my name is virtual Assistant")  
      return "my name is virtual Assistant"


    elif "hello" in user_data  or "hye" in user_data or "hay" in user_data: 
        text_to_speech.text_to_speech("Hey sir, How i can  help you !")  
        return "Hey mam, How i can  help you !" 

    elif "how are you" in user_data:
            text_to_speech.text_to_speech("I am doing great these days mam") 
            return "I am doing great these days mam"   
    
    elif "kaalai vanakkam" in user_data or "vanakkam"  in user_data:
            text_to_speech.text_to_speech("vanakkam amma") 
            return "vanakkam amma"  
    
    # elif "who is project guide" in user_data or "guide"  in user_data:
    #         text_to_speech.text_to_speech("My project guideNithyasri amma") 
    #         return "Nithiyasri amma"  
    

    elif "thankyou" in user_data or "thank" in user_data:
           text_to_speech.text_to_speech("its my pleasure mam to stay with you")
           return "its my pleasure mam to stay with you"      

    # elif "good morning" in user_data:
    #        text_to_speech.text_to_speech("Good morning mam, i think you might need some help")
    #        return "Good morning mam, i think you might need some help"   
    # elif "good afternoon" in user_data:
    #        text_to_speech.text_to_speech("Good morning mam, i think you might need some help")
    #        return "Good afternoon, i think you might need some help"   
    # elif "good evening" in user_data:
    #        text_to_speech.text_to_speech("Good morning mam, i think you might need some help")
    #        return "Good evening mam, i think you might need some help"   

    elif "good morning" in user_data or "good afternoon" in user_data or "good evening" in user_data or "namaskaram" in user_data:
        text_to_speech.text_to_speech("Good " + user_data.split()[1] + "! How may I assist you?")
        return "Good " + user_data.split()[1] + "! How may I assist you?"


    elif "time now" in user_data or "what is time now" in user_data or "time" in user_data:
          current_time = datetime.datetime.now()
          Time = (str)(current_time)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          text_to_speech.text_to_speech(Time)
          return str(Time) 

    elif "shutdown" in user_data or "quit" in user_data:
            text_to_speech.text_to_speech("ok mam")
            return "ok mam"  

    elif "play music" in user_data or "song" in user_data or "music open cheiyum" in user_data or "music theravandi" in user_data:
        webbrowser.open("https://gaana.com/")   
        text_to_speech.text_to_speech("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    # elif 'open google panlingua' in user_data or 'google open'  in user_data:
    #     url = 'https://google.com/'
    #     webbrowser.get().open(url)
    #     text_to_speech.text_to_speech("google opened mam")  
    #     return "google opened mam"
    
    elif 'google teravandi' in user_data or 'open google'  in user_data or 'google open cheiyum'  in user_data or 'google open'  in user_data or  'google'  in user_data:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        text_to_speech.text_to_speech(" google తెరవండి")  
        return "google తెరవండి"


  
    elif 'youtube' in user_data or "youtube open cheiyum" in  user_data or "youtube teravandi" in  user_data:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        text_to_speech.text_to_speech("YouTube opened mam") 
        return "YouTube opened mam"
    

    elif 'skillrack' in user_data or 'open skillrack'in  user_data or 'skillrack teravandi'in  user_data or 'skillrack open cheiyum'in  user_data:
         url = 'https://skillrack.com/'
         webbrowser.get().open(url)
         text_to_speech.text_to_speech("skillrack opened mam") 
         return "Skillrack opened mam"

    
    # # elif 'open vscode' in user_data or "visualstudio" in  user_data or "vscode" in user_data:
    #     url = 'C:\Users\kavis\AppData\Local\Programs\Microsoft VS Code\Code.exe'
    #     webbrowser.get().open(url)
    #     text_to_speech.text_to_speech("Vscode opened mam") 
    #     return "Vscode opened mam"      
    
    elif 'weather' in user_data :
       ans   = whathdr.weather()
       text_to_speech.text_to_speech(ans) 
       return ans

    elif 'music from my laptop' in user_data or 'laptop music' in user_data or 'laptop music teravandi' in user_data or 'laptop music open cheiyum' in user_data:
        url = 'D:\Music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        text_to_speech.text_to_speech("songs playing...")
        return "songs playing..." 
    
    elif 'open notepad' in user_data or 'notepad teravandi' in user_data  or 'notepad open cheiyum' in user_data:
        subprocess.Popen(['notepad.exe'])
        text_to_speech.text_to_speech("Opening Notepad!")
        return "Opening Notepad!"
    
    elif 'open word' in user_data or 'microsoft word' in user_data or 'word open cheiyum' in user_data or ' word teravandi' in user_data:
        word_path = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
        subprocess.Popen([word_path])
        text_to_speech.text_to_speech("Opening Microsoft Word!")
        return "Opening Microsoft Word!"
    

  

    # elif "open camera" in user_data:
    #      subprocess.Popen("start microsoft.windows.camera:", shell=True)
    #      text_to_speech.text_to_speech("Opening camera...")
    #      return "Opening camera..."
    
    elif "open camera" in user_data or "camera open cheiyum" in user_data or "camera teravandi" in user_data:
         subprocess.Popen("start microsoft.windows.camera:", shell=True)
         text_to_speech.text_to_speech("Opening camera...")
         return "Opening camera..."


    elif "send email" in user_data:
        # Specify the command to open the email application on your laptop
        subprocess.Popen("email_command_here")
        text_to_speech.text_to_speech("Opening email application...")
        return "Opening email application..."
    
    # elif 'calendar open' in user_data or 'calendar open cheiyum' in user_data :
    #    subprocess.Popen(['start', 'cal'])
    #    text_to_speech.text_to_speech("Opening Calendar!")
    #    return "Opening Calendar!"


    # elif 'open calendar' in user_data:
    #     subprocess.Popen(['start', 'shell:AppsFolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App'])
    #     text_to_speech.text_to_speech("Opening Calendar!")
    #     return "Opening Calendar!"

    # elif "nandi" in user_data:
    #     text_to_speech.text_to_speech("നന്ദി, മാമ, നിങ്ങളുടെ സഹായത്തിന് സന്തോഷമാണ്")
    #     return "നന്ദി, മാമ, നിങ്ങളുടെ സഹായത്തിന് സന്തോഷമാണ്" 


    else:
        text_to_speech.text_to_speech( "i'm unable to understand!")
        return "i'm unable to understand!"      



        
    
          


















