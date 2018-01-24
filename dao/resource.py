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
            query = "select * from resource where r_name = %s;"
            cursor.execute(query, (r_name,))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getResourceByCategoryTypeAndName(self,r_category, r_type, r_name):
        cursor = self.conn.cursor()
        query = "select * from resource where r_category = %s and r_type = %s and r_name = %s;"
        cursor.execute(query, (r_category, r_type, r_name))
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

    def getResourceByCategoryAndType(self,r_category, r_type):
        cursor = self.conn.cursor()
        query = "select * from resource where r_category = %s and r_type = %s;"
        cursor.execute(query, (r_category, r_type))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByTypeAndName(self,r_type, r_name):
        cursor = self.conn.cursor()
        query = "select * from resource where r_type = %s and r_name = %s;"
        cursor.execute(query, (r_type, r_name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByResourceId(self, r_id):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from users natural inner join seller natural inner join resource natural inner join announcement where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByResourceId(self, r_id):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from users natural inner join buyer natural inner join resource natural inner join request where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByType(self, r_type):
            cursor = self.conn.cursor()
            query = "select * from resource where r_type = %s;"
            cursor.execute(query, (r_type,))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def update(self, r_id, r_name, r_category, r_type):
        cursor = self.conn.cursor()
        query = "update resource set r_name = %s, r_category = %s, r_type = %s where r_id = %s;"
        cursor.execute(query, (r_name, r_category, r_type,r_id,))
        self.conn.commit()
        return r_id

    def insert(self, r_name, r_category, r_type):
        cursor = self.conn.cursor()
        query = "insert into resource(r_name, r_category, r_type) values (%s, %s, %s) returning r_id;"
        cursor.execute(query, (r_name, r_category, r_type,))
        r_id = cursor.fetchone()[0]
        self.conn.commit()
        return r_id

    def delete(self, r_id):
        cursor = self.conn.cursor()
        query = "delete from resource where r_id = %s;"
        cursor.execute(query, (r_id,))
        self.conn.commit()
        return r_id

