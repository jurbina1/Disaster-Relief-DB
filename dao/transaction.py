from config.dbconfig import pg_config
import psycopg2


class TransactionDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select * from transaction;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionById(self, t_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_id = %s;"
        cursor.execute(query, (t_id,))
        result = cursor.fetchone()
        return result

    def getBuyerByTransactionId(self, t_id):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from transaction natural inner join buyer natural inner join users where t_id = %s;"
        cursor.execute(query, (t_id,))
        result = cursor.fetchone()
        return result

    def getSellerByTransactionId(self, t_id):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from transaction natural inner join seller natural inner join users where t_id = %s;"
        cursor.execute(query, (t_id,))
        result = cursor.fetchone()
        return result

    def getTransactionByDateSellerandBuyer(self, s_id, b_id, t_date):
        cursor = self.conn.cursor()
        query = "select * from transaction where b_id = %s and s_id = %s and t_date = %s;"
        cursor.execute(query, (b_id, s_id, t_date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionBySellerandBuyer(self, s_id, b_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where b_id = %s and s_id = %s;"
        cursor.execute(query, (b_id, s_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionBySellerandDate(self, s_id, t_date):
        cursor = self.conn.cursor()
        query = "select * from transaction where s_id = %s and t_date = %s;"
        cursor.execute(query, (s_id, t_date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByDateandBuyer(self, t_date, b_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where b_id = %s and t_date = %s;"
        cursor.execute(query, (b_id, t_date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionBySeller(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByBuyer(self, b_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where b_id = %s;"
        cursor.execute(query, (b_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByDate(self, t_date):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_date = %s;"
        cursor.execute(query, (t_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByTransactionId(self, t_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type from transaction natural inner join resource where t_id = %s;"
        cursor.execute(query, (t_id,))
        result = cursor.fetchone()
        return result

    def getTransactionTotalSum(self):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from transaction;"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getTransactionSumBySeller(self, s_id):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from transaction where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        return result

    def getTransactionSumByBuyer(self, b_id):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from transaction where b_id = %s;"
        cursor.execute(query, (b_id,))
        result = cursor.fetchone()
        return result

    def getTransactionSumByResource(self, r_id):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from transaction where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = cursor.fetchone()
        return result

    def getTransactionSumByDate(self, t_date):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from transaction where t_date = %s;"
        cursor.execute(query, (t_date,))
        result = cursor.fetchone()
        return result

    def getTransactionSumByCity(self, city):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from((select s_id, u_city as s_city from seller natural inner join users) S join transaction T on T.s_id = S.s_id) T1 join (select b_id, u_city as b_city from buyer natural inner join users) B on T1.b_id = B.b_id where b_city = %s or s_city= %s;"
        cursor.execute(query, (city,city))
        result = cursor.fetchone()
        return result

    def getTransactionSumByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select sum(t_total) from((select s_id, u_region as s_region from seller natural inner join users) S join transaction T on T.s_id = S.s_id) T1 join (select b_id, u_region as b_region from buyer natural inner join users) B on T1.b_id = B.b_id where b_region = %s or s_region= %s;"
        cursor.execute(query, (region,region))
        result = cursor.fetchone()
        return result

    def getDonations(self):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_donation = true;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservations(self):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_reservation = true;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
