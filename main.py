# Austin Sohn, Justin Sohn, Samuel Sandoval
# main.py

import sys
from database import Database
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
    self.db = Database()
  def addGoalFunction(self):
    #Typing in the Textbox and clicking add button to add to the List
    task = self.goalInputBox.toPlainText()
    self.goalInputBox.setPlainText(task)
    self.goalList_Widget.addItem(task)
    task_id = int(self.db.highestTaskID()) + 1
    status = 0
    start_date = "10/30/22" # change to input later
    end_date = "11/30/22" # change to input later
    params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
    self.db.addTask(params)
    self.db.outputDB()

  def removeGoalFunction(self):
    #clicking on the Goal and clicking the remove button
    clicked = self.goalList_Widget.currentRow()
    self.goalList_Widget.takeItem(clicked)
    self.db.removeTask(3)

def main():
  app = QtWidgets.QApplication([])
  widget = GUI()
  widget.resize(600, 500)
  widget.show()

  sys.exit(app.exec())
if __name__ == "__main__":
  main()
