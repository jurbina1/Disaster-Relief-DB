from flask import jsonify
from dao.resource import ResourceDAO


class ResourceHandler:

    def build_stat_dict(self,row):
        result=[]
        if (row[0] == 1):
            result.append("Water")
        elif (row[0] == 2):
            result.append("Fuel")
        elif (row[0] == 3):
            result.append("Baby Food")
        elif (row[0] == 4):
            result.append("Medications")
        elif (row[0] == 5):
            result.append("Canned Food")
        elif (row[0] == 6):
            result.append("Dry Food")
        elif (row[0] == 7):
            result.append("Ice")
        elif (row[0] == 8):
            result.append("Medical Devices")
        elif (row[0] == 9):
            result.append("Heavy Equipment")
        elif (row[0] == 10):
            result.append("Tools")
        elif (row[0] == 11):
            result.append("Clothing")
        elif (row[0] == 12):
            result.append("Batteries")
        else:
            result.append("Power Generators")
        result.append(int(row[1]))
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
        return result

    def build_resource_attributes(self, r_id, r_name, r_category, r_type):
        result = {}
        result['r_id'] = r_id
        result['r_name'] = r_name
        if (r_category == '1'):
            result['r_category'] = "Water"
            if (r_type == '1'):
                result['r_type'] = "Bottled Water"
            elif (r_type == '2'):
                result['r_type'] = "1 Gallon Water"
        elif (r_category == '2'):
            result['r_category'] = "Fuel"
            if (r_type == '1'):
                result['r_type'] = "Diesel"
            elif (r_type == '2'):
                result['r_type'] = "Gasoline"
            else:
                result['r_type'] = "Propane"
        elif (r_category == '3'):
            result['r_category'] = "Baby Food"
            result['r_type'] = "Baby Food"
        elif (r_category == '4'):
            result['r_category'] = "Medications"
            result['r_type'] = "Medications"
        elif (r_category == '5'):
            result['r_category'] = "Canned Food"
            result['r_type'] = "Canned Food"
        elif (r_category == '6'):
            result['r_category'] = "Dry Food"
            result['r_type'] = "Dry Food"
        elif (r_category == '7'):
            result['r_category'] = "Ice"
            result['r_type'] = "Ice"
        elif (r_category == '8'):
            result['r_category'] = "Medical Devices"
            result['r_type'] = "Medical Devices"
        elif (r_category == '9'):
            result['r_category'] = "Heavy Equipment"
            result['r_type'] = "Heavy Equipment"
        elif (r_category == '10'):
            result['r_category'] = "Tools"
            result['r_type'] = "Tools"
        elif (r_category == '11'):
            result['r_category'] = "Clothing"
            result['r_type'] = "Clothing"
        elif (r_category == '12'):
            result['r_category'] = "Batteries"
            result['r_type'] = "Batteries"
        else:
            result['r_category'] = "Power Generators"
            if (r_type == '1'):
                result['r_type'] = "Diesel Power Generator"
            elif (r_type == '2'):
                result['r_type'] = "Gasoline Power Generator"
            else:
                result['r_type'] = "Propane Power Generator"
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

    def insertResource(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post Resource"), 400
        else:
            r_name = form['r_name']
            r_category = form['r_category']
            r_type = form['r_type']
            if r_name and r_category and r_type:
                dao = ResourceDAO()
                r_id = dao.insert(r_name, r_category, r_type)
                result = self.build_resource_attributes(r_id, r_name, r_category, r_type)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post Resource"), 400

    def deleteResource(self, r_id):
        dao = ResourceDAO()
        if not dao.getResourceById(r_id):
            return jsonify(Error = "Resource not found."), 404
        else:
            dao.delete(r_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateResource(self, r_id, form):
        dao = ResourceDAO()
        if not dao.getResourceById(r_id):
            return jsonify(Error = "Resource not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update Resource"), 400
            else:
                r_name = form['r_name']
                r_category = form['r_category']
                r_type = form['r_type']
                if r_name and r_category and r_type:
                    dao = ResourceDAO()
                    dao.update(r_id, r_name, r_category, r_type)
                    result = self.build_resource_attributes(r_id, r_name, r_category, r_type)
                    return jsonify(Resource=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in update Resource"), 400

    def getStatistic(self):
        dao= ResourceDAO()
        result_list = []

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getDNStats()
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getDAStats()
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getDMStats()
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getWNStats()
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getWAStats()
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getWMStats()
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("Ponce")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("Ponce")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("Ponce")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("Arecibo")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("Arecibo")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("Arecibo")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("Mayaguez")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("Mayaguez")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("Mayaguez")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("Caguas")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("Caguas")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("Caguas")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("Bayamon")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("Bayamon")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("Bayamon")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("San Juan")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("San Juan")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("San Juan")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Needed'])
        resources_list = dao.getRNStats("Humacao")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Available'])
        resources_list = dao.getRAStats("Humacao")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)

        result = []
        result.append(['Resources', 'Matching'])
        resources_list = dao.getRMStats("Humacao")
        for row in resources_list:
            temp = self.build_stat_dict(row)
            result.append(temp)
        result_list.append(result)


        return result_list