# database.py
import sqlite_utils

class Database():
  def __init__(self):
    super().__init__()
    self.tableName = "tasks"
    self.db = sqlite_utils.Database("./database/tasks.db")
    self.table = self.db.table(self.tableName, pk="task_id", 
    column_order=("task_id","task","start_date","end_date","status"))

# checks the table to see if it exsits
  def checkTable(self, params):
    self.count = self.table.count_where("task_id = " + str(params.get("task_id")))
    if self.count > 0:
      return True
    return False

  # outputs the entire database
  def outputDB(self):
    for row in self.db.query("SELECT * FROM " + self.tableName):
      print(row)

  # adds task to database after checking it exists or not
  def addTask(self, params):
    if not self.checkTable(params):
      self.table.insert(params)
      print("Added")

  def removeTask(self, params):
    if self.checkTable(params):
      self.table.delete(str(params.get("task_id")))
      print("Deleted")