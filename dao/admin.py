from config.dbconfig import pg_config
import psycopg2


class AdminDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)




    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select admin_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from admin natural inner join users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, admin_id):
            cursor = self.conn.cursor()
            query = "select admin_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from admin natural inner join users where admin_id = %s;"
            cursor.execute(query, (admin_id,))
            result = cursor.fetchone()
            print(result)
            return result