#from config.dbconfig import pg_config
#import psycopg2


class AdminDAO:
   # def __init__(self):
#
 #       connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
  #                                                          pg_config['user'],
   #                                                         pg_config['passwd'])
    #    self.conn = psycopg2._connect(connection_url)


    def result(self):
       result = [
           {
               'admin_id': 1,
               'u_name': "Sara",
               'u_lastname': "Valle",
               'u_email': "sara.valle2@hotmail.com",
               'u_password': "***********",
               'u_region': "San Juan",
               'u_phone': 7871234567,
               'u_age': 75,
           },
           {
               'admin_id': 2,
               'u_name': "Jocelyn",
               'u_lastname': "Finelli",
               'u_email': "jocelyn.finelli@gmail.com",
               'u_password': "*********",
               'u_region': "Bayamon",
               'u_phone': 7870987654,
               'u_age': 20,
           },
           {
               'admin_id': 3,
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


    def getAllAdmins(self):
      #  cursor = self.conn.cursor()
      #  query = "select admin_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from admin natural inner join user;"
      #  cursor.execute(query)
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getAdminById(self, admin_id):
            #cursor = self.conn.cursor()
       #     query = "select b_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from admin natural inner join user where admin_id = %s;"
       #     cursor.execute(query, (admin_id,))
       #     result = cursor.fetchone()
            result = []
            for row in self.result():  # cursor:
                result.append(row)
            return result