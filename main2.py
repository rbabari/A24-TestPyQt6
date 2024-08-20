# Partie 1 : Premier exemple avec la librairie PyQt6

# importer la librairie

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# Créer un objet QApplication
app = QApplication([])
# Créer un objet QWidget
fen = QWidget()
# modifier les parametres de cet objet
fen.setGeometry(50,50,400,200)
fen.setWindowTitle("Ma premiere app")

# QLabel
qlbl1 = QLabel(fen)
qlbl1.setText("Bonjour à toutes et à tous ")
qlbl1.setStyleSheet("background-color:white;color:red;border:3px solid yellow;font-size:28px;font:broadway")
qlbl1.setGeometry(10,10,400,200)



# Appler la methode show() de l'objet de type QWidget
fen.show()
# Executer l'application : object QApplication
app.exec()