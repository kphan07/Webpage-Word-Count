import requests
import re
import tkinter as tk
import validators
from tkinter import *

def getwordcount(url, word):
    page = requests.get(url).text
    page.lower()
    text=re.findall(word.lower(), page)
    return text

def searchurl():
    url_en = url.get()
    word_en = word.get()
    totaltext = getwordcount(url_en, word_en)

    lbl_1.config(text='%d ' %len(totaltext) + 'instances of ' + word_en + ' were found')
    lbl_1.update()

def error_handling():
    url_en = url.get()
    word_en = word.get()

    url_en=url_en.lower()
    word_en=word_en.lower()

    if not validators.url(url_en):
        window = tk.Toplevel(master)
        window.geometry('300x50')
        window.title('Error')

        if url_en[:7] != 'http://' and url_en[:8] != 'https://':
            lbl_b=Label(window,text='Please append "http://" or "https://" to the URL')

        else:
            lbl_b = Label(window, text='Please enter a valid URL')

        lbl_b.pack(side='top')
        OK_b = Button(window, text='OK', command=window.destroy)
        OK_b.pack(side='bottom')

    elif word_en == '':
        window = tk.Toplevel(master)
        window.geometry('300x50')
        window.title('Error')

        lbl_b = Label(window, text='Please enter a word')
        lbl_b.pack(side='top')

        OK_b = Button(window, text='OK', command=window.destroy)
        OK_b.pack(side='bottom')

    else:
        searchurl()

master=Tk()
frame=Frame(master)
frame.pack()

lbl=Label(frame,text='Enter URL:')
lbl.grid(column=0,row=0)

lblw=Label(frame,text='Enter Word:')
lblw.grid(column=0,row=10)

lbl_1=Label(frame,text='')
lbl_1.grid(column=20,row=60)

url=Entry(frame,width=50)
url.grid(column=20,row=0)

word=Entry(frame,width=50)
word.grid(column=20,row=10)

search=Button(frame,text='Search',command=error_handling)
search.grid(column=20,row=100)

quit=Button(frame,text='Quit',command=frame.quit)
quit.grid(column=0,row=100)

frame.master.geometry('450x100')
frame.master.title('URL Word Count')
master.mainloop()