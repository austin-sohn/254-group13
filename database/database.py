# database.py
from datetime import date
import sqlite_utils

class DatabaseClass():
  def __init__(self):
    super().__init__()
    self.taskTableName = "tasks"
    self.db = sqlite_utils.Database("./database/database.db")
    self.subtaskTableName = "subtasks"
    self.taskTable = self.db.table(self.taskTableName, pk="task_id", 
    columns={"task_id": int, "start_date": date, "end_date": date, "status": bool},
    column_order=("task_id","task","start_date","end_date","status"))
    self.subtaskTable = self.db.table(self.subtaskTableName, pk="subtask_id", 
    columns={"subtask_id": int, "id":int, "start_date": date, "end_date": date, "status": bool},
    column_order=("task_id","id","task","start_date","end_date","status"))

# checks the table to see if it exsits
  def checkTable(self, table, params):
    if type(params) is dict:
      count = self.db[table].count_where("task_id = " + str(params.get("task_id")))
    else:
      count = self.db[table].count_where(f"task_id = {str(params)}")
    return count > 0

# outputs the entire database. only for testing.
  def outputDB(self, table):
    for row in self.db.query(f"SELECT * FROM {table}"):
      print(row)

# get list of database
  def listDB(self, table):
    l = []
    for row in self.db.query(f"SELECT * FROM {table}"):
      l.append(row)
    return l

# adds task to database after checking it exists or not
  def addTask(self, table, params):
    if not self.checkTable(table, params):
      self.db[table].insert(params)
      print("Added")
      # self.outputDB(table)

# removes the task
  def removeTask(self, table, params):
    try:
      if self.checkTable(table, params):
        self.taskTable.delete(params)
        print("Deleted")
        # self.outputDB(table)
    except:
      print("error in removeTask")

# find highest task_id
  def highestTaskID(self, table):
    if table == "tasks":
      cur = self.db.execute("SELECT MAX(task_id) FROM tasks").fetchall()
    elif table == "subtasks":
      cur = self.db.execute("SELECT MAX(subtask_id) FROM subtasks").fetchall()
    else:
      print("wrong table name")
    return cur[0][0]

  def findTaskID(self, table, task):
    if table == "tasks":
      cur = self.db.execute("SELECT task_id FROM tasks WHERE task = ?", [task]).fetchall()
    elif table == "subtasks":
      cur = self.db.execute("SELECT subtask_id FROM subtasks WHERE subtask = ?", [task]).fetchall()
    if cur:
      return int(cur[0][0])