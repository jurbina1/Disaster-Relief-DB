#from config.dbconfig import pg_config
#import psycopg2

class BankAccountDAO:
 #   def __init__(self):
#
#        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
#                                                            pg_config['user'],
#                                                            pg_config['passwd'])
#        self.conn = psycopg2._connect(connection_url)

    def result(self):
        result = [
            {
                'ba_id':1,
                's_id':3,
                'ba_rtnumber':987654321,
                'ba_number':12345678901234,
                'ba_bank': "Chase"
            },
            {
                'ba_id': 2,
                's_id': 1,
                'ba_rtnumber': 123456789,
                'ba_number': 98076543210987,
                'ba_bank': "First Bank"
            },
            {
                'ba_id': 3,
                's_id': 2,
                'ba_rtnumber': 456789012,
                'ba_number': 67890123456789,
                'ba_bank': "Santander"
            }
        ]
        return result

    def getBankAccountBySeller(self, s_id):
#        cursor = self.conn.cursor()
#        query = "select * from bankaccount where s_id = %s;"
#        cursor.execute(query, (s_id,))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getBankAccountByBank(self, ba_bank):
 #       cursor = self.conn.cursor()
 #       query = "select * from bankaccount where ba_bank = %s;"
 #       cursor.execute(query, (ba_bank,))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getBankAccountByBankandSeller(self, ba_bank, s_id):
 #       cursor = self.conn.cursor()
 #       query = "select * from bankaccount where s_id = %s and ba_bank = %s;"
 #       cursor.execute(query, (s_id, ba_bank))
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getSellerByBankAccountId(self, ba_id):
  #      cursor = self.conn.cursor()
  #      query = "select s_id, u_name, u_lastname, u_email, u_password, u_region, u_phone, u_age from bankaccount natural inner join seller natural inner join user where ba_id = %s;"
  #      cursor.execute(query, (ba_id,))
  #      result = cursor.fetchone()
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getBankAccountById(self, ba_id):
   #     cursor = self.conn.cursor()
   #     query = "select * from bankaccount where ba_id = %s;"
   #     cursor.execute(query, (ba_id,))
    #    result = cursor.fetchone()
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result

    def getAllBankAccounts(self):
    #    cursor = self.conn.cursor()
    #    query = "select * from bankaccount;"
    #    cursor.execute(query)
        result = []
        for row in self.result():#cursor:
            result.append(row)
        return result