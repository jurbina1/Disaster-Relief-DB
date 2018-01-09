from flask import jsonify
from dao.creditcard import CreditCardDAO


class CreditCardHandler:
    def build_creditcard_dict(self, row):
        result = {}
        result['c_id'] = row[0]
        result['b_id'] = row[1]
        result['c_name'] = row[2]
        result['c_number'] = row[3]
        result['c_cvv'] = row[4]
        result['c_expdate'] = row[5]
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

    def getAllCreditCards(self):
        dao = CreditCardDAO()
        creditcard_list = dao.getAllCreditCards()
        if not creditcard_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result_list = []
            for row in creditcard_list:
                result = self.build_creditcard_dict(row)
                result_list.append(result)
            return jsonify(Credit_Cards=result_list)

    def getCreditCardById(self, c_id):
        dao = CreditCardDAO()
        creditcard_list = dao.getCreditCardById(c_id)
        if not creditcard_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result = self.build_creditcard_dict(creditcard_list)
        return jsonify(Credit_Card=result)

    def getBuyerByCreditCardId(self, c_id):
        dao = CreditCardDAO()
        creditcard_list = dao.getCreditCardById(c_id)
        if not creditcard_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result = self.build_buyer_dict(creditcard_list)
        return jsonify(Buyer=result)

    def searchCreditCards(self, args):
        name = args.get("name")
        b_id = args.get("b_id")
        dao = CreditCardDAO()
        creditcard_list = []
        if (len(args) == 2) and name and b_id:
            creditcard_list = dao.getCreditCardByNameandBuyer(name, b_id)
        elif (len(args) == 1) and name:
            creditcard_list = dao.getCreditCardByName(name)
        elif (len(args) == 1) and b_id:
            creditcard_list = dao.getCreditCardByBuyer(b_id)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not creditcard_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result_list = []
            for row in creditcard_list:
                result = self.build_creditcard_dict(row)
                result_list.append(result)
            return jsonify(CreditCards=result_list)