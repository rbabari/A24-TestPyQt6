# Partie 1 : Premier exemple avec la librairie PyQt6

# importer la librairie

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout


def action1():
    print("Action du btn1")
    qlbl1.setText("Btn1")

def action2():
    print("Action du btn2")
    qlbl1.setText("Btn2")

# Créer un objet QApplication
app = QApplication([])
# Créer un objet QWidget
fen = QWidget()
# modifier les parametres de cet objet
fen.setGeometry(50,50,400,200)
fen.setWindowTitle("Ma premiere app")

# Grid

grid = QGridLayout()
fen.setLayout(grid)


# QLabel
qlbl1 = QLabel(fen)
qlbl1.setText("Bonjour à toutes et à tous ")
grid.addWidget(qlbl1, 0, 0)

#QPushButton
qbtn1 = QPushButton(fen)
qbtn1.setText("Faire Action1")
qbtn1.clicked.connect(action1)
grid.addWidget(qbtn1, 1, 0)

#QPushButton
qbtn2 = QPushButton(fen)
qbtn2.setText("Faire Action2")
qbtn2.clicked.connect(action2)
grid.addWidget(qbtn2, 1, 1)

# Appler la methode show() de l'objet de type QWidget
fen.show()
# Executer l'application : object QApplication
app.exec()