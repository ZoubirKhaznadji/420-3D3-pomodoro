import wx
from observers.observer import Observateur


class BarreProgression(Observateur):

    def __init__(self, parent, sizer):
        self._barre = wx.Gauge(parent, range=100, size=(300, 20))
        self._barre.SetValue(100)
        sizer.Add(self._barre, 0, wx.ALL | wx.CENTER, 10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant et duree_totale depuis sujet.get_donnees()
        # Calculez la valeur en pourcentage (0-100)
        # Mettez à jour self._barre avec SetValue()
        pass
