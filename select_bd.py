import sqlite3

conn = sqlite3.connect('db.sqlite3')

print ("Opened database successfully");

cursor = conn.execute("SELECT user_id, user_name, user_email from user")
for row in cursor:
   print ("ID = ", row[0])
   print ("Name = ", row[1])
   print ("Email = ", row[2])
   