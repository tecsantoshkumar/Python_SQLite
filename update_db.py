import sqlite3

conn = sqlite3.connect('db/db.sqlite3');
print ("Opened database successfully");

conn.execute("UPDATE COMPANY set SALARY = 26000.00 where ID = 4");
conn.commit();
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY");
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")