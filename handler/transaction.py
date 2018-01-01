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
        result['r_category'] = row[2]
        result['r_type'] = row[3]
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
        s_id = args.get("s_id")
        b_id = args.get("b_id")
        t_date = args.get("t_date")
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

