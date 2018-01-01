from config.dbconfig import pg_config
import psycopg2


class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, rq_id):
        cursor = self.conn.cursor()
        query = "select * from request where rq_id = %s;"
        cursor.execute(query, (rq_id,))
        result = cursor.fetchone()
        return result

    def getResourcesByRequestId(self, rq_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type from request natural inner join resource where rq_id = %s;"
        cursor.execute(query, (rq_id,))
        result = cursor.fetchone()
        return result

    def getBuyerByRequestId(self, rq_id):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from request natural inner join buyer natural inner join users where rq_id = %s;"
        cursor.execute(query, (rq_id,))
        result = cursor.fetchone()
        return result

    def getRequestByBuyerResourceandDate(self, rq_date, b_id, r_id):
        cursor = self.conn.cursor()
        query = "select * from request where rq_date = %s and b_id = %s and r_id = %s;"
        cursor.execute(query, (rq_date, b_id, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByBuyerandResource(self, b_id, r_id):
        cursor = self.conn.cursor()
        query = "select * from request where b_id = %s and r_id = %s;"
        cursor.execute(query, (b_id, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByBuyerandDate(self, b_id, rq_date):
        cursor = self.conn.cursor()
        query = "select * from request where rq_date = %s and b_id = %s;"
        cursor.execute(query, (rq_date, b_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByResourceandDate(self, r_id, rq_date):
        cursor = self.conn.cursor()
        query = "select * from request where rq_date = %s and r_id = %s;"
        cursor.execute(query, (rq_date, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByBuyer(self, b_id):
        cursor = self.conn.cursor()
        query = "select * from request where b_id = %s;"
        cursor.execute(query, (b_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByResource(self, r_id):
        cursor = self.conn.cursor()
        query = "select * from request where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByDate(self, rq_date):
        cursor = self.conn.cursor()
        query = "select * from request where rq_date = %s;"
        cursor.execute(query, (rq_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

