from flask import jsonify
from dao.transaction import TransactionDAO


class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        result['t_id'] = row[0]
        result['s_id'] = row[1]
        result['b_id'] = row[2]
        result['r_id'] = row[3]
        result['t_qty'] = row[4]
        result['t_total'] = row[5]
        result['t_date'] = row[6]
        result['t_donation'] = row[7]
        result['t_reservation'] = row[8]
        return result

    def build_buyer_dict(self, row):
        result = {}
        result['b_id'] = row[0]
        result['u_name'] = row[1]
        result['u_lastname'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_region'] = row[5]
        result['u_phone'] = row[6]
        result['u_age'] = row[7]
        return result

    def build_seller_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['u_name'] = row[1]
        result['u_lastname'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_region'] = row[5]
        result['u_phone'] = row[6]
        result['u_age'] = row[7]
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
        row = dao.getTransactionById(t_id)
        if not row:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            transaction = self.build_transaction_dict(row)
        return jsonify(Transaction=transaction)

    def getBuyerByTransactionId(self, t_id):
        dao = TransactionDAO()
        buyer_list = dao.getBuyerByTransactionId(t_id)
        if not buyer_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in buyer_list:
                result = self.build_buyer_dict(row)
                result_list.append(result)
            return jsonify(Buyer=result_list)

    def getSellerByTransactionId(self, t_id):
        dao = TransactionDAO()
        seller_list = dao.getSellerByTransactionId(t_id)
        if not seller_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in seller_list:
                result = self.build_seller_dict(row)
                result_list.append(result)
            return jsonify(Sellerr=result_list)

    def searchTransactions(self, args):
        s_id = args.get("s_id")
        b_id = args.get("b_id")
        t_date = args.get("t_date")
        dao = TransactionDAO()
        transaction_list = []
        if s_id and b_id and t_date:
            transaction_list = dao.getTransactionByDateSellerandBuyer(s_id, b_id, t_date)
        elif s_id and b_id:
            transaction_list = dao.getTransactionBySellerandBuyer(s_id, b_id)
        elif s_id and t_date:
            transaction_list = dao.getTransactionBySellerandDate(s_id, t_date)
        elif t_date and b_id:
            transaction_list = dao.getTransactionByDateandBuyer(t_date, b_id)
        elif s_id:
            transaction_list = dao.getTransactionBySeller(s_id)
        elif b_id:
            transaction_list = dao.getTransactionByBuyer(b_id)
        elif t_date:
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

