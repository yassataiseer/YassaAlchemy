#Example code

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