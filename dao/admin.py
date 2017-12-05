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
               'u_name': "Victor",
               'u_lastname': "Schmidth",
               'u_email': "victor.schmidth35@hotmail.com",
               'u_password': "*****",
               'u_region': "Mayaguez",
               'u_phone': 7875492748,
               'u_age': 29,
           },
           {
               'admin_id': 2,
               'u_name': "Eileen",
               'u_lastname': "Cordova",
               'u_email': "eileen.cordova2@gmail.com",
               'u_password': "************",
               'u_region': "Ponce",
               'u_phone': 7879876543,
               'u_age': 27,
           },
           {
               'admin_id': 3,
               'u_name': "Fernando",
               'u_lastname': "Febus",
               'u_email': "fernando.febus39@yahoo.com",
               'u_password': "********",
               'u_region': "Arecibo",
               'u_phone': 7871234567,
               'u_age': 19,
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