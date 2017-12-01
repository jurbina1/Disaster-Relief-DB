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
        return result

    def getAllSellers(self):
        dao = SellerDAO()
        sellers_list = dao.getAllSellers()
        result_list = []
        for row in sellers_list:
            result = self.build_seller_dict(row)
            result_list.append(result)
        return jsonify(Sellers=result_list)

    def getSupplierById(self, s_id):
        dao = SellerDAO()
        row = dao.getSellerById(s_id)
        if not row:
            return jsonify(Error="Seller Not Found"), 404
        else:
            part = self.build_seller_dict(row)
        return jsonify(Seller=part)

    def getResourcesBySellerId(self, s_id):
        dao = SellerDAO()
        resource_list = dao.getResourcesBySellerId(s_id)
        if not resource_list:
            return jsonify(Error="Seller Not Found"), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)
