import tkinter as tk
from observers.observer import Observateur



class AffichageEtat(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="Travail", font=("Arial", 16, "bold"))
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez etat depuis sujet.get_donnees()
        sujet.get_donnees()
        donnees = sujet.get_donnees()
        donnees = donnees["etat"]
        # Mettez à jour le label
        # Couleur : noir pour "Travail", bleu pour "Pause"
        self.label_etat.config(text="Travail", fg="blue")
