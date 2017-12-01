from config.dbconfig import pg_config
import psycopg2

class ResourceDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, r_id):
            cursor = self.conn.cursor()
            query = "select * from resource where r_id = %s;"
            cursor.execute(query, (r_id,))
            result = cursor.fetchone()
            return result

    def getResourceByCategory(self, r_category):
            cursor = self.conn.cursor()
            query = "select * from resource where r_category = %s;"
            cursor.execute(query, (r_category,))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getResourceByName(self, r_name):
            cursor = self.conn.cursor()
            query = "select * from resource where r_category = %s;"
            cursor.execute(query, (r_name,))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getResourceByCategoryAndName(self,r_category, r_name):
        cursor = self.conn.cursor()
        query = "select * from resource where r_category = %s and r_name = %s;"
        cursor.execute(query, (r_category, r_name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByResourceId(self, r_id):
        cursor = self.conn.cursor()
        query = "select u_id, u_name, u_lastname, u_email, u_region, u_phone, u_age from user natural inner join seller natural inner join resource natural inner join annoucements where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByResourceId(self, r_id):
        cursor = self.conn.cursor()
        query = "select u_id, u_name, u_lastname, u_email, u_region, u_phone, u_age from user natural inner join buyer natural inner join resource natural inner join requests where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result