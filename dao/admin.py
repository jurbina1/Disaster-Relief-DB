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
        query = "select admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from admin natural inner join users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, admin_id):
            cursor = self.conn.cursor()
            query = "select admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from admin natural inner join users where admin_id = %s;"
            cursor.execute(query, (admin_id,))
            result = cursor.fetchone()
            print(result)
            return result

    def insert(self, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        cursor = self.conn.cursor()
        query = "with value as (insert into users(u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age) values(%s, %s, %s, %s, %s, %s, %s, %s, %s) returning u_id) insert into admin(u_id) select u_id from value returning admin_id;"
        cursor.execute(query, (u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age,))
        admin_id = cursor.fetchone()[0]
        self.conn.commit()
        return admin_id

    def delete(self, admin_id):
        cursor = self.conn.cursor()
        query = "delete from admin where admin_id = %s;"
        cursor.execute(query, (admin_id,))
        self.conn.commit()
        return admin_id

    def update(self, admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        cursor = self.conn.cursor()
        query = "with value as (select u_id from admin where admin_id = %s) update users set u_name = %s, u_lastname = %s, u_email = %s, u_password = %s, u_address = %s, u_city = %s, u_region = %s, u_phone = %s, u_age = %s where u_id = (select u_id from value);"
        cursor.execute(query, (admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age,))
        self.conn.commit()
        return admin_id
