import pymysql

Connection = pymysql.connect(host='localhost', user='root', password='',
                             db='raktar', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
ExecuteQuery(Connection)
Connection.close()
