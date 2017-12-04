from flask import jsonify
from dao.seller import SellerDAO


class SellerHandler:
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

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['a_qty'] = row[3]
        result['a_price'] = row[4]
        result['a_date'] = row[5]
        return result

    def getAllSellers(self):
        dao = SellerDAO()
        seller_list = dao.getAllSellers()
        if not seller_list:
            return jsonify(Error="Seller Not Found"), 404
        else:
            result_list = []
            for row in seller_list:
                result = self.build_seller_dict(row)
                result_list.append(result)
            return jsonify(Sellers=result_list)

    def getSellerById(self, s_id):
        dao = SellerDAO()
        row = dao.getSellerById(s_id)
        if not row:
            return jsonify(Error="Seller Not Found"), 404
        else:
            seller = self.build_seller_dict(row)
        return jsonify(Seller=seller)

    def getResourcesBySellerId(self, s_id):
        dao = SellerDAO()
        seller_list = dao.getResourcesBySellerId(s_id)
        if not seller_list:
            return jsonify(Error="Seller Not Found"), 404
        else:
            result_list = []
            for row in seller_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    def searchSeller(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        region = args.get("region")
        dao = SellerDAO()
        seller_list = []
        if (len(args) == 3) and name and lastname and region:
            seller_list = dao.getSellerByRegionNameAndLastName(region, name,lastname)
        elif (len(args) == 2) and name and lastname:
            seller_list = dao.getSellerByNameandLastName(name, lastname)
        elif (len(args) == 2) and name and region:
            seller_list = dao.getSellerByNameandRegion(name, region)
        elif (len(args) == 2) and lastname and region:
            seller_list = dao.getSellerByLastNameandRegion(lastname, region)
        elif (len(args) == 1) and name:
            seller_list = dao.getSellerByName(name)
        elif (len(args) == 1) and lastname:
            seller_list = dao.getSellerByLastName(lastname)
        elif (len(args) == 1) and region:
            seller_list = dao.getSellerByRegion(region)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not seller_list:
            return jsonify(Error="Seller Not Found"), 404
        else:
            result_list = []
            for row in seller_list:
                result = self.build_seller_dict(row)
                result_list.append(result)
            return jsonify(Sellers=result_list)