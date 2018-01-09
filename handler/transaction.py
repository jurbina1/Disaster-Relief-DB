from flask import jsonify
from dao.transaction import TransactionDAO


class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        result['t_id'] = row[0]
        result['s_id'] = row[1]
        result['b_id'] = row[2]
        result['ba_id'] = row[3]
        result['c_id'] = row[4]
        result['r_id'] = row[5]
        result['t_qty'] = row[6]
        result['t_total'] = row[7]
        result['t_date'] = row[8]
        result['t_donation'] = row[9]
        result['t_reservation'] = row[10]
        return result

    def build_buyer_dict(self, row):
        result = {}
        result['b_id'] = row[0]
        result['u_name'] = row[1]
        result['u_lastname'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_address'] = row[5]
        result['u_city'] = row[6]
        result['u_region'] = row[7]
        result['u_phone'] = row[8]
        result['u_age'] = row[9]
        return result

    def build_seller_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['u_name'] = row[1]
        result['u_lastname'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_address'] = row[5]
        result['u_city'] = row[6]
        result['u_region'] = row[7]
        result['u_phone'] = row[8]
        result['u_age'] = row[9]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_name'] = row[1]
        if(row[2]==1):
            result['r_category'] = "Water"
            if (row[3]==1):
                result['r_type'] = "Bottled Water"
            elif(row[3]==2):
                result['r_type'] = "1 Gallon Water"
        elif (row[2] == 2):
            result['r_category'] = "Fuel"
            if (row[3]==1):
                result['r_type'] = "Diesel"
            elif(row[3]==2):
                result['r_type'] = "Gasoline"
            else:
                result['r_type'] = "Propane"
        elif (row[2] == 3):
            result['r_category'] = "Baby Food"
            result['r_type'] = "Baby Food"
        elif (row[2] == 4):
            result['r_category'] = "Medications"
            result['r_type'] = "Medications"
        elif (row[2] == 5):
            result['r_category'] = "Canned Food"
            result['r_type'] = "Canned Food"
        elif (row[2] == 6):
            result['r_category'] = "Dry Food"
            result['r_type'] = "Dry Food"
        elif (row[2] == 7):
            result['r_category'] = "Ice"
            result['r_type'] = "Ice"
        elif (row[2] == 8):
            result['r_category'] = "Medical Devices"
            result['r_type'] = "Medical Devices"
        elif (row[2] == 9):
            result['r_category'] = "Heavy Equipment"
            result['r_type'] = "Heavy Equipment"
        elif (row[2] == 10):
            result['r_category'] = "Tools"
            result['r_type'] = "Tools"
        elif (row[2] == 11):
            result['r_category'] = "Clothing"
            result['r_type'] = "Clothing"
        elif (row[2] == 12):
            result['r_category'] = "Batteries"
            result['r_type'] = "Batteries"
        else:
            result['r_category'] = "Power Generators"
            if (row[3]==1):
                result['r_type'] = "Diesel Power Generator"
            elif(row[3]==2):
                result['r_type'] = "Gasoline Power Generator"
            else:
                result['r_type'] = "Propane Power Generator"
        return result

    def build_creditcard_dict(self, row):
        result = {}
        result['c_id'] = row[0]
        result['b_id'] = row[1]
        result['c_name'] = row[2]
        result['c_number'] = row[3]
        result['c_cvv'] = row[4]
        result['c_expdate'] = row[5]
        return result

    def build_bankaccount_dict(self, row):
        result = {}
        result['ba_id'] = row[0]
        result['s_id'] = row[1]
        result['ba_number'] = row[2]
        result['ba_bank'] = row[3]
        return result

    def getAllTransactions(self):
        dao = TransactionDAO()
        transaction_list = dao.getAllTransactions()
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transaction_dict(row)
                result_list.append(result)
            return jsonify(Transactions=result_list)

    def getTransactionById(self, t_id):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionById(t_id)
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result = self.build_transaction_dict(transaction_list)
        return jsonify(Transaction=result)

    def getResourcesByTransactionId(self, t_id):
        dao = TransactionDAO()
        transaction_list = dao.getResourceByTransactionId(t_id)
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result = self.build_resource_dict(transaction_list)
        return jsonify(Resource=result)


    def getBuyerByTransactionId(self, t_id):
        dao = TransactionDAO()
        transaction_list = dao.getBuyerByTransactionId(t_id)
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result = self.build_buyer_dict(transaction_list)
        return jsonify(Buyer=result)

    def getSellerByTransactionId(self, t_id):
        dao = TransactionDAO()
        transaction_list = dao.getSellerByTransactionId(t_id)
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result = self.build_seller_dict(transaction_list)
        return jsonify(Seller=result)

    def searchTransactions(self, args):
        s_id = args.get("seller")
        b_id = args.get("buyer")
        t_date = args.get("date")
        dao = TransactionDAO()
        transaction_list = []
        if (len(args) == 3) and s_id and b_id and t_date:
            transaction_list = dao.getTransactionByDateSellerandBuyer(s_id, b_id, t_date)
        elif (len(args) == 2) and s_id and b_id:
            transaction_list = dao.getTransactionBySellerandBuyer(s_id, b_id)
        elif (len(args) == 2) and s_id and t_date:
            transaction_list = dao.getTransactionBySellerandDate(s_id, t_date)
        elif (len(args) == 2) and t_date and b_id:
            transaction_list = dao.getTransactionByDateandBuyer(t_date, b_id)
        elif (len(args) == 1) and s_id:
            transaction_list = dao.getTransactionBySeller(s_id)
        elif (len(args) == 1) and b_id:
            transaction_list = dao.getTransactionByBuyer(b_id)
        elif (len(args) == 1) and t_date:
            transaction_list = dao.getTransactionByDate(t_date)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transaction_dict(row)
                result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionTotalSum(self):
        dao = TransactionDAO()
        sum = dao.getTransactionTotalSum()
        if not sum:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            return jsonify(TransactionsSum=sum[0])

    def getTransactionSum(self, args):
        s_id = args.get("seller")
        b_id = args.get("buyer")
        t_date = args.get("date")
        r_id = args.get("resource")
        region = args.get("region")
        city = args.get("city")
        dao = TransactionDAO()
        sum=[]
        if (len(args) == 1) and s_id:
            sum = dao.getTransactionSumBySeller(s_id)
        elif (len(args) == 1) and b_id:
            sum = dao.getTransactionSumByBuyer(b_id)
        elif (len(args) == 1) and t_date:
            sum = dao.getTransactionSumByDate(t_date)
        elif (len(args) == 1) and r_id:
            sum = dao.getTransactionSumByResource(r_id)
        elif (len(args) == 1) and region:
            sum = dao.getTransactionSumByRegion(region)
        elif (len(args) == 1) and city:
            sum = dao.getTransactionSumByCity(city)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not sum:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            if sum[0] is None:
                sum = []
                sum.append(0)
            return jsonify(TransactionsSum=sum[0])

    def getDonations(self):
        dao = TransactionDAO()
        transaction_list = dao.getDonations()
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transaction_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def getReservations(self):
        dao = TransactionDAO()
        transaction_list = dao.getReservations()
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transaction_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def getCreditCardByTransactionId(self, t_id):
        dao = TransactionDAO()
        transaction_list = dao.getCreditCardByTransactionId(t_id)
        if not transaction_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result = self.build_creditcard_dict(transaction_list)
        return jsonify(CreditCard=result)

    def getBankAccountByTransactionId(self, t_id):
        dao = TransactionDAO()
        transaction_list = dao.getBankAccountByTransactionId(t_id)
        if not transaction_list:
            return jsonify(Error="Bank Account Not Found"), 404
        else:
            result = self.build_bankaccount_dict(transaction_list)
        return jsonify(BankAccount=result)
