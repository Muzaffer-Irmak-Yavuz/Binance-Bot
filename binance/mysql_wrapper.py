import mysql.connector
import mysql_conn_info as cinfo

class mysql_handler:

    #class member variables
    connection = None
    cursor = None

    #class constructor
    def __init__(self):
        self.connection = mysql.connector.connect(host=cinfo.host,user=cinfo.user,passwd=cinfo.password,database=cinfo.database,port=3306)

    def insert_value(self,name,open,close,macd,macd_s,macd_h,rsi):

        
        sql_insert_query = ("INSERT INTO coins "
               "(name,open,close,macd,macd_s,macd_h,rsi) "
               "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        
        sql_insert_data = (name , open ,close ,macd ,macd_s , macd_h ,rsi)

        
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_insert_query, sql_insert_data)
        self.connection.commit()

    def get_data_from_sql(self):
        
        sql_select_query = ("select * from coins")

        self.cursor.execute(sql_select_query)
        columns = self.cursor.fetchall()

        return columns

    def purge_sql_connection(self):

        self.cursor.close()
        self.connection.close()  









