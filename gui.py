# from tkinter import Tk, Label, LabelFrame, Canvas, Text , Entry, CENTER, Button, SOLID, END
# from PIL import Image , ImageTk
# import tkinter 
# from tkinter import END 
# import speech_to_text 
# import action
# from googletrans import Translator


# root = Tk()
# root.title("AI Assistant")
# root.geometry("550x675")
# root.resizable(False, False)
#         #background color
# root.config(bg="#CAFF70") 
# ##Initialize user_val
# user_val=""

# #ask fun
# def ask():
#     global user_val 
#     user_val = speech_to_text.speech_to_text()
#     if user_val:
#           bot_val = action.Action(user_val)
#           text.insert(END , 'User--->'+ user_val+"\n")
#           if bot_val is not  None:
#         #   if bot_val != None:
#             text.insert(END , "BOT <----"+ str(bot_val)+ "\n")
#           if bot_val == "ok sir":
#               root.destroy() 
          
# ##send fun
# def send():
#     global user_val 
#     send_text = entry.get() 
#     bot = action.Action(user_val)
#     text.insert(END , 'User--->'+ send_text+"\n")
#     if bot!= None:
#         text.insert(END , "BOT <----"+str(bot)+"\n")
#     if bot == "ok sir":
#         root.destroy()   

# ## del_text fun
# def del_text():
#    text.delete('1.0' , "end")




# # frame
# frame = LabelFrame(root, padx= 100, pady= 7, borderwidth= 3, relief ="raised")
# frame.config(bg="#97FFFF")
# frame.grid(row = 0, column= 1, padx= 55, pady= 10)

# # text table 

# text_label = Label(frame , text="SMART PANLINGUA", font=("dancing script", 14 , "bold") ,bg="#356696")
# text_label.grid(row =0, column =0, padx =20 , pady =10)

# #image
# image = ImageTk.PhotoImage(Image.open(r"C:\Users\kavis\Downloads\assitant.png"))
# image_label= Label(frame , image=image)
# image_label.grid(row=1, column= 0,pady= 20)


# #ADDING SOME TEXT
# text = Text(root, font= ('courier 10 bold'), bg = "#356696")
# text.grid(row= 2, column= 0 )
# text.place(x = 100, y = 375, width = 375, height = 100)


# #another box entry widgit
# entry = Entry(root, justify= CENTER)
# entry.place(x= 100, y = 500, width= 350, height = 30)



# #button creation

# Button1= Button(root,text = "ASK" , bg = "#8DEEEE" , pady = 16, padx = 40, borderwidth = 3, relief= SOLID, command = ask)
# Button1.place(x = 70, y= 575)


# Button2= Button(root,text = "SEND" , bg = "#8DEEEE" , pady = 16, padx = 40, borderwidth = 3, relief= SOLID, command = send)
# Button2.place(x = 400, y= 575)

# Button3= Button(root,text = "DELETE" , bg = "#8DEEEE" , pady = 16, padx = 40, borderwidth = 3, relief= SOLID, command = del_text)
# Button3.place(x = 225, y= 575)



# root.mainloop()


































from tkinter import Tk, Label, LabelFrame, Canvas, Text , Entry, CENTER, Button, SOLID, END
from PIL import Image , ImageTk
import tkinter 
from tkinter import END 
import speech_to_text 
import action
from googletrans import Translator

translator = Translator()

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#CAFF70") 
user_val=""

def ask():
    global user_val 
    user_val = speech_to_text.speech_to_text()
    if user_val:
        bot_val = action.Action(user_val)
        text.insert(END , 'User--->'+ user_val+"\n")
        if bot_val is not None:
            translated_response = translator.translate(bot_val, src='en', dest='ta')
            text.insert(END , "BOT <----"+ str(translated_response.text)+ "\n")
        if bot_val == "ok sir":
            root.destroy() 

def send():
    global user_val 
    send_text = entry.get() 
    bot = action.Action(user_val)
    text.insert(END , 'User--->'+ send_text+"\n")
    if bot!= None:
        translated_response = translator.translate(bot, src='en', dest='ta')
        text.insert(END , "BOT <----"+str(translated_response.text)+"\n")
    if bot == "ok sir":
        root.destroy()   

def del_text():
   text.delete('1.0' , "end")

frame = LabelFrame(root, padx= 100, pady= 7, borderwidth= 3, relief ="raised")
frame.config(bg="#97FFFF")
frame.grid(row = 0, column= 1, padx= 55, pady= 10)

text_label = Label(frame , text="SMART PANLINGUA", font=("dancing script", 14 , "bold") ,bg="#356696")
text_label.grid(row =0, column =0, padx =20 , pady =10)

image = ImageTk.PhotoImage(Image.open(r"C:\Users\kavis\Downloads\assitant.png"))
image_label= Label(frame , image=image)
image_label.grid(row=1, column= 0,pady= 20)

text = Text(root, font= ('courier 10 bold'), bg = "#356696")
text.grid(row= 2, column= 0 )
text.place(x = 100, y = 375, width = 375, height = 100)

entry = Entry(root, justify= CENTER)
entry.place(x= 100, y = 500, width= 350, height = 30)

Button1= Button(root,text = "ASK" , bg = "#8DEEEE" , pady = 16, padx = 40, borderwidth = 3, relief= SOLID, command = ask)
Button1.place(x = 70, y= 575)

Button2= Button(root,text = "SEND" , bg = "#8DEEEE" , pady = 16, padx = 40, borderwidth = 3, relief= SOLID, command = send)
Button2.place(x = 400, y= 575)

Button3= Button(root,text = "DELETE" , bg = "#8DEEEE" , pady = 16, padx = 40, borderwidth = 3, relief= SOLID, command = del_text)
Button3.place(x = 225, y= 575)

root.mainloop()










