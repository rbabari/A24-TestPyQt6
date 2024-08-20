import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

def calculDouble():
    print(input.text())
    N = int(input.text()) * 2
    input.setText(str(N))

app = QApplication([])
fen = QWidget()
fen.setWindowTitle("CalculDouble")
fen.setGeometry(50,50,400,200)

# grid
grid = QGridLayout()
fen.setLayout(grid)

#label
lbl = QLabel("Donner un chiffre",fen)
grid.addWidget(lbl,0,0)

# lineEdit
input = QLineEdit(fen)
grid.addWidget(input,0,1)

# bouton
btn = QPushButton("Double",fen)
btn.clicked.connect(calculDouble)
grid.addWidget(btn,1,0)


fen.show()
app.exec()