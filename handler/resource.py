from flask import jsonify
from dao.resource import ResourceDAO


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['r_description'] = row[3]
        return result

    def build_user_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_name'] = row[1]
        result['u_lastname'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_region'] = row[5]
        result['u_phone'] = row[6]
        result['u_age'] = row[7]
        return result

    def getAllResources(self):
        dao = ResourceDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(records=result_list)

    def getResourceById(self, r_id):
        dao = ResourceDAO()
        row = dao.getResourceById(r_id)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
        return jsonify(Resource=resource)

    def searchResources(self, args):
        category = args.get("category")
        name = args.get("name")
        dao = ResourceDAO()
        resources_list = []
        if category and name:
            resources_list = dao.getResourceByCategoryAndName(category, name)
        elif category:
            resources_list = dao.getResourceByCategory(category)
        elif name:
            resources_list = dao.getResourceByName(name)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getUserSuppliersByResourceId(self, r_id):
        dao = ResourceDAO()
        users_list = dao.getUserSuppliersByResourceId(r_id)
        if not users_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in users_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)

    def getUserConsumersByResourceId(self, r_id):
        dao = ResourceDAO()
        users_list = dao.getUserConsumersByResourceId(r_id)
        if not users_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in users_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)