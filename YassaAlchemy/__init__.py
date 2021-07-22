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

class mk_table(setup):
    def __init__(self,host,user,passwd,database):
        super().__init__(host,user,passwd,database)
    

