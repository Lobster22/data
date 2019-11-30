import requests
import tkinter as tk
import re

def makePatt(lang):
    pattern = lang[0] + '[a-z]'
    return pattern

def notSure(data, lang):
    lol = []
    pattern = makePatt(lang)
    for l in data:
        re.findall(pattern, l["name"])

def getOneLang(data, thisLang):
    for lang in data:
        if lang['name'] == thisLang:
            return lang
        else:
            return notSure(data, thisLang)


def getAllLang(data): 
    lol = []
    for lang in data:
        lol.append(lang["name"])
    return lol


def getData(lang):
    r = requests.get('https://lobster22.github.io/data/lang.json')
    data = r.json()

    if lang == '':
        label['text'] = str(getAllLang(data))
    else:
        label['text'] = getOneLang(data, lang)


root = tk.Tk()

window = tk.Canvas(root, height=500, width=600)
window.pack()

# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR-wK0V7jbZQOg6Kw8HFaOjMOS8o7NHj_54c8lV5Z4Mtnvavgs&s

#background_image = tk.PhotoImage(file='')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,
                   command=lambda: getData(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
