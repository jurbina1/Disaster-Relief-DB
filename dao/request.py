from config.dbconfig import pg_config
import psycopg2

class RequestDAO:
 #   def __init__(self):
#
#        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
#                                                            pg_config['user'],
#                                                            pg_config['passwd'])
#        self.conn = psycopg2._connect(connection_url)


    def result(self):
        result= [
            {
                'rq_id' : 1,
                'b_id' : 3,
                'r_id' : 1,
                'rq_qty' : 24,
                'rq_date': '09/29/2017',
                'rq_fulfillment': False,
            },
            {
                'rq_id': 2,
                'b_id': 2,
                'r_id': 2,
                'rq_qty': 5,
                'rq_date': '04/01/2017',
                'rq_fulfillment': True,
            },
            {
                'rq_id': 3,
                'b_id': 1,
                'r_id': 3,
                'rq_qty': 3,
                'rq_date': '11/18/2017',
                'rq_fulfillment': False,
            }
        ]
        return result

    def getAllRequests(self):
#        cursor = self.conn.cursor()
#        query = "select * from request;"
#        cursor.execute(query)
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getRequestById(self, rq_id):
#        cursor = self.conn.cursor()
#        query = "select * from request where rq_id = %s;"
#        cursor.execute(query, (rq_id,))
#        result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getResourcesByRequestId(self, rq_id):
#        cursor = self.conn.cursor()
#        query = "select r_id, r_category, r_name, r_description from request natural inner join resource where rq_id = %s;"
#        cursor.execute(query, (rq_id,))
#        result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByRequestId(self, rq_id):
 #       cursor = self.conn.cursor()
 #       query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from request natural inner join buyer natural inner join user where rq_id = %s;"
 #       cursor.execute(query, (rq_id,))
 #       result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByBuyerResourceandDate(self, rq_date, b_id, r_id):
  #      cursor = self.conn.cursor()
  #      query = "select * from request where rq_date = %s and b_id = %s and r_id = %s;"
  #      cursor.execute(query, (rq_date, b_id, r_id))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByBuyerandResource(self, b_id, r_id):
  #      cursor = self.conn.cursor()
  #      query = "select * from request where b_id = %s and r_id = %s;"
  #      cursor.execute(query, (b_id, r_id))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByBuyerandDate(self, b_id, rq_date):
 #       cursor = self.conn.cursor()
 #       query = "select * from request where rq_date = %s and b_id = %s;"
 #       cursor.execute(query, (rq_date, b_id))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByResourceandDate(self, r_id, rq_date):
#        cursor = self.conn.cursor()
#        query = "select * from request where rq_date = %s and r_id = %s;"
#        cursor.execute(query, (rq_date, r_id))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByBuyer(self, b_id):
#        cursor = self.conn.cursor()
#        query = "select * from request where b_id = %s;"
#        cursor.execute(query, (b_id,))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByResource(self, r_id):
 #       cursor = self.conn.cursor()
 #       query = "select * from request where r_id = %s;"
 #       cursor.execute(query, (r_id,))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getRequestByDate(self, rq_date):
 #       cursor = self.conn.cursor()
 #       query = "select * from request where rq_date = %s;"
 #       cursor.execute(query, (rq_date,))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result
    
    