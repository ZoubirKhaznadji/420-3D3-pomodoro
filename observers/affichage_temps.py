import wx
from observers.observer import Observateur


class AffichageTemps(Observateur):

    def __init__(self, parent, sizer):
        self._label = wx.StaticText(parent, label="25:00")
        font = self._label.GetFont()
        font.SetPointSize(48)
        font.MakeBold()
        self._label.SetFont(font)
        sizer.Add(self._label, 0, wx.ALL | wx.CENTER, 10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant depuis sujet.get_donnees()
        # Calculez minutes et secondes
        # Mettez à jour le label au format "MM:SS"
        pass
