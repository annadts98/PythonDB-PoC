# Patient Records Database Query Script

This Python script demonstrates how to connect to a local MySQL database (`patientrecords`) and execute various SQL queries using the `mysql-connector-python` library. It includes examples of basic `SELECT` statements, using loops and functions to streamline code, and performing an `INNER JOIN` across tables.

## Prerequisites

Before running this script, ensure you have the following installed and configured:

1. **Python 3.x**
2. **MySQL Server** running locally (`localhost`).
3. **Database Setup**: You must have a database named `patientrecords` containing at least two tables:
   * `Patients` (must contain a `Medication` column referencing a medication ID, and a `FullName` column)
   * `Medication` (must contain a `MedicationID` and `Name` column)
4. **Python Dependencies**: Install the MySQL connector library.

```bash
# Using standard pip
pip install mysql-connector-python

# Or using uv (if managing your environment with uv)
uv pip install mysql-connector-python
```



## Usage

This script uses command-line arguments to securely pass your database credentials without hardcoding them into the script. 

Run the script from your terminal using the `--user` and `--password` flags:

```bash
python PatientRecords.py --user <your_username> --password <your_password>
```


> **Note:** Replace `PatientRecords.py` with the actual name of your Python file (e.g., `main.py` or `db_queries.py`).

## Features Demonstrated

When executed, the script will output the results of the following operations to the console:

* **Basic Queries:** Fetches and prints all records from the `Patients` and `Medication` tables.
* **Filtered Queries:** Fetches patients specifically assigned to Medication ID `3`.
* **Iteration:** Demonstrates how to loop through a predefined list of SQL query strings for automated execution.
* **Reusable Functions:** Uses a custom `run_and_print()` function to adhere to the DRY (Don't Repeat Yourself) programming principle.
* **Relational Joins:** Executes an `INNER JOIN` to map the `Medication` ID in the `Patients` table to the actual medication `Name` in the `Medication` table, resulting in a readable `Patient | Medication` output.
```
