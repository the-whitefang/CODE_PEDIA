#!/bin/bash

DB_PATH="employee_records.db"

DELETE_DATE=$(date -d "30 days ago" '+%Y-%m-%d')

SQL="DELETE FROM employee WHERE created_at = '$DELETE_DATE';"

sqlite3 "$DB_PATH" "$SQL"

echo "Deleted records with created_at = $DELETE_DATE from $DB_PATH"
