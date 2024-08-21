# Partie 1 : Premier    exemple avec la librairie PyQt6

# importer la librairie

from PyQt6.QtWidgets import QApplication, QWidget
# Créer un objet QApplication
app = QApplication([])
# Créer un objet QWidget
fen = QWidget()




# Appler la methode show() de l'objet de type QWidget
fen.show()
# Executer l'application : object QApplication
app.exec()
