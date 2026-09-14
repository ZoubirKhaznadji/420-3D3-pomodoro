import tkinter as tk
from models.minuteur import Minuteur
from observers.affichage_temps import AffichageTemps
from observers.affichage_etat import AffichageEtat
from observers.barre_progression import BarreProgression
from observers.compteur_sessions import CompteurSessions
from observers.logger_session import LoggerSession


class Dashboard(tk.Tk):

    INTERVALLE_MS = 1000

    def __init__(self, minuteur: Minuteur):
        super().__init__()
        self.title("Minuteur Pomodoro")
        self.resizable(False, False)
        self._minuteur = minuteur
        self._en_marche = False
        minuteur = Minuteur()
        

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_boutons()

    def _creer_observateurs(self) -> None:
        # À compléter :
        # Instanciez AffichageEtat, AffichageTemps, BarreProgression,
        self._minuteur = Minuteur()
        etat = AffichageEtat()
        self._minuteur.abonner(etat)
        temps = AffichageTemps()
        self._minuteur.abonner(temps)
        barre = BarreProgression()
        self._minuteur.abonner(barre)
        logger = LoggerSession("pomodoro.log")
        self._minuteur.abonner(logger)
        compteur = CompteurSessions()
        self._minuteur.abonner(compteur)


    def _abonner_observateurs(self) -> None:
        # À compléter :
        # Abonnez tous les observateurs au minuteur
        etat = AffichageEtat()
        self._minuteur.abonner(etat)
        temps = AffichageTemps()
        self._minuteur.abonner(temps)
        barre = BarreProgression()
        self._minuteur.abonner(barre)
        logger = LoggerSession("pomodoro.log")
        self._minuteur.abonner(logger)
        compteur = CompteurSessions()
        self._minuteur.abonner(compteur)

    def _creer_boutons(self) -> None:
        frame = tk.Frame(self)
        frame.pack(pady=10)

        self._btn_start = tk.Button(frame, text="Démarrer", command=self._demarrer)
        self._btn_start.pack(side=tk.LEFT, padx=5)

        self._btn_pause = tk.Button(
            frame, text="Pause", command=self._pause, state=tk.DISABLED
        )
        self._btn_pause.pack(side=tk.LEFT, padx=5)

        self._btn_reset = tk.Button(frame, text="Réinitialiser", command=self._reset)
        self._btn_reset.pack(side=tk.LEFT, padx=5)

    def _demarrer(self) -> None:
        # À compléter :
        # Activez le minuteur et démarrez la boucle _tick()
        # Mettez à jour les boutons
        self.en_marche = True
        self.en_pause = False
        self.btn_start.config(state=tk.DISABLED)
        self.btn_pause.config(state=tk.NORMAL)
        self.tick()

    def _pause(self) -> None:
        # À compléter :
        # Appelez basculer_pause() sur le minuteur
        # Mettez à jour le texte du bouton
        # Si on reprend, relancez _tick()
        if self.en_pause:
            self.en_pause = False
            self.btn_pause.config(text="Pause")
            self.tick()
        else:
            self.en_pause = True
            self.btn_pause.config(text="Reprendre")

    def _reset(self) -> None:
        # À compléter :
        # Réinitialisez le minuteur
        # Mettez à jour les boutons
        DUREE_TRAVAIL = 25 * 60
        self.en_marche = False
        self.en_pause = False
        self.temps_restant = DUREE_TRAVAIL
        self.btn_start.config(state=tk.NORMAL)
        self.btn_pause.config(state=tk.DISABLED)
        self.btn_pause.config(text="Pause")
        self.label_etat.config(text="Travail", fg="black")
        self.label_temps.config(text="25:00")
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 300, 20, fill="green", outline="")

    def _tick(self) -> None:
        # À compléter :
        # Si en marche et pas en pause : appeler minuteur.tick()
        # Planifier le prochain appel avec self.after()
        if self.en_marche and not self.en_pause :
            self._minuteur.tick()
        self._fenetre.after(1000, self.tick)
