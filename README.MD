# YassaAlchemy

SQLAlchemy was getting annoying so I have now made my own MySQL ORM(work in project btw).
The idea is to get basic SQL commands working. Currently can make tables and columns.
PyPi code: https://pypi.org/project/YassaAlchemy/

## Setup 
Just look at this code:
```python3
#this is a test page

import YassaAlchemy #import library


db = YassaAlchemy.table(host="localhost",user="root",passwd="new_password",database="yassadb")
#create instance of YassaAlchemy
#make sure a database is created and insert
#the neccesary credentials



class Users:
    #make static class


    #class for Users
    def create(db):
        db.connect()
        #connect to db
        db.mk_table("Users")#name the table
        db.mk_column("Username","VARCHAR(500)")#column one(Username) and type of data(Varchar)
        db.mk_column("Password","VARCHAR(500)")#column two(Password) and type of data(Varchar)
        db.publish_db()#commit changes
    

Users.create(db) #create User's table

```

## Install:
Clone repo. Delete test.py as it is simply starter code(or don't).
Make sure MySQL,python and the MySQL.connector are all installed.



## How to help
I have no time so please help me.
To find out what to do check over at ```projects```.



