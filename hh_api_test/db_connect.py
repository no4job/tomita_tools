__author__ = 'mdu'
#from itertools import chain
import common_config
import mysql.connector
import datetime
from mysql.connector import Error
#import configparser
#import os.path


class Database():
    #connection = None
    #cursor = None
    def __init__(self, **kwargs):
        self.host = kwargs.get('HOST')
        self.port = kwargs.get('PORT')
        self.database = kwargs.get('NAME')
        self.user = kwargs.get('USER')
        self.password = kwargs.get('PASSWORD')
        self.autocommit = True
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      port=self.port,
                                                      database=self.database,
                                                      user=self.user,
                                                      password=self.password,
                                                      autocommit=self.autocommit
                                                      )
            if self.connection.is_connected():
                self.connection_id = self.connection.connection_id
                print("Database connection with ID = %s established." % str(self.connection_id))
                self.cursor = self.connection.cursor()
                #self.cursor_d = self.connection.cursor(dictionary=True)
        except Error as e:
            print(e)
            raise

    def query(self, query, params):
        try:
            self.cursor.execute(query, params)
        except Error as e:
            print(e)
            raise
        finally:
            if common_config.DEBUG:
                print(self.cursor.statement)
        return self.cursor

    def __enter__(self):
        return self

    def insert(self, table, data):
        """Insert a record"""

        query = self._serialize_insert(data)

        sql = "INSERT %s (%s) VALUES(%s)" % (table, query[0], query[1])

        #return self.query(sql, data.values()).rowcount
        return self.query(sql, data).rowcount

    def _serialize_insert(self, data):
        """Format insert dict values into strings"""
        kv=data.items()
        keys = ",".join( k[0] for k in kv )
        vals = ",".join(["%%(%s)s" % k[0] for k in kv])

        return [keys, vals]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            #self.conn.rollback()
            pass
        try:
            #self.connection.commit()
            pass
        except Exception:
            #self.connection.rollback()
            pass
        finally:
            self.connection.close()
            if not self.connection.is_connected():
                print("Database connection with ID = %s closed." % str(self.connection_id))



if __name__ == "__main__":
    #ts=datetime.datetime(2015, 6, 11, 19, 29, 50, 974279)
    #data ={"skill_id":"NULL", "name":'name25', "mode":1, "active":2, "creation_time":"NULL"}
    data ={"name":'name25', "mode":1, "active":2}
    #data ={"NULL", "name25", 1, 2, "NULL"}
    with Database(**common_config.DATABASES['default']) as db:
        #print(db.query("select CONNECTION_ID()",None).fetchone())
        db.insert("skill_abbreviations",data)
        db.query("select * from skill_abbreviations",None)
        for row in db.cursor:
            #print(cursor.query("select * from skill_abbreviations",None).fetchone())
            print(row)


exit(0)
