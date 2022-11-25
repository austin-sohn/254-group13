sqlite-utils create-database ./database/database.db
sqlite-utils create-table ./database/database.db tasks task_id integer --pk=task_id
sqlite-utils insert ./database/database.db tasks ./database/tasks.csv --csv --ignore --alter
sqlite-utils create-table ./database/database.db subtasks subtask_id integer --pk=subtask_id
sqlite-utils insert ./database/database.db tasks ./database/subtasks.csv --csv --ignore --alter
python3 main.py