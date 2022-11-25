# 254-group13

# Prerequisites

- python 3.7+
- PySide6
  - pip3 install pyside6==6.4
- PyQT
  - pip3 install pyqt6
- sqlite_utils
  - pip3 install sqlite-utils
- Tkinter
  - macos
    - brew install python-tk
  - linux (distros with apt)
    - sudo apt-get install python3-tk

# How to run the program

- cd to 254-group13 file
- To run the program, type in terminal:
  - chmod +x run.sh
  - ./run.sh
- An alternative way to run the program is to enter these commands one by one:
  - sqlite-utils create-database ./database/database.db
  - sqlite-utils create-table ./database/database.db tasks task_id integer --pk=task_id 
  - sqlite-utils insert ./database/database.db tasks ./database/tasks.csv --csv --ignore --alter 
  - sqlite-utils create-table ./database/database.db subtasks subtask_id integer --pk=subtask_id
  - sqlite-utils insert ./database/database.db subtasks ./database/subtasks.csv --csv --ignore --alter
  - python3 main.py

# Documentation

- PyQT
  - https://doc.qt.io/qtforpython/contents.html
- sqlite_utils
  - https://sqlite-utils.datasette.io/en/stable/python-api.html
- Tkinter
  - https://docs.python.org/3/library/tkinter.html
