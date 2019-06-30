
#On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.


# On importe Tkinter
from tkinter import *
import sys
import os
import first_script
import textToSpeech

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="SmartBot")

# On affiche le label dans la fenêtre
champ_label.pack()
#boutons
bouton_ExecuteP = Button(fenetre, text="Name", fg='Blue', command=).pack(side=LEFT, padx=5, pady=5)
bouton_ExecuteP.pack()
#bouton_ExecuteP = Button(fenetre, text="Name", fg='Blue')
#bouton_ExecuteP.pack()
#bouton_ExecuteT = Button(fenetre, text="Tem", fg='red', command=textToSpeech.recognize_speech_from_mic(first_script.m, first_script.r))
#bouton_ExecuteT.pack()
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
