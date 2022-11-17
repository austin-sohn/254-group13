# Austin Sohn, Justin Sohn, Samuel Sandoval
# main.py

import sys
from database.database import DatabaseClass
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QTextEdit, QMessageBox, QListView
from PyQt6.uic import loadUi
from PySide6 import QtCore, QtWidgets, QtGui

class GUI(QDialog):
  def __init__(self):
    super(GUI,self).__init__()
    loadUi("window.ui",self)
    self.addGoalButton.clicked.connect(self.addGoalFunction)
    self.removeGoalButton.clicked.connect(self.removeGoalFunction)
    self.exportButton.clicked.connect(self.exportFunc)
    self.taskDB = DatabaseClass()

  def addsPresetGoals(self):
    l = self.taskDB.listDB()
    for x in l:
      self.goalList_Widget.addItem(x)

  def addGoalFunction(self):
    #Typing in the Textbox and clicking add button to add to the List
    task = self.goalInputBox.toPlainText()
    self.goalInputBox.setPlainText(task)
    self.goalList_Widget.addItem(task)
    self.goalInputBox.clear()
    task_id = int(self.taskDB.highestTaskID()) + 1
    status = 0
    start_date = "10/30/22" # change to input later
    end_date = "11/30/22" # change to input later
    params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
    self.taskDB.addTask(params)

  def removeGoalFunction(self):
    #clicking on the Goal and clicking the remove button
    try:
      clicked = self.goalList_Widget.currentRow()
      task = self.goalList_Widget.selectedItems()
      task = task[0].text()
      self.goalList_Widget.takeItem(clicked)
      task_id = self.taskDB.findTaskID(task)
      if(task_id):
        self.taskDB.removeTask(task_id)
    except IndexError:
      print("error")
      # msg = QMessageBox()
      # msg.setIcon(QMessageBox.critical())
      # msg.setText("Error")
      # msg.setInformativeText('More information')
      # msg.setWindowTitle("Error")
      # msg.setStandartaskDButtons(QMessageBox.Ok | QMessageBox.Cancel)
  
  def exportFunc(self):
    try:
      clicked = self.goalList_Widget.currentRow()
      task = self.goalList_Widget.selectedItems()
      task = task[0].text()
      with open('outputtedTask.txt', 'w') as f:
          f.write(task)
          print("Exported Task")
    except IndexError:
      print("error")


def main():
  app = QtWidgets.QApplication([])
  widget = GUI()
  widget.resize(600, 500)
  widget.addsPresetGoals()
  widget.show()
  

  sys.exit(app.exec())
if __name__ == "__main__":
  main()
