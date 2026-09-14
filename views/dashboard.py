import wx
from models.minuteur import Minuteur
from observers.affichage_temps import AffichageTemps
from observers.affichage_etat import AffichageEtat
from observers.barre_progression import BarreProgression
from observers.compteur_sessions import CompteurSessions
from observers.logger_session import LoggerSession


class Dashboard(wx.Frame):

    INTERVALLE_MS = 1000

    def __init__(self, minuteur: Minuteur):
        super().__init__(None, title="Minuteur Pomodoro")
        self._minuteur = minuteur
        self._en_marche = False

        self._panel = wx.Panel(self)
        self._sizer = wx.BoxSizer(wx.VERTICAL)

        self._creer_observateurs()
        self._abonner_observateurs()
        self._creer_boutons()

        self._panel.SetSizer(self._sizer)
        self.Fit()

    def _creer_observateurs(self) -> None:
        # À compléter :
        # Instanciez AffichageEtat, AffichageTemps, BarreProgression,
        # CompteurSessions et LoggerSession
        # Note : les observateurs wx reçoivent self._panel et self._sizer
        # en paramètres pour s'ajouter au layout
        pass

    def _abonner_observateurs(self) -> None:
        # À compléter :
        # Abonnez tous les observateurs au minuteur
        pass

    def _creer_boutons(self) -> None:
        sizer_boutons = wx.BoxSizer(wx.HORIZONTAL)

        self._btn_start = wx.Button(self._panel, label="Démarrer")
        self._btn_pause = wx.Button(self._panel, label="Pause")
        self._btn_reset = wx.Button(self._panel, label="Réinitialiser")
        self._btn_pause.Disable()

        self._btn_start.Bind(wx.EVT_BUTTON, lambda e: self._demarrer())
        self._btn_pause.Bind(wx.EVT_BUTTON, lambda e: self._pause())
        self._btn_reset.Bind(wx.EVT_BUTTON, lambda e: self._reset())

        sizer_boutons.Add(self._btn_start, 0, wx.ALL, 5)
        sizer_boutons.Add(self._btn_pause, 0, wx.ALL, 5)
        sizer_boutons.Add(self._btn_reset, 0, wx.ALL, 5)
        self._sizer.Add(sizer_boutons, 0, wx.CENTER)

    def _demarrer(self) -> None:
        # À compléter :
        # Activez le minuteur et démarrez la boucle _tick()
        # Mettez à jour les boutons
        pass

    def _pause(self) -> None:
        # À compléter :
        # Appelez basculer_pause() sur le minuteur
        # Mettez à jour le texte du bouton
        # Si on reprend, relancez _tick()
        pass

    def _reset(self) -> None:
        # À compléter :
        # Réinitialisez le minuteur
        # Mettez à jour les boutons
        pass

    def _tick(self) -> None:
        # À compléter :
        # Si en marche et pas en pause : appeler minuteur.tick()
        # Planifier le prochain appel avec wx.CallLater()
        pass
