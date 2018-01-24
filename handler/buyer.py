from flask import jsonify
from dao.buyer import BuyerDAO


class BuyerHandler:
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

    def build_buyer_attributes(self, b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        result = {}
        result['b_id'] = b_id
        result['u_name'] = u_name
        result['u_lastname'] = u_lastname
        result['u_email'] = u_email
        result['u_password'] = u_password
        result['u_address'] = u_address
        result['u_city'] =  u_city
        result['u_region'] = u_region
        result['u_phone'] = u_phone
        result['u_age'] = u_age
        return result

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
        result['rq_qty'] = row[4]
        result['rq_date'] = row[5]
        return result

    def getAllBuyers(self):
        dao = BuyerDAO()
        buyer_list = dao.getAllBuyers()
        if not buyer_list:
            return jsonify(Error="Buyer Not Found"), 404
        else:
            result_list = []
            for row in buyer_list:
                result = self.build_buyer_dict(row)
                result_list.append(result)
            return jsonify(Buyers=result_list)

    def getBuyerById(self, b_id):
        dao = BuyerDAO()
        buyer_list = dao.getBuyerById(b_id)
        if not buyer_list:
            return jsonify(Error="Buyer Not Found"), 404
        else:
            result = self.build_buyer_dict(buyer_list)
        return jsonify(Buyer=result)

    def getResourcesByBuyerId(self, b_id):
        dao = BuyerDAO()
        buyer_list = dao.getResourcesByBuyerId(b_id)
        if not buyer_list:
            return jsonify(Error="Buyer Not Found"), 404
        else:
            result_list = []
            for row in buyer_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    def searchBuyers(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        region = args.get("region")
        dao = BuyerDAO()
        buyer_list = []
        if (len(args) == 3) and name and lastname and region:
            buyer_list = dao.getBuyerByRegionNameAndLastName(region, name,lastname)
        elif (len(args) == 2) and name and lastname:
            buyer_list = dao.getBuyerByNameandLastName(name, lastname)
        elif (len(args) == 2) and name and region:
            buyer_list = dao.getBuyerByNameandRegion(name, region)
        elif (len(args) == 2) and lastname and region:
            buyer_list = dao.getBuyerByLastNameandRegion(lastname, region)
        elif (len(args) == 1) and name:
            buyer_list = dao.getBuyerByName(name)
        elif (len(args) == 1) and lastname:
            buyer_list = dao.getBuyerByLastName(lastname)
        elif (len(args) == 1) and region:
            buyer_list = dao.getBuyerByRegion(region)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not buyer_list:
            return jsonify(Error="Buyer Not Found"), 404
        else:
            result_list = []
            for row in buyer_list:
                result = self.build_buyer_dict(row)
                result_list.append(result)
            return jsonify(Buyers=result_list)

    def getTransactionsByBuyerId(self, b_id):
        dao = BuyerDAO()
        transaction_list = dao.getTransactionsByBuyerId(b_id)
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transaction_dict(row)
                result_list.append(result)
            return jsonify(Transactions=result_list)

    def insertBuyer(self, form):
        if len(form) != 9:
            return jsonify(Error = "Malformed post request"), 400
        else:
            u_name = form['u_name']
            u_lastname = form['u_lastname']
            u_email = form['u_email']
            u_password = form['u_password']
            u_address = form['u_address']
            u_city = form['u_city']
            u_region = form['u_region']
            u_phone = form['u_phone']
            u_age = form['u_age']
            if u_name and u_lastname and u_email and u_password and u_address and u_city and u_region and u_phone and u_age:
                dao = BuyerDAO()
                b_id = dao.insert(u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                result = self.build_buyer_attributes(b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                return jsonify(Buyer=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteBuyer(self, b_id):
        dao = BuyerDAO()
        if not dao.getBuyerById(b_id):
            return jsonify(Error = "Buyer not found."), 404
        else:
            dao.delete(b_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateBuyer(self, b_id, form):
        dao = BuyerDAO()
        if not dao.getBuyerById(b_id):
            return jsonify(Error = "Buyer not found."), 404
        else:
            if len(form) != 9:
                return jsonify(Error="Malformed update request"), 400
            else:
                u_name = form['u_name']
                u_lastname = form['u_lastname']
                u_email = form['u_email']
                u_password = form['u_password']
                u_address = form['u_address']
                u_city = form['u_city']
                u_region = form['u_region']
                u_phone = form['u_phone']
                u_age = form['u_age']
                if u_name and u_lastname and u_email and u_password and u_address and u_city and u_region and u_phone and u_age:
                    dao = BuyerDAO()
                    dao.update(b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                    result = self.build_buyer_attributes(b_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                    return jsonify(Buyer=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
