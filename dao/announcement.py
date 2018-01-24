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
        query = "select * from announcement where a_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result

    def getResourcesByAnnouncementId(self, a_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type from announcement natural inner join resource where a_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result

    def getSellerByAnnouncementId(self, a_id):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from announcement natural inner join buyer natural inner join users where a_id = %s;"
        cursor.execute(query, (a_id,))
        result = cursor.fetchone()
        return result

    def getAnnouncementBySellerResourceandDate(self, a_date, s_id, r_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_date = %s and s_id = %s and r_id = %s;"
        cursor.execute(query, (a_date, s_id, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySellerandResource(self, s_id, r_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where s_id = %s and r_id = %s;"
        cursor.execute(query, (s_id, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySellerandDate(self, s_id, a_date):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_date = %s and s_id = %s;"
        cursor.execute(query, (a_date, s_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByResourceandDate(self, r_id, a_date):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_date = %s and r_id = %s;"
        cursor.execute(query, (a_date, r_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementBySeller(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByResource(self, r_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByDate(self, a_date):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_date = %s;"
        cursor.execute(query, (a_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAvailableAnnouncements(self):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_available > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableResources(self):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type, a_qty, a_price, a_totalprice, a_available, a_date from announcement natural inner join resource where a_available>0 order by r_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAvailableResourcesByCity(self, city):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type, a_qty, a_price, a_totalprice, a_available, a_date from announcement natural inner join resource natural inner join seller natural inner join users where a_available>0 and u_city = %s order by r_name;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAvailableResourcesByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type, a_qty, a_price, a_totalprice, a_available, a_date from announcement natural inner join resource natural inner join seller natural inner join users where a_available>0 and u_region = %s order by r_name;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update(self, a_id, s_id, r_id, a_qty, a_price, a_totalprice, a_available):
        cursor = self.conn.cursor()
        query = "update announcement set s_id = %s, r_id = %s, a_qty = %s, a_price = %s, a_totalprice = %s, a_available = %s where a_id = %s;"
        cursor.execute(query, (s_id, r_id, a_qty, a_price, a_totalprice, a_available, a_id,))
        self.conn.commit()
        return a_id

    def delete(self, a_id):
        cursor = self.conn.cursor()
        query = "delete from announcement where a_id = %s;"
        cursor.execute(query, (a_id,))
        self.conn.commit()
        return a_id

    def insert(self, s_id, r_id, a_qty, a_price, a_totalprice, a_available):
        cursor = self.conn.cursor()
        query = "insert into parts(s_id, r_id, a_qty, a_price, a_totalprice, a_available) values (%s, %s, %s, %s, %s, %s) returning a_id;"
        cursor.execute(query, (s_id, r_id, a_qty, a_price, a_totalprice, a_available,))
        a_id = cursor.fetchone()[0]
        self.conn.commit()
        return a_id
