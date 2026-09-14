import wx
from observers.observer import Observateur


class AffichageEtat(Observateur):

    def __init__(self, parent, sizer):
        self._label = wx.StaticText(parent, label="Travail")
        font = self._label.GetFont()
        font.SetPointSize(16)
        font.MakeBold()
        self._label.SetFont(font)
        sizer.Add(self._label, 0, wx.ALL | wx.CENTER, 5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez etat depuis sujet.get_donnees()
        # Mettez à jour le label
        # Couleur : noir pour "Travail", bleu pour "Pause"
        pass
