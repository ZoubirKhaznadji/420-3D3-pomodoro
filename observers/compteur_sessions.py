import wx
from observers.observer import Observateur


class CompteurSessions(Observateur):

    def __init__(self, parent, sizer):
        self._label = wx.StaticText(parent, label="Sessions complétées : 0")
        sizer.Add(self._label, 0, wx.ALL | wx.CENTER, 5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez sessions_completees depuis sujet.get_donnees()
        # Mettez à jour le label avec SetLabel()
        pass
