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
        result['a_qty'] = row[4]
        result['a_total'] = row[5]
        result['a_date'] = row[6]
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
        seller_list = dao.getSellerById(s_id)
        if not seller_list:
            return jsonify(Error="Seller Not Found"), 404
        else:
            result = self.build_seller_dict(seller_list)
        return jsonify(Seller=result)

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
