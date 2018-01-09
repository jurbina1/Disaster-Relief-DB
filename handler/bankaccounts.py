from flask import jsonify
from dao.bankaccounts import BankAccountDAO


class BankAccountHandler:
    def build_bankaccount_dict(self, row):
        result = {}
        result['ba_id'] = row[0]
        result['s_id'] = row[1]
        result['ba_number'] = row[2]
        result['ba_bank'] = row[3]
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

    def getAllBankAccounts(self):
        dao = BankAccountDAO()
        bankaccount_list = dao.getAllBankAccounts()
        if not bankaccount_list:
            return jsonify(Error="Bank Account Not Found"), 404
        else:
            result_list = []
            for row in bankaccount_list:
                result = self.build_bankaccount_dict(row)
                result_list.append(result)
            return jsonify(Bank_Accounts=result_list)

    def getBankAccountById(self, ba_id):
        dao = BankAccountDAO()
        bankaccount_list = dao.getBankAccountById(ba_id)
        if not bankaccount_list:
            return jsonify(Error="Bank Account Not Found"), 404
        else:
            result = self.build_bankaccount_dict(bankaccount_list)
        return jsonify(Bank_Account=result)

    def getSellerByBankAccountId(self, ba_id):
        dao = BankAccountDAO()
        bankaccount_list = dao.getSellerByBankAccountId(ba_id)
        if not bankaccount_list:
            return jsonify(Error="Bank Account Not Found"), 404
        else:
            result = self.build_seller_dict(bankaccount_list)
        return jsonify(Seller = result)


    def searchBankAccounts(self, args):
        ba_bank = args.get("bank")
        s_id = args.get("seller")
        dao = BankAccountDAO()
        bankaccount_list = []
        if (len(args) == 2) and ba_bank and s_id:
            bankaccount_list = dao.getBankAccountByBankandSeller(ba_bank, s_id)
        elif (len(args) == 1) and ba_bank:
            bankaccount_list = dao.getBankAccountByBank(ba_bank)
        elif (len(args) == 1) and s_id:
            bankaccount_list = dao.getBankAccountBySeller(s_id)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not bankaccount_list:
            return jsonify(Error="Bank Account Not Found"), 404
        else:
            result_list = []
            for row in bankaccount_list:
                result = self.build_bankaccount_dict(row)
                result_list.append(result)
            return jsonify(Bank_Accounts=result_list)