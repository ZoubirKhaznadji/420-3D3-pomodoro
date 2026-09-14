from datetime import datetime
from observers.observer import Observateur


class LoggerSession(Observateur):

    def __init__(self, chemin_fichier: str = "pomodoro.log"):
        self._chemin = chemin_fichier
        self._derniere_session = 0

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        sessions = donnees['sessions_completees']

        # Écrire seulement quand une nouvelle session est complétée
        if sessions > self._derniere_session:
            self._derniere_session = sessions
            horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self._chemin, 'a') as f:
                f.write(f"{horodatage} | Session {sessions} complétée\n")
