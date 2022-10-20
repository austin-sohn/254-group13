sqlite-utils insert ./database/tasks.db tasks ./database/tasks.csv --csv --pk=task_id --ignore
python3 main.py
