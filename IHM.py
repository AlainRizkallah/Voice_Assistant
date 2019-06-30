
#On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.


# On importe Tkinter
from tkinter import *
from functools import partial
import sys
import os
from textToSpeech import recognize_speech_from_mic

# On importe speech_recognition et on initie le micro
import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()
m = sr.Microphone()
answer= ['empty']
# On crée une fenêtre, racine de notre interface
fenetre = Tk()

def load():
    answer[0]=recognize_speech_from_mic(r,m)
def quitfenetre():
    fenetre.quit

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="SmartBot")

# On affiche le label dans la fenêtre
champ_label.pack()
#boutons
bouton_ExecuteP = Button(fenetre, text="Record", fg='Blue', command=load)
bouton_ExecuteP.pack(side=LEFT, padx=5, pady=5)
bouton_ExecuteP.pack()
#bouton_ExecuteP = Button(fenetre, text="Name", fg='Blue')
#bouton_ExecuteP.pack()
#bouton_ExecuteT = Button(fenetre, text="Tem", fg='red', command=textToSpeech.recognize_speech_from_mic(first_script.m, first_script.r))
#bouton_ExecuteT.pack()
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
