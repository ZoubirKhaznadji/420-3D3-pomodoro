import tkinter as tk
from observers.observer import Observateur


class BarreProgression(Observateur):

    
    def __init__(self, parent):
        self._canvas = tk.Canvas(parent, width=300, height=20, bg="white")
        self._canvas.pack(pady=10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant et duree_totale depuis sujet.get_donnees()
        DUREE_TRAVAIL = 25 * 60   # 25 minutes en secondes
        DUREE_PAUSE = 5 * 60      # 5 minutes en secondes
        sujet.get_donnees()
        donnees = sujet.get_donnees()
        donnees = donnees["temps_restant"]
        donnees = donnees["duree_totale"]
        
        
        # Calculez la largeur proportionnelle (300 * temps_restant / duree_totale)
        if self.en_pause is False and self.label_etat.cget("text") == "Travail":
            duree_totale = DUREE_TRAVAIL
        else:
            duree_totale = DUREE_PAUSE
            largeur = int(300 * self.temps_restant / duree_totale)

        # Effacez le canvas et dessinez le rectangle
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, largeur, 20, fill="green", outline="")
