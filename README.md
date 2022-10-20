# 254-group13

# How to run the program

- cd to 254-group13 file
- To run the program, type in terminal:
  - chmod +x run.sh
  - ./run.sh
- Alternative way to run the program, type in terminal:
  - sqlite-utils insert ./database/tasks.db tasks ./database/tasks.csv --csv --pk=task_id --ignore
  - python3 main.py

# Install PyQT(PySide6)

- https://doc.qt.io/qtforpython/quickstart.html#requirements

# Documentation

- PyQT
  - https://doc.qt.io/qtforpython/contents.html
- sqlite_utils
  - https://sqlite-utils.datasette.io/en/stable/python-api.html

# How to update GitHub

- git add remote origin https://github.com/austin-sohn/254-group13/
- git checkout -b <new branch name>
  - creates a new local branch
- git add <files>
  - adds the files to be sent.
  - use "git add ." to add all the files in the folder
- git commit -m "some message"
  - writes a commit messages
- git push -u origin <new branch name>
  - make sure to be in the correct local branch before pushing new stuff
  - pushes the files to the repository under the new branch name

# Other useful git commands

- Pull changes to code
  - git pull
- Check what local branches you have
  - git branch
- Switch to different branches
  - git checkout <branch name>
- Delete local branch
  - git branch -d <branch name>
