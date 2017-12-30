from config.dbconfig import pg_config
import psycopg2


class CreditCardDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCreditCards(self):
        cursor = self.conn.cursor()
        query = "select * from creditcard;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardById(self, c_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard where c_id = %s;"
        cursor.execute(query, (c_id,))
        result = cursor.fetchone()
        return result

    def getBuyerByCreditCardId(self, c_id):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from creditcard natural inner join buyer natural inner join users where c_id = %s;"
        cursor.execute(query, (c_id,))
        result = cursor.fetchone()
        return result

    def getCreditCardByNameandBuyer(self, name, b_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard where c_name = %s and b_id = %S;"
        cursor.execute(query, (name, b_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from creditcard where c_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardByBuyer(self, b_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard where b_id = %S;"
        cursor.execute(query, (b_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
