from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
app = QApplication([])
fen = QWidget()

fen.setWindowTitle("QTableView Example")
fen.setGeometry(100, 100, 600, 400)


# create a QTableWidget
table = QTableWidget(fen)
table.setRowCount(2)
table.setColumnCount(3)
table.setGeometry(50, 50, 350, 150)


# adding header to the table
headerH = ['ID', 'Name', 'email']
headerV = ['a', 'b']
table.setHorizontalHeaderLabels(headerH)
table.setVerticalHeaderLabels(headerV)

table.setItem(0, 0, QTableWidgetItem(' 1'))
table.setItem(0, 1, QTableWidgetItem('  Albert Einstein'))
table.setItem(0, 2, QTableWidgetItem('  albert_einstein@gmail.com'))

fen.show()
app.exec()