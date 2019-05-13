from tkinter import *
from random import randint

#BUTTON


# Ein Fenster erstellen
fenster = Tk()
fenster.title("Dark Shots")
fenster.geometry("300x300")


player_spin = Spinbox(fenster, from_=0, to=20)



player_spin.pack()

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()
