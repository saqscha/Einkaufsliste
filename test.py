

import tkinter as tk
from tkinter import Entry



color1 = '#B7B7A4'
color2 = '#DDBEA9'
color3 = '#CB997E'

root = tk.Tk()
root.configure(bg=color2)


root.title("Einkaufsliste")
root.geometry("400x400")
root.minsize(width=200, height=200)

label_title = tk.Label(root, text="Deine persönliche Einkaufsliste:",
                       bg=color1, borderwidth="0", font=("Helvetica", 16))
label_title.pack(fill="x")

label_que = tk.Label(root, text="Was möchtest du einkaufen?", bg=color2, font=("Helvetica", 16))
label_que.pack(side="bottom")

article_list = []


t = tk.Text(root, bg=color2)
t.config(state="normal", borderwidth="0", font=("Helvetica", 14))

def tb():

    arlist = sorted(article_list, key=str.lower)
    t.delete('1.0', tk.END)
   
    
    
    for x in arlist:
        t.insert(tk.END, "➡ " + x + '\n')
        t.pack(side="top")






def articles(e):
    
    ar_i = entry.get()
    article_list.append(ar_i)
    entry.delete(0, tk.END)
    tb()



entry = Entry(root, borderwidth="0", bg=color3)
entry.pack(side="bottom", fill="x")
entry.bind('<Return>', articles)







    



        


root.mainloop()

print(article_list)