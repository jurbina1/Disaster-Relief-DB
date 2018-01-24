from config.dbconfig import pg_config
import psycopg2

class BankAccountDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getBankAccountBySeller(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from bankaccount where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByBank(self, ba_bank):
        cursor = self.conn.cursor()
        query = "select * from bankaccount where ba_bank = %s;"
        cursor.execute(query, (ba_bank,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBankAccountByBankandSeller(self, ba_bank, s_id):
        cursor = self.conn.cursor()
        query = "select * from bankaccount where s_id = %s and ba_bank = %s;"
        cursor.execute(query, (s_id, ba_bank))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSellerByBankAccountId(self, ba_id):
        cursor = self.conn.cursor()
        query = "select s_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age from bankaccount natural inner join seller natural inner join users where ba_id = %s;"
        cursor.execute(query, (ba_id,))
        result = cursor.fetchone()
        return result

    def getBankAccountById(self, ba_id):
        cursor = self.conn.cursor()
        query = "select * from bankaccount where ba_id = %s;"
        cursor.execute(query, (ba_id,))
        result = cursor.fetchone()
        return result

    def getAllBankAccounts(self):
        cursor = self.conn.cursor()
        query = "select * from bankaccount;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update(self, ba_id, s_id, ba_number, ba_bank):
        cursor = self.conn.cursor()
        query = "update bankaccount set s_id = %s, ba_number = %s, ba_bank = %s where ba_id = %s;"
        cursor.execute(query, (s_id, ba_number, ba_bank,  ba_id,))
        self.conn.commit()
        return ba_id

    def delete(self, ba_id):
        cursor = self.conn.cursor()
        query = "delete from bankaccount where ba_id = %s;"
        cursor.execute(query, (ba_id,))
        self.conn.commit()
        return ba_id

    def insert(self, s_id, ba_number, ba_bank):
        cursor = self.conn.cursor()
        query = "insert into bankaccount(s_id, ba_number, ba_bank) values (%s, %s, %s) returning ba_id;"
        cursor.execute(query, (s_id, ba_number, ba_bank,))
        ba_id = cursor.fetchone()[0]
        self.conn.commit()
        return ba_id