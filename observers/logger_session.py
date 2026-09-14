from datetime import datetime
from observers.observer import Observateur


class LoggerSession(Observateur):

    def __init__(self, chemin_fichier: str = "pomodoro.log"):
        self._chemin = chemin_fichier
        self._derniere_session = 0

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez sessions_completees depuis sujet.get_donnees()
        sujet.get_donnees()
        donnees = sujet.get_donnees()
        donnees = donnees["sessions_completees"]
        # Écrivez dans le fichier SEULEMENT si une nouvelle session est complétée
        # (comparez avec self._derniere_session)
        # Mettez à jour self._derniere_session
        if self.label_etat.cget("text") == "Travail":
            horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("pomodoro.log", 'a') as f:
                f.write(
                    f"{horodatage} | Session {self.sessions_completees} "
                    f"complétée\n")
        self.sessions_completees = self.sessions_completees + 1
        self._derniere_session = self.sessions_completees
