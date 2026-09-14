import wx
from datetime import datetime


DUREE_TRAVAIL = 25 * 60
DUREE_PAUSE = 5 * 60


class App(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Minuteur Pomodoro")
        self.SetSize((350, 380))

        self.temps_restant = DUREE_TRAVAIL
        self.en_marche = False
        self.en_pause = False
        self.sessions_completees = 0

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Affichage état
        self.label_etat = wx.StaticText(panel, label="Travail")
        font_etat = self.label_etat.GetFont()
        font_etat.SetPointSize(16)
        font_etat.MakeBold()
        self.label_etat.SetFont(font_etat)
        sizer.Add(self.label_etat, 0, wx.ALL | wx.CENTER, 10)

        # Affichage temps
        self.label_temps = wx.StaticText(panel, label="25:00")
        font_temps = self.label_temps.GetFont()
        font_temps.SetPointSize(48)
        font_temps.MakeBold()
        self.label_temps.SetFont(font_temps)
        sizer.Add(self.label_temps, 0, wx.ALL | wx.CENTER, 10)

        # Barre de progression
        self.barre = wx.Gauge(panel, range=100, size=(300, 20))
        self.barre.SetValue(100)
        sizer.Add(self.barre, 0, wx.ALL | wx.CENTER, 10)

        # Compteur de sessions
        self.label_sessions = wx.StaticText(
            panel, label="Sessions complétées : 0"
        )
        sizer.Add(self.label_sessions, 0, wx.ALL | wx.CENTER, 5)

        # Boutons
        frame_boutons = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_start = wx.Button(panel, label="Démarrer")
        self.btn_pause = wx.Button(panel, label="Pause")
        self.btn_reset = wx.Button(panel, label="Réinitialiser")
        self.btn_pause.Disable()

        self.btn_start.Bind(wx.EVT_BUTTON, self.demarrer)
        self.btn_pause.Bind(wx.EVT_BUTTON, self.pause)
        self.btn_reset.Bind(wx.EVT_BUTTON, self.reinitialiser)

        frame_boutons.Add(self.btn_start, 0, wx.ALL, 5)
        frame_boutons.Add(self.btn_pause, 0, wx.ALL, 5)
        frame_boutons.Add(self.btn_reset, 0, wx.ALL, 5)
        sizer.Add(frame_boutons, 0, wx.CENTER)

        panel.SetSizer(sizer)
        self.Fit()

    def demarrer(self, event):
        self.en_marche = True
        self.en_pause = False
        self.btn_start.Disable()
        self.btn_pause.Enable()
        self.tick()

    def pause(self, event):
        if self.en_pause:
            self.en_pause = False
            self.btn_pause.SetLabel("Pause")
            self.tick()
        else:
            self.en_pause = True
            self.btn_pause.SetLabel("Reprendre")

    def reinitialiser(self, event):
        self.en_marche = False
        self.en_pause = False
        self.temps_restant = DUREE_TRAVAIL
        self.btn_start.Enable()
        self.btn_pause.Disable()
        self.btn_pause.SetLabel("Pause")
        self.label_etat.SetLabel("Travail")
        self.label_temps.SetLabel("25:00")
        self.barre.SetValue(100)

    def tick(self):
        if not self.en_marche or self.en_pause:
            return

        if self.temps_restant > 0:
            self.temps_restant -= 1

            # Mettre à jour le temps
            minutes = self.temps_restant // 60
            secondes = self.temps_restant % 60
            self.label_temps.SetLabel(f"{minutes:02d}:{secondes:02d}")

            # Mettre à jour la barre
            if self.label_etat.GetLabel() == "Travail":
                duree_totale = DUREE_TRAVAIL
            else:
                duree_totale = DUREE_PAUSE
            valeur = int(100 * self.temps_restant / duree_totale)
            self.barre.SetValue(valeur)

            wx.CallLater(1000, self.tick)

        else:
            if self.label_etat.GetLabel() == "Travail":
                self.sessions_completees += 1
                self.label_sessions.SetLabel(
                    f"Sessions complétées : {self.sessions_completees}"
                )
                self.label_etat.SetLabel("Pause")
                self.temps_restant = DUREE_PAUSE

                horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("pomodoro.log", 'a') as f:
                    f.write(
                        f"{horodatage} | Session {self.sessions_completees} "
                        f"complétée\n"
                    )
            else:
                self.label_etat.SetLabel("Travail")
                self.temps_restant = DUREE_TRAVAIL

            wx.CallLater(1000, self.tick)


if __name__ == "__main__":
    app = wx.App()
    fenetre = App()
    fenetre.Show()
    app.MainLoop()
