import  pymysql
import mysql.connector

class setup:
    def __init__(self,host,user,passwd,database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
    def connect(self):
        db =mysql.connector.connect(
            host = self.host ,
            user = self.user ,
            passwd = self.passwd ,
            database = self.database)
        return db 

class table(setup):
    def __init__(self,host,user,passwd,database):
        self.table = ""
        super().__init__(host,user,passwd,database)
    
    def mk_table(self,table_name):

        self.table = "CREATE TABLE IF NOT EXISTS "+table_name+"( "

        return "table is added"
    
    def mk_column(self,column_name,type):
        self.table+=column_name+" "+type+","
        return "added_table"
    def publish_db(self):
        connect = setup(self.host,self.user,self.passwd,self.database)
        mydb = connect.connect()
        mycursor = mydb.cursor()
        self.table=self.table[0:-1]
        self.table+=")"
        #self.table[-2]="a"
        #print(self.table)
        mycursor.execute(self.table)
        mycursor.close()        
        return "succesfully created the table"



