from config.dbconfig import pg_config
import psycopg2


class BuyerDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)



    def getAllBuyers(self):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerById(self, b_id):
            cursor = self.conn.cursor()
            query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where b_id = %s;"
            cursor.execute(query, (b_id,))
            result = cursor.fetchone()
            return result

    def getResourcesByBuyerId(self, b_id):
        cursor = self.conn.cursor()
        query = "select r_id, r_name, r_category, r_type, rq_qty, rq_date from resource natural inner join buyer natural inner join request where b_id = %s;"
        cursor.execute(query, (b_id,))
        result = []
        for row in cursor:
          result.append(row)
        return result

    def getBuyerByRegionNameAndLastName(self, region, name, lastname):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_name = %s and u_lastname = %s and u_region = %s;"
        cursor.execute(query, (name, lastname, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByNameandLastName(self, name, lastname):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_name = %s and u_lastname = %s;"
        cursor.execute(query, (name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByNameandRegion(self, name, region):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_name = %s and u_region = %s;"
        cursor.execute(query, (name, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByLastNameandRegion(self, lastname, region):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_lastname = %s and u_region = %s;"
        cursor.execute(query, (lastname, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByName(self, name):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByLastName(self, lastname):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_lastnane = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBuyerByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from buyer natural inner join users where u_region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByBuyerId(self, b_id):
        cursor = self.conn.cursor()
        query = "select t_id, s_id, b_id, ba_id, c_id, r_id, t_qty, t_total, t_date, t_donation, t_reservation from buyer natural inner join transaction where b_id = %s;"
        cursor.execute(query, (b_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update(self, b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        cursor = self.conn.cursor()
        query = "with value as (select u_id from buyer where b_id = %s) update users set u_name = %s, u_lastname = %s, u_email = %s, u_password = %s, u_address = %s, u_city = %s, u_region = %s, u_phone = %s, u_age = %s where u_id = (select u_id from value);"
        cursor.execute(query,(b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age,))
        self.conn.commit()
        return b_id

    def delete(self, b_id):
        cursor = self.conn.cursor()
        query = "delete from buyer where b_id = %s;"
        cursor.execute(query, (b_id,))
        self.conn.commit()
        return b_id

    def insert(self, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        cursor = self.conn.cursor()
        query = "with value as (insert into users(u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age) values(%s, %s, %s, %s, %s, %s, %s, %s, %s) returning u_id) insert into buyer (u_id) select u_id from value returning b_id;"
        cursor.execute(query, (u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age,))
        b_id = cursor.fetchone()[0]
        self.conn.commit()
        return b_id