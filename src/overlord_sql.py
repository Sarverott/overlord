import mysql.connector

class OverlordSql():

    #todo: sql script parser, script executor, logs puller 

    def __init__(database):
        self.sqlDatabase=database

    def config(self, host, username, password):
        self.sqlHost=host
        self.sqlUser=username
        self.sqlPass=password

    def connect(mode="mysql"): #more modes in future plans
        self.sqlHook=mysql.connector.connect(
          host=self.sqlHost,
          user=self.sqlUser,
          password=self.sqlPass,
          database=self.sqlDatabase
        )
        self.dbCursor=self.sqlHook.cursor()

    def end():
        self.sqlHook.close()
