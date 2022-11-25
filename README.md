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
  - linux
    pip3 install tk

# How to run the program

- cd to 254-group13 file
- To run the program, type in terminal:
  - chmod +x run.sh
  - ./run.sh
- Alternative way to run the program, type in terminal:
  - sqlite-utils insert ./database/tasks.db tasks ./database/tasks.csv --csv --pk=task_id --ignore
  - python3 main.py

# Documentation

- PyQT
  - https://doc.qt.io/qtforpython/contents.html
- sqlite_utils
  - https://sqlite-utils.datasette.io/en/stable/python-api.html
- Tkinter
  - https://docs.python.org/3/library/tkinter.html
