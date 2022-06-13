# How to Fetch and Update Data From Database in  Python-DB

* Connect to MySQL database

* Fetch data from the database

* Create data from database

* Update data from database

* Delete data from database

# Connect to MySQL database
```
import sqlite3

conn = sqlite3.connect('db/db.sqlite3');

print ("Opened database successfully");
```

# Fetch data from the database

```
import sqlite3

conn = sqlite3.connect('db.sqlite3')

print ("Opened database successfully");

cursor = conn.execute("SELECT user_id, user_name, user_email from user")
for row in cursor:
   print ("ID = ", row[0])
   print ("Name = ", row[1])
   print ("Email = ", row[2])
 ```  
   
  # Create data from database
  
  ```
  conn = sqlite3.connect('db/db.sqlite3');

print ("Opened database successfully");

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");
```

# Update data from database

```
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
   ```

# Delete data from database

```
import sqlite3

conn = sqlite3.connect('db/db.sqlite3');
print ("Opened database successfully");

conn.execute("DELETE from COMPANY where ID = 3;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
   ```
