from flask import jsonify
from dao.resource import ResourceDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_name'] = row[1]
        result['r_category'] = row[2]
        result['r_type'] = row[3]
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

    def getAllResources(self):
        dao = ResourceDAO()
        resources_list = dao.getAllResources()
        result_list = []
        if not resources_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            for row in resources_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, r_id):
        dao = ResourceDAO()
        resources_list= dao.getResourceById(r_id)
        if not resources_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result = self.build_resource_dict(resources_list)
        return jsonify(Resource=result)

    def searchResource(self, args):
        category = args.get("category")
        name = args.get("name")
        type = args.get("type")
        dao = ResourceDAO()
        resources_list = []
        if (len(args) == 3) and category and name and type:
            resources_list = dao.getResourceByCategoryTypeAndName(category, type, name)
        elif (len(args) == 2) and category and name:
            resources_list = dao.getResourceByCategoryAndName(category, name)
        elif (len(args) == 2) and category and type:
            resources_list = dao.getResourceByCategoryAndType(category, type)
        elif (len(args) == 2) and type and name:
            resources_list = dao.getResourceByTypeAndName(type, name)
        elif (len(args) == 1) and category:
            resources_list = dao.getResourceByCategory(category)
        elif (len(args) == 1) and type:
            resources_list = dao.getResourceByType(type)
        elif (len(args) == 1) and name:
            resources_list = dao.getResourceByName(name)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not resources_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in resources_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Resources=result_list)

    def getSellersByResourceId(self, r_id):
        dao = ResourceDAO()
        users_list = dao.getSellerByResourceId(r_id)
        if not users_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in users_list:
                result = self.build_seller_dict(row)
                result_list.append(result)
            return jsonify(Sellers=result_list)

    def getBuyersByResourceId(self, r_id):
        dao = ResourceDAO()
        users_list = dao.getBuyerByResourceId(r_id)
        if not users_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in users_list:
                result = self.build_buyer_dict(row)
                result_list.append(result)
            return jsonify(Buyers=result_list)