#this is a test page

import YassaAlchemy


db = YassaAlchemy.table(host="localhost",user="root",passwd="new_password",database="yassadb")




class Users:
    def create(db):
        db.connect()
        #table_name =
        #name = db.table()
        db.mk_table("Users")
        db.mk_column("Username","VARCHAR(500)")
        db.mk_column("Password","VARCHAR(500)")
        db.publish_db()
    

Users.create(db)