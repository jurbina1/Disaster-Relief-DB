from config.dbconfig import pg_config
import psycopg2

class BuyerDAO:
   # def __init__(self):
#
 #       connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
  #                                                          pg_config['user'],
   #                                                         pg_config['passwd'])
    #    self.conn = psycopg2._connect(connection_url)


    def result(self):
       result = [
           {
               'b_id': 1,
               'u_name': "Sara",
               'u_lastname': "Valle",
               'u_email': "sara.valle2@hotmail.com",
               'u_password': "***********",
               'u_region': "San Juan",
               'u_phone': 7871234567,
               'u_age': 75,
           },
           {
               'b_id': 2,
               'u_name': "Jocelyn",
               'u_lastname': "Finelli",
               'u_email': "jocelyn.finelli@gmail.com",
               'u_password': "*********",
               'u_region': "Bayamon",
               'u_phone': 7870987654,
               'u_age': 20,
           },
           {
               'b_id': 3,
               'u_name': "Christian",
               'u_lastname': "Hernandez",
               'u_email': "christian.hernandez578@yahoo.com",
               'u_password': "************",
               'u_region': "Humacao",
               'u_phone': 7875678901,
               'u_age': 35,
           }
       ]
       return result


    def getAllBuyers(self):
      #  cursor = self.conn.cursor()
      #  query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user;"
      #  cursor.execute(query)
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getBuyerById(self, b_id):
            #cursor = self.conn.cursor()
       #     query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer where b_id = %s;"
       #     cursor.execute(query, (b_id,))
       #     result = cursor.fetchone()
            result = []
            for row in self.result():  # cursor:
                result.append(row)
            return result

    def getResourcesByBuyerId(self, b_id):
      #  cursor = self.conn.cursor()
      #  query = "select r_id, r_category, r_name, rq_qty, rq_price, rq_date from resource natural inner join buyer natural inner join request where s_id = %s;"
      #  cursor.execute(query, (b_id,))
      result = []
      for row in self.result():  # cursor:
          result.append(row)
      return result

    def getBuyerByRegionNameAndLastName(self, region, name, lastname):
     #   cursor = self.conn.cursor()
     #   query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_name = %s and u_lastname = %s and u_region = %s;"
     #   cursor.execute(query, (name, lastname, region))
     #   result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByNameandLastName(self, name, lastname):
      #  cursor = self.conn.cursor()
      #  query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_name = %s and u_lastname = %s;"
      #  cursor.execute(query, (name, lastname))
     #   result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByNameandRegion(self, name, region):
      #  cursor = self.conn.cursor()
      #  query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_name = %s and u_region = %s;"
      #  cursor.execute(query, (name, region))
      #  result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByLastNameandRegion(self, lastname, region):
      #  cursor = self.conn.cursor()
      #  query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_lastname = %s and u_region = %s;"
      #  cursor.execute(query, (lastname, region))
      #  result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByName(self, name):
      #  cursor = self.conn.cursor()
       # query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_name = %s;"
      #  cursor.execute(query, (name,))
       # result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByLastName(self, lastname):
       # cursor = self.conn.cursor()
       # query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_lastnane = %s;"
       # cursor.execute(query, (lastname,))
       # result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result

    def getBuyerByRegion(self, region):
       # cursor = self.conn.cursor()
       # query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from buyer natural inner join user where u_region = %s;"
       # cursor.execute(query, (region,))
       # result = cursor.fetchone()
        result = []
        for row in self.result():  # cursor:
            result.append(row)
        return result