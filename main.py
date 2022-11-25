# Austin Sohn, Justin Sohn, Samuel Sandoval
# main.py

import sys
from database.database import DatabaseClass
from datetime import datetime
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QTextEdit, QMessageBox, QListView
from PyQt6.uic import loadUi
from PySide6 import QtCore, QtWidgets, QtGui
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo

class GUI(QDialog):
  def __init__(self):
    self.table = "tasks"
    super(GUI,self).__init__()
    loadUi("./UI/window.ui",self)
    self.addGoalButton.clicked.connect(self.addGoalFunction)
    self.removeGoalButton.clicked.connect(self.removeGoalFunction)
    self.importButton.clicked.connect(self.importGoalFunctionality)
    self.exportButton.clicked.connect(self.exportGoalFunctionality)
    self.database = DatabaseClass()
    self.reminders()

    # outputs contents of db on startup
    self.database.outputDB(self.table)
    print("----------------")
    self.database.outputDB("subtasks")


  def addsPresetGoals(self):
    l = self.database.listDB(self.table)
    for x in l:
      self.goalList_Widget.addItem(x['task'])
      
  def addGoalFunction(self):
    #Typing in the Textbox and clicking add button to add to the List
    task = self.goalInputBox.toPlainText()
    if len(task) < 1:
      self.messageboxCreate("Add Goal Error", "Make sure to type your goal in before selecting add goal") 
      return
    self.goalInputBox.setPlainText(task)
    self.goalList_Widget.addItem(task)
    self.goalInputBox.clear()
    task_id = int(self.database.highestTaskID(self.table)) + 1
    status = 0
    start_date = "10/30/22" # change to input later
    end_date = "11/22/22" # change to input later
    params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
    self.database.addTask(self.table, params)

  def removeGoalFunction(self):
    #clicking on the Goal and clicking the remove button
    try:
      clicked = self.goalList_Widget.currentRow()
      task = self.goalList_Widget.selectedItems()
      task = task[0].text()
      self.goalList_Widget.takeItem(clicked)
      task_id = self.database.findTaskID(self.table,task)
      if(task_id):
        self.database.removeTask(self.table,task_id)
    except IndexError:
      print("error")
      self.messageboxCreate("Removing Error", "Error: Cannot remove a blank goal, please select an existing goal to remove.")      
  
  def messageboxCreate(self, winTitle, genText):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.setText(winTitle)
    msg.setInformativeText(genText)
    msg.setWindowTitle(winTitle)
    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    returnValue = msg.exec()

  # Imports text file from inputted filepath and creates goals
  def importGoalFunctionality(self):
    filepath = self.goalInputBox.toPlainText()
    self.goalInputBox.setPlainText(filepath)

    if len(filepath) < 1:
      self.messageboxCreate("Import Error", "Type the filepath into the box above and then select import again.")
    else:
      self.goalInputBox.clear()
      goalsFile = open(filepath , 'r')
      status = 0
      start_date = "10/30/22" # change to input later
      end_date = "11/30/22" # change to input later
      for task in goalsFile:
        task_id = int(self.database.highestTaskID(self.table)) + 1
        params = {"task_id":task_id, "task":task, "start_date":start_date, "end_date":end_date, "status":status}
        self.database.addTask(self.table,params)
      self.goalList_Widget.clear()
      self.addsPresetGoals()
      self.messageboxCreate("Import Completed", "Goals file has been imported.")

  # Exports goal into a text file 
  def exportGoalFunctionality(self):
    try:
      task = self.goalList_Widget.selectedItems()
      task = task[0].text()
      with open('outputtedTask.txt', 'w') as f:
          f.write(task)
          print("Exported Task")
      self.messageboxCreate("Export Completed", "Task has been exported.")
    
    except IndexError:
      self.messageboxCreate("Export Error", "Error: Select a goal before clicking export")      
      print("Error: Select a goal before clicking export") 

  # Reminders users about their goals
  def reminders(self):
    l = self.database.listDB(self.table)
    for task in l:
      d1 = datetime.strptime(task['end_date'], "%m/%d/%y").date()
      d2 = datetime.now().date()

      delta =  d2 - d1 
      if int(delta.days) >= -2 and task['task'] != None:
        # reminder
        msg = "Don't forget to compete your "
        msg += task['task']
        msg += ', the deadline is coming up!'
        self.messageboxCreate("Goal Reminder", msg)     

def main():
  app = QtWidgets.QApplication([])
  widget = GUI()
  widget.resize(600, 500)
  widget.addsPresetGoals()
  widget.show()

  


  sys.exit(app.exec())
if __name__ == "__main__":
  main()
