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
        result['u_region'] = row[5]
        result['u_phone'] = row[6]
        result['u_age'] = row[7]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['rq_qty'] = row[3]
        result['rq_date'] = row[4]
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
        row = dao.getBuyerById(b_id)
        if not row:
            return jsonify(Error="Buyer Not Found"), 404
        else:
            part = self.build_buyer_dict(row)
        return jsonify(Buyer=part)

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

    def searchBuyer(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        region = args.get("region")
        dao = BuyerDAO()
        buyer_list = []
        if name and lastname and region:
            buyer_list = dao.getBuyerByRegionNameAndLastName(region, name,lastname)
        elif name and lastname:
            buyer_list = dao.getBuyerByNameandLastName(name, lastname)
        elif name and region:
            buyer_list = dao.getBuyerByNameandRegion(name, region)
        elif lastname and region:
            buyer_list = dao.getBuyerByLastNameandRegion(lastname, region)
        elif name:
            buyer_list = dao.getBuyerByName(name)
        elif lastname:
            buyer_list = dao.getBuyerByLastName(lastname)
        elif region:
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
