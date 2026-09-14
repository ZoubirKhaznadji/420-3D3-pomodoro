import tkinter as tk
from observers.observer import Observateur


class AffichageTemps(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="25:00", font=("Arial", 48, "bold"))
        self._label.pack(pady=10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant depuis sujet.get_donnees()
        sujet.get_donnees()
        donnees = sujet.get_donnees()
        donnees = donnees["temps_restant"]
        # Calculez minutes et secondes
        # Mettez à jour le label au format "MM:SS"
        minutes = self.temps_restant // 60
        secondes = self.temps_restant % 60
        self.label_temps.config(text=f"{minutes:02d}:{secondes:02d}")
