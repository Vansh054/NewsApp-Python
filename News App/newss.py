import pywhatkit 
from PIL import Image,ImageTk
from tkinter import *
import requests
from tkinter import messagebox

def fetchnews(country_code,country_name):
    response = requests.get("https://newsapi.org/v2/top-headlines?country="+country_code+"&apiKey=bdc912d442614e15846f1804f1b751d8")
    data = response.json()
    articles = data["articles"]
    headlines = ''
    counter = 1
    for a in articles:
        headlines = headlines + str(counter) + "." + a['title'] + '\n'
        counter = counter + 1
    
    if len(articles) == 0:
        messagebox.showinfo('Information','No Headlines Found for this {}'.format(country_name))
    else:
        newss['text'] = headlines
        


def fetchcountrycode():
    country = country_name.get()
    response = requests.get("https://api.printful.com/countries")
    data = response.json()
    result = data['result']
    cc = ''
    for r in result:
        if r['name'].lower() == country.lower():
            cc = r['code'].lower()
    
    if cc == '': 
        messagebox.showerror('Error', 'Country not found {}'.format(country))
    else: 
        fetchnews(cc,country)


root = Tk()
root.title('ZEE News')
root.geometry('600x450')
bg = ImageTk.PhotoImage(file="bg.png")
bgimage = Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
country_name = StringVar()
country_entry = Entry(root,textvariable=country_name,bd=5)
country_entry.place(x=225,y=50)
btn = Button(root, text='', font='Times 20 bold', bg='white',
                 fg='white', height=1, width=4, command=lambda: fetchcountrycode())
btn.place(x=250,y=100)
newss = Label(root,text='',bg='white',fg='black')
newss.place(x=150,y=200)
root.mainloop()

