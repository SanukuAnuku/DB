import mysql.connector
import pymysql.cursors

class DB_Connect():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cursorclass = pymysql.cursors.DictCursor
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

    def insert_classes(self):
        cursor = self.connection.cursor()
        sql = 'INSERT INTO grades(grade, exam_grade) VALUES (%s, %s)'
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (place1, place2,))
            self.connection.commit()

    def select_classes(self):
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM grades'
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            classes = cursor.fetchall()
            for row in classes:
                print(row)
