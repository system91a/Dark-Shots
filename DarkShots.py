from Tkinter import *
from random import randint
import random
import DarkShots_action as act

#BUTTON

def names_update():

    global num_players
    global names_entry
    alt_num = num_players
    num_players = int(names_spin.get())

    if (num_players > alt_num):
        names_entry[num_players-1] = Entry(set_names, bd=5, width=40)
        names_entry[num_players-1].pack()
    else:
        names_entry[alt_num-1].destroy()
 

def los_action():
    def next_action():
        global antidote
        h = 0
        for i in range(act.virus_k+1) :
            antidote[i] -= 1
            if (antidote[i] == 0):
                h = 1
                typ = "Antidote"
                action = act.virus[i].end
                expl = ""
                break
        if (h == 0):
            rtyp = randint(1,100)
        else:
            rtyp = 101
        if (rtyp <= 66):
            global cnormal
            if (cnormal == act.normal_k):
                action = "GAME OVER"
                typ = "GAME OVER"
                expl = "GAME OVER"
            else:
                cnormal += 1
                typ = act.normal[cnormal].typ    
                action = act.normal[cnormal].text
                expl = act.normal[cnormal].expl
            
        elif (rtyp <= 74):
            global ceither
            if (ceither == act.either_k):
                action = "GAME OVER"
                typ = "GAME OVER"
                expl = "GAME OVER"
            else:
                ceither += 1
                typ = act.either[ceither].typ    
                action = act.either[ceither].text
                expl = act.either[ceither].expl

        elif (rtyp <= 82):
            global cvirus
            if (cvirus == act.virus_k):
                action = "GAME OVER"
                typ = "GAME OVER"
                expl = "GAME OVER"
            else:
                cvirus += 1
                antidote[cvirus] = randint(10,20)
                typ = act.virus[cvirus].typ    
                action = act.virus[cvirus].text
                expl = act.virus[cvirus].expl

        elif (rtyp <= 90):
            global cbrain
            if (cbrain == act.brain_k):
                action = "GAME OVER"
                typ = "GAME OVER"
                expl = "GAME OVER"
            else:
                cbrain += 1
                typ = act.brain[cbrain].typ    
                action = act.brain[cbrain].text
                expl = act.brain[cbrain].expl

        elif (rtyp <= 98):
            global cdemo
            if (cdemo == act.demo_k):
                action = "GAME OVER"
                typ = "GAME OVER"
                expl = "GAME OVER"
            else:
                cdemo += 1
                typ = act.demo[cdemo].typ    
                action = act.demo[cdemo].text
                expl = act.demo[cdemo].expl

        elif (rtyp <= 100):
            global ccount
            if (ccount == act.count_k):
                action = "GAME OVER"
                typ = "GAME OVER"
                expl = "GAME OVER"
            else:
                ccount += 1
                typ = act.count[ccount].typ    
                action = act.count[ccount].text
                expl = act.count[ccount].expl

        typ_label.config(text=typ)
        action_label.config(text=action)
        expl_label.config(text=expl)
            
    game = Tk()
    game.title("Dark Shots")
    game.geometry("500x250")
    backcol = "black"
    game.configure(background=backcol)
    next_button = Button(game, text="NEXT !", command = next_action, bg="red")
    void_label = Label(game, text="you cant see this", bg = backcol, fg = backcol ,font = 30)
    head_label = Label(game, text="DARK SHOTS", bg = backcol, fg = "red" ,font = 30)
    typ_label = Label(game, text="START", bg = backcol, fg = "yellow" ,font = 30)
    action_label = Label(game, text= "PROST ! ! !", bg = backcol, fg = "white" ,font = 30)
    expl_label = Label(game, text= "Everyone drinks.", bg = backcol, fg = "green" ,font = 30)

    #shuffle
    random.shuffle(act.normal) 
    random.shuffle(act.either) 
    random.shuffle(act.virus) 
    random.shuffle(act.brain) 
    random.shuffle(act.demo) 
    random.shuffle(act.count) 
    
    head_label.pack()
    void_label.pack()
    typ_label.pack()
    action_label.pack()
    expl_label.pack()
    next_button.pack()
    next_button.place(anchor = NW, x= 200, y = 170, width = 100, height = 50)


maxnames = 20
num_players = 0
cnormal = -1
ceither = -1
cvirus  = -1
cbrain  = -1
cdemo   = -1
ccount  = -1
antidote = []

for i in range(act.virus_k+1):
    antidote.append(-1)
    

# Ein set_names erstellen
set_names = Tk()
set_names.title("Set Names")
set_names.geometry("300x300")


names_spin = Spinbox(set_names, from_=0, to=maxnames, command = names_update)

names_entry =  []
for i in range(maxnames):
    names_entry.append(0)    

los_button = Button(text="Los geht's!!!", command = los_action, bg="red")

los_button.pack()
names_spin.pack()

# In der Ereignisschleife auf Eingabe des Benutzers warten.
set_names.mainloop()
