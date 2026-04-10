import mysql.connector
import argparse

# Set up the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--user", required=True, help="The database username")
parser.add_argument("--password", required=True, help="The database password")
args = parser.parse_args()

#Connect to my database 'patientrecords'
mydb = mysql.connector.connect(
    host="localhost",
    user=args.user,         
    password=args.password, 
    database = "patientrecords"
)

#Print table 'Patients'
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Patients")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#Print table 'Medication'
mycursor.execute("SELECT * FROM Medication")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#Print the information of Patients receiving Medication with ID 3
mycursor.execute ("SELECT * FROM Patients WHERE Medication = 3")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#To automate queries that are asked often:
#Define your queries in a list
queries = [
    "SELECT * FROM Patients",
    "SELECT * FROM Medication",
    "SELECT * FROM Patients WHERE Medication = 3"
]

#Loop through each query
for sql in queries:
    print(f"\n--- Running: {sql} ---") # adds a header for clarity
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        print(x)

#Or to easily execute different sql commands:
#Define the function to run and print the sql command
def run_and_print(query_string):
    mycursor.execute(query_string) 
    for row in mycursor.fetchall():
        print(row)

#Use the function with the appropriate sql command (instead of repeating as in the first instance)
run_and_print("SELECT * FROM Patients")


#To show what medication each patient receives - join table 'Patients' column 'FullName' with table 'Medication' column 'Name'
sql = "SELECT \
    Patients.FullName AS Patient, \
    Medication.Name AS Medication \
    FROM Patients \
    INNER JOIN Medication ON Patients.Medication = Medication.MedicationID"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    