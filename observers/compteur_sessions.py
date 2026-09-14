import tkinter as tk
from observers.observer import Observateur


class CompteurSessions(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(
            parent,
            text="Sessions complétées : 0",
            font=("Arial", 12)
        )
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez sessions_completees depuis sujet.get_donnees()
        
        DUREE_PAUSE = 5 * 60
        sujet.get_donnees()
        donnees = sujet.get_donnees()
        donnees = donnees["sessions_completees"]

        
        # Mettez à jour le label
        if self.label_etat.cget("text") == "Travail":
                self.sessions_completees += 1
                self.label_sessions.config(
                    text=f"Sessions complétées : {self.sessions_completees}"
                )
                self.label_etat.config(text="Pause", fg="blue")
                self.temps_restant = DUREE_PAUSE
