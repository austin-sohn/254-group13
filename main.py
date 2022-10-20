# Austin Sohn, Justin Sohn, Samuel Sandoval
# main.py

import sys
import random
from database import Database
from PySide6 import QtCore, QtWidgets, QtGui

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

def main():
  app = QtWidgets.QApplication([])
  widget = GUI()
  widget.resize(800, 600)
  widget.show()
  task_id = 1211
  task = "idk"
  start_date = "10/30/22"
  end_date = "11/30/22"
  status = 1
  params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
  db = Database()
  db.addTask(params)
  db.removeTask(params)
  db.outputDB() # outputs database to terminal
  sys.exit(app.exec())
if __name__ == "__main__":
  main()