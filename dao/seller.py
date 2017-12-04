from config.dbconfig import pg_config
import psycopg2

class SellerDAO:
    #def __init__(self):

    #    connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                        pg_config['user'],
    #                                                        pg_config['passwd'])
    #    self.conn = psycopg2._connect(connection_url)

    def result(self):
        result=[
            {
                's_id':1,
                'u_name':"Leo",
                'u_lastname': "Rodriguez",
                'u_email':"leo.rodriguez1848@hotmail.com",
                'u_password': "***********",
                'u_region': "Ponce",
                'u_phone': 7876573982,
                'u_age': 29,
            },
            {
                's_id': 2,
                'u_name': "Melvin",
                'u_lastname': "Fernandez",
                'u_email': "melvin.fernandez86@gmail.com",
                'u_password': "*********",
                'u_region': "Mayaguez",
                'u_phone': 7878736492,
                'u_age': 38,
            },
            {
                's_id': 3,
                'u_name': "Olga",
                'u_lastname': "Benitez",
                'u_email': "olga.benitez62@yahoo.com",
                'u_password': "************",
                'u_region': "Arecibo",
                'u_phone': 7875853850,
                'u_age': 54,
            }
        ]
        return result

    def getAllSellers(self):
   #     cursor = self.conn.cursor()
   #     query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user;"
    #    cursor.execute(query)
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerById(self, s_id):
   #         cursor = self.conn.cursor()
   #         query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller where s_id = %s;"
   #         cursor.execute(query, (s_id,))
   #         result = cursor.fetchone()
            result = []
            for row in self.result():  # cursor:
                result.append(row)
            return result

    def getResourcesBySellerId(self, s_id):
       # cursor = self.conn.cursor()
       # query = "select r_id, r_category, r_name, a_qty, a_price, a_date from resource natural inner join seller natural inner join announcement where s_id = %s;"
       # cursor.execute(query, (s_id,))
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerByRegionNameAndLastName(self, region, name, lastname):
       # cursor = self.conn.cursor()
       # query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_name = %s and u_lastname = %s and u_region = %s;"
       # cursor.execute(query, (name, lastname, region))
       # result = cursor.fetchone()
       result = []
       for row in self.result():  # cursor:
           result.append(row)
       return result

    def getSellerByNameandLastName(self, name, lastname):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_name = %s and u_lastname = %s;"
       # cursor.execute(query, (name, lastname))
        #result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerByNameandRegion(self, name, region):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_name = %s and u_region = %s;"
        #cursor.execute(query, (name, region))
        #result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerByLastNameandRegion(self, lastname, region):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_lastname = %s and u_region = %s;"
        #cursor.execute(query, (lastname, region))
        #result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerByName(self, name):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_name = %s;"
        #cursor.execute(query, (name,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerByLastName(self, lastname):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_lastnane = %s;"
        #cursor.execute(query, (lastname,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getSellerByRegion(self, region):
        #cursor = self.conn.cursor()
        #query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from seller natural inner join user where u_region = %s;"
        #cursor.execute(query, (region,))
        #result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result