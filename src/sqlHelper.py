import sqlite3
import os

def db_exists(db_file):
   """ tests existence of a database
   """
   return os.path.exists(db_file)

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by the db_file
   :param db_file: database file
   :return: Connection object or None
   """
   try:
      conn = sqlite3.connect(db_file)
      return conn
   except Error as e:
      print(e)
   return None

def main():
   dbdir = '../data/'
   emailsDB = 'emails.db'

   cursor = create_connect_db(dbdir + emailsDB).cursor()
   c.execute('''CREATE TABLE emails
               (date text, qty real, price real)''')
   pass

if __name__ == '__main__':
   main()
