from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from tkinter import *
from googletrans import Translator


root = Tk()
root.title("speechConverter.com")
root.geometry("700x400")




def speaking_sound():
    engine = pyttsx3.init()
    engine.say(my_entry.get())

    engine.runAndWait() 
 
 
 
def text_to_speach():
    # language = 'es'
    # output = gTTS(text=my_entry_trans.get(), lang=language, slow=False) 
    
    traslator = Translator()
    out = traslator.translate(my_entry_trans.get(), dest='es')
    translation_label = Label(root, text=out.text, fg='white')
    translation_label.grid(column=14, row=7, columnspan=2)
    
 
 
    
# def translator_text():
#     traslator = Translator()
#     out = traslator.translate(my_entry_trans.get(), dest='es')
    







english= Label(text='Audio', fg='white')
english.grid(column=10, row=3, columnspan=1, rowspan=2)

my_entry = Entry(root, fg='grey')
my_entry.grid(column=11, row=4, columnspan=2)

my_entry_trans = Entry(root, fg='grey')
my_entry_trans.grid(column=16, row=4, columnspan=2)


spanish = Label(text='Spanish', fg='white')
spanish.grid(column=20, row=3, columnspan=1, rowspan=2)

speak = Button(root, text='Speak', bg='black', fg='white', command=speaking_sound)
speak.grid(column=13, row=5, columnspan=2)

translation_btn = Button(root, text='Translate', bg='black', fg='white', command=text_to_speach)
translation_btn.grid(column=13, row=6, columnspan=2)





root.mainloop()