# Austin Sohn, Justin Sohn, Samuel Sandoval
# main.py

"""
import sys, os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PyQt6 import QtWidgets, uic


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

  sys.exit(app.exec())
if __name__ == "__main__":
  main()
"""

# This Python file uses the following encoding: utf-8

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QTextEdit,QListView
from PyQt6.uic import loadUi
from PySide6 import QtCore, QtWidgets, QtGui

class GUI(QDialog):
  def __init__(self):
    super(GUI,self).__init__()
    loadUi("window.ui",self)
    self.addGoalButton.clicked.connect(self.addGoalFunction)
    self.removeGoalButton.clicked.connect(self.removeGoalFunction)

  def addGoalFunction(self):
    #Typing in the Textbox and clicking add button to add to the List
    content = self.goalInputBox.toPlainText()
    self.goalInputBox.setPlainText(content)
    self.goalList_Widget.addItem(content)

  def removeGoalFunction(self):
    #clicking on the Goal and clicking the remove button
    clicked = self.goalList_Widget.currentRow()
    self.goalList_Widget.takeItem(clicked)


def main():
  app = QtWidgets.QApplication([])
  widget = GUI()
  widget.resize(600, 500)
  widget.show()

  sys.exit(app.exec())
if __name__ == "__main__":
  main()
