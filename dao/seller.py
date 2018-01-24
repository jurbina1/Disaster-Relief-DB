from config.dbconfig import pg_config
import psycopg2

class SellerDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllSellers(self):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerById(self, s_id):
            cursor = self.conn.cursor()
            query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where s_id = %s;"
            cursor.execute(query, (s_id,))
            result = cursor.fetchone()
            return result

    def getResourcesBySellerId(self, s_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type, a_qty, a_totalprice, a_date from resource natural inner join seller natural inner join announcement where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByRegionNameAndLastName(self, region, name, lastname):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_name = %s and u_lastname = %s and u_region = %s;"
        cursor.execute(query, (name, lastname, region))
        result = []
        for row in cursor:
           result.append(row)
        return result

    def getSellerByNameandLastName(self, name, lastname):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_name = %s and u_lastname = %s;"
        cursor.execute(query, (name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByNameandRegion(self, name, region):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_name = %s and u_region = %s;"
        cursor.execute(query, (name, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByLastNameandRegion(self, lastname, region):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_lastname = %s and u_region = %s;"
        cursor.execute(query, (lastname, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByName(self, name):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByLastName(self, lastname):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_lastnane = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from seller natural inner join users where u_region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySellerId(self, s_id):
        cursor = self.conn.cursor()
        query = "select t_id, s_id, b_id, ba_id, c_id, r_id, t_qty, t_total, t_date, t_donation, t_reservation from seller natural inner join transaction where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update(self, s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        cursor = self.conn.cursor()
        query = "with value as (select u_id from seller where s_id = %s) update users set u_name = %s, u_lastname = %s, u_email = %s, u_password = %s, u_address = %s, u_city = %s, u_region = %s, u_phone = %s, u_age, u_phone = %s, u_age = %s where u_id = (select u_id from value);"
        cursor.execute(query, (s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age,))
        self.conn.commit()
        return s_id

    def delete(self, s_id):
        cursor = self.conn.cursor()
        query = "delete from seller where pid = %s;"
        cursor.execute(query, (s_id,))
        self.conn.commit()
        return s_id

    def insert(self, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        cursor = self.conn.cursor()
        query = "with value as (insert into users(u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age) values(%s, %s, %s, %s, %s, %s, %s, %s, %s) returning u_id) insert into seller(u_id) select u_id from value returning s_id;"
        cursor.execute(query, (u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age,))
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id