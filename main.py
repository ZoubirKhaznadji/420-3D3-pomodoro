from models.minuteur import Minuteur
from views.dashboard import Dashboard
 
minuteur = Minuteur()
dashboard = Dashboard(minuteur)
dashboard.mainloop()