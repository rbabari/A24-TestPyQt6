# Partie 1 : Premier exemple avec la librairie PyQt6
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
# importer la librairie

from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# Créer un objet QApplication
app = QApplication([])
# Créer un objet QWidget
fen = QWidget()
fen.setGeometry(100, 100, 200, 200)
# créer un objet qpixmap
qpixmap1 = QPixmap("images/laptop.png")

# creer l'objet label
lbl1 = QLabel(fen)
lbl1.setPixmap(qpixmap1)

# modifier la taille de l'image
lbl1.setScaledContents(True)
lbl1.resize(200,200)


# Appler la methode show() de l'objet de type QWidget
fen.show()
# Executer l'application : object QApplication
app.exec()