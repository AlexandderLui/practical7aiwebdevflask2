from mysql.connector import Error
from mysql.connector import pooling
#from config.Settings import Settings

#Staging on heroku
class DatabasePool:
    #class variable
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host=Settings.host,
                                                  database=Settings.database,
                                                  user=Settings.user,
                                                  password=Settings.password)


"""
# Dev
class DatabasePool:
    #class variable
    connection_pool = pooling.MySQLConnectionPool(pool_name="ws_pool",
                                                  pool_size=5,
                                                  host='localhost',
                                                  database='furniture2',
                                                  user='root',
                                                  password='A!ex1333')

"""

    @classmethod
    def getConnection(cls):
        dbConn = cls.connection_pool.get_connection()
        return dbConn


'''
connection_object=DatabasePool.getConnection()
db_Info = connection_object.get_server_info()

print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)

cursor = connection_object.cursor(dictionary=True)

cursor.execute("select * from user;")
records = cursor.fetchall()
for record in records:
    print(record)
'''