# database.py
from datetime import date
import sqlite_utils

class DatabaseClass():
  def __init__(self):
    super().__init__()
    self.taskTableName = "tasks"
    self.db = sqlite_utils.Database("./database/tasks.db")
    self.taskTable = self.db.table(self.taskTableName, pk="task_id", 
    columns={"task_id": int, "start_date": date, "end_date": date, "status": bool},
    column_order=("task_id","task","start_date","end_date","status"))

# checks the table to see if it exsits
  def checkTable(self, params):
    if type(params) is dict:
      self.count = self.taskTable.count_where("task_id = " + str(params.get("task_id")))
    else:
      self.count = self.taskTable.count_where(f"task_id = {str(params)}")
    return self.count > 0

# outputs the entire database
  def outputDB(self):
    for row in self.db.query(f"SELECT * FROM {self.taskTableName}"):
      print(row)

# get list of database
  def listDB(self):
    l = []
    for row in self.db.query("SELECT * FROM " + self.taskTableName):
      l.append(row)
    return l

# adds task to database after checking it exists or not
  def addTask(self, params):
    if not self.checkTable(params):
      self.taskTable.insert(params)
      print("Added")
      self.outputDB()

# removes the task
  def removeTask(self, params):
    try:
      if self.checkTable(params):
        self.taskTable.delete(params)
        print("Deleted")
        self.outputDB()
    except:
      print("error in removeTask")

# find highest task_id
  def highestTaskID(self):
    cur = self.db.execute("SELECT MAX(task_id) FROM tasks").fetchall()
    return cur[0][0]

  def findTaskID(self, task):
    cur = self.db.execute("SELECT task_id FROM tasks WHERE task = ?", [task]).fetchall()
    if cur:
      return int(cur[0][0])