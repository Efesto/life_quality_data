import mysql.connector
import os

from dotenv import load_dotenv
load_dotenv()

class MySql:
    def connection(self):
      return mysql.connector.connect(
        host="localhost",
        user=os.environ['HUMIDITY_DB_USER'],
        passwd=os.environ['HUMIDITY_DB_PASSWORD'],
        database=os.environ['HUMIDITY_DB_NAME']
      )

    def get_all(self):
        connection = self.connection()
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM readings ORDER BY datetime DESC")
        myresult = mycursor.fetchall()

        connection.close()

        return myresult

    def create_table(self):
        connection = self.connection()
        mycursor = connection.cursor()
        mycursor.execute("CREATE TABLE readings (datetime DATETIME, temperature FLOAT, humidity FLOAT)")
        connection.close()
    
    def insert_reading(self, time, temperature, humidity):
        connection = self.connection()
        reading_time = time.strftime('%Y-%m-%d %H:%M:%S')
        mycursor = connection.cursor()
        mycursor.execute(f"INSERT INTO readings (datetime, humidity, temperature) VALUES ('{reading_time}', {humidity}, {temperature})")
        connection.commit()
        connection.close()