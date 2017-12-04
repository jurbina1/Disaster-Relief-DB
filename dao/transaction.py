from config.dbconfig import pg_config
import psycopg2

class TransactionDAO:
   # def __init__(self):
        #connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
         #                                                   pg_config['user'],
         #                                                   pg_config['passwd'])
       # self.conn = psycopg2._connect(connection_url)

    def result(self):
        result = [
            {
                't_id': 1,
                's_id': 1,
                'b_id': 2,
                'r_id': 3,
                't_qty': 5,
                't_total': 10.00,
                't_date': '08/13/2017',
                't_donation': False,
                't_reservation': False
            },
            {
                't_id': 2,
                's_id': 2,
                'b_id': 1,
                'r_id': 1,
                't_qty': 2,
                't_total': 0.00,
                't_date': '11/1/2017',
                't_donation': True,
                't_reservation': False
            }
        ]
        return result

    def getAllTransactions(self):
        #cursor = self.conn.cursor()
        #query = "select * from transaction;"
        #cursor.execute(query)
        result = []
        for row in self.result: #cursor
            result.append(row)
        return result

    def getTransactionById(self, t_id):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where t_id = %s;"
        #cursor.execute(query, (t_id,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getBuyerByTransactionId(self, t_id):
        #cursor = self.conn.cursor()
        #query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from transaction natural inner join buyer natural inner join user where t_id = %s;"
        #cursor.execute(query, (t_id,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getSellerByTransactionId(self, t_id):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from transaction natural inner join buyer natural inner join user where t_id = %s;"
        #cursor.execute(query, (t_id,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getTransactionByDateSellerandBuyer(self, s_id, b_id, t_date):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where b_id = %s and s_id = %s and t_date = %s;"
        #cursor.execute(query, (b_id,s_id, t_date))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getTransactionBySellerandBuyer(self, s_id, b_id):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where b_id = %s and s_id = %s;"
        #cursor.execute(query, (b_id,s_id))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getTransactionBySellerandDate(self, s_id, t_date):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where s_id = %s and t_date = %s;"
        #cursor.execute(query, (s_id, t_date))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result


    def getTransactionByDateandBuyer(self, t_date, b_id):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where b_id = %s and t_date = %s;"
        #cursor.execute(query, (b_id, t_date))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result


    def getTransactionBySeller(self, s_id):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where s_id = %s;"
        #cursor.execute(query, (s_id,))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getTransactionByBuyer(self, b_id):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where b_id = %s;"
        #cursor.execute(query, (b_id,))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getTransactionByDate(self, t_date):
        #cursor = self.conn.cursor()
        #query = "select * from transaction where t_date = %s;"
        #cursor.execute(query, (t_date,))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getResourceByTransactionId(self, t_id):
        #cursor = self.conn.cursor()
        #query = "select r_id, r_category, r_name, r_description from transaction natural inner join resource where t_id = %s;"
        #cursor.execute(query, (t_id,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result
    