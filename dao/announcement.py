from config.dbconfig import pg_config
import psycopg2


class AnnouncementDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAnnouncements(self):
        cursor = self.conn.cursor()
        query = "select * from announcement;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementById(self, a_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where t_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result

    def getResourcesByAnnouncementId(self, a_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_category, r_name, r_description from announcement natural inner join resource where a_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result

    def getSellerByAnnouncementId(self, a_id):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from announcement natural inner join buyer natural inner join user where a_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result

    def getAnnouncementBySellerResourceandDate(self, a_date, s_id, r_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where a_date = %s and s_id = %s and r_id = %s;"
        cursor.execute(query, (a_date, s_id, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySellerandResource(self, s_id, r_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where s_id = %s and r_id = %s;"
        cursor.execute(query, (s_id, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySellerandDate(self, s_id, a_date):
        cursor = self.conn.cursor()
        query = "select * from transaction where a_date = %s and s_id = %s;"
        cursor.execute(query, (a_date, s_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByResourceandDate(self, r_id, a_date):
        cursor = self.conn.cursor()
        query = "select * from transaction where a_date = %s and r_id = %s;"
        cursor.execute(query, (a_date, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySeller(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByResource(self, r_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByDate(self, a_date):
        cursor = self.conn.cursor()
        query = "select * from transaction where a_date = %s;"
        cursor.execute(query, (a_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

