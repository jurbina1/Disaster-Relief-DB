from flask import jsonify
from dao.request import RequestDAO


class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['rq_id'] = row[0]
        result['b_id'] = row[1]
        result['r_id'] = row[2]
        result['rq_qty'] = row[3]
        result['rq_date'] = row[4]
        result['rq_fulfillment'] = row[5]
        return result

    def build_request_attributes(self, rq_id, b_id, r_id, rq_qty, rq_fulfillment):
        result = {}
        result['rq_id'] = rq_id
        result['b_id'] = b_id
        result['r_id'] = r_id
        result['rq_qty'] = rq_qty
        result['rq_fulfillment'] = rq_fulfillment
        return result

    def build_resource_requested_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_name'] = row[1]
        if (row[2] == 1):
            result['r_category'] = "Water"
            if (row[3] == 1):
                result['r_type'] = "Bottled Water"
            elif (row[3] == 2):
                result['r_type'] = "1 Gallon Water"
        elif (row[2] == 2):
            result['r_category'] = "Fuel"
            if (row[3] == 1):
                result['r_type'] = "Diesel"
            elif (row[3] == 2):
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
            if (row[3] == 1):
                result['r_type'] = "Diesel Power Generator"
            elif (row[3] == 2):
                result['r_type'] = "Gasoline Power Generator"
            else:
                result['r_type'] = "Propane Power Generator"
        result['rq_qty'] = row[4]
        result['rq_date'] = row[3]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_name'] = row[1]
        if (row[2] == 1):
            result['r_category'] = "Water"
            if (row[3] == 1):
                result['r_type'] = "Bottled Water"
            elif (row[3] == 2):
                result['r_type'] = "1 Gallon Water"
        elif (row[2] == 2):
            result['r_category'] = "Fuel"
            if (row[3] == 1):
                result['r_type'] = "Diesel"
            elif (row[3] == 2):
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
            if (row[3] == 1):
                result['r_type'] = "Diesel Power Generator"
            elif (row[3] == 2):
                result['r_type'] = "Gasoline Power Generator"
            else:
                result['r_type'] = "Propane Power Generator"
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

    def getAllRequests(self):
        dao = RequestDAO()
        request_list = dao.getAllRequests()
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
            result_list = []
            for row in request_list:
                result = self.build_request_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

    def getRequestById(self, rq_id):
        dao = RequestDAO()
        request_list = dao.getRequestById(rq_id)
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
            result = self.build_request_dict(request_list)
        return jsonify(Request=result)

    def getResourcesByRequestId(self, rq_id):
        dao = RequestDAO()
        request_list = dao.getResourcesByRequestId(rq_id)
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
            result = self.build_resource_dict(request_list)
        return jsonify(Resource=result)

    def getBuyerByRequestId(self, rq_id):
        dao = RequestDAO()
        request_list = dao.getBuyerByRequestId(rq_id)
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
            result = self.build_buyer_dict(request_list)
        return jsonify(Buyer=result)

    def searchRequest(self, args):
        b_id = args.get("buyer")
        r_id = args.get("resource")
        rq_date = args.get("date")
        dao = RequestDAO()
        request_list = []
        if (len(args) == 3) and b_id and r_id and rq_date:
            request_list = dao.getRequestByBuyerResourceandDate(rq_date, b_id, r_id)
        elif (len(args) == 2) and b_id and r_id:
            request_list = dao.getRequestByBuyerandResource(b_id, r_id)
        elif (len(args) == 2) and b_id and rq_date:
            request_list = dao.getRequestByBuyerandDate(b_id, rq_date)
        elif (len(args) == 2) and r_id and rq_date:
            request_list = dao.getRequestByResourceandDate(r_id, rq_date)
        elif (len(args) == 1) and b_id:
            request_list = dao.getRequestByBuyer(b_id)
        elif (len(args) == 1) and r_id:
            request_list = dao.getRequestByResource(r_id)
        elif (len(args) == 1) and rq_date:
            request_list = dao.getRequestByDate(rq_date)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
            result_list = []
            for row in request_list:
                result = self.build_request_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

    def getAvailableRequests(self):
        dao = RequestDAO()
        request_list = dao.getAvailableRequests()
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
            result_list = []
            for row in request_list:
                result = self.build_request_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

    def getAllRequestedResources(self):
        dao = RequestDAO()
        announcement_list = dao.getAllRequestedResources()
        if not announcement_list:
            return jsonify(Error="Resources Not Found"), 404
        else:
            result_list = []
            for row in announcement_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def insertRequest(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            b_id = form['b_id']
            r_id = form['r_id']
            rq_qty = form['rq_qty']
            rq_fulfillment = form['rq_fulfillment']
            if b_id and r_id and rq_qty and rq_fulfillment:
                dao = RequestDAO()
                rq_id = dao.insert(b_id, r_id, rq_qty, rq_fulfillment)
                result = self.build_request_attributes(rq_id, b_id, r_id, rq_qty, rq_fulfillment)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteRequest(self, rq_id):
        dao = RequestDAO()
        if not dao.getRequestById(rq_id):
            return jsonify(Error = "Request not found."), 404
        else:
            dao.delete(rq_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateRequest(self, rq_id, form):
        dao = RequestDAO()
        if not dao.getRequestById(rq_id):
            return jsonify(Error = "Request not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                b_id = form['b_id']
                r_id = form['r_id']
                rq_qty = form['rq_qty']
                rq_fulfillment = form['rq_fulfillment']
                if b_id and r_id and rq_qty and rq_fulfillment:
                    dao = RequestDAO()
                    dao.update(rq_id, b_id, r_id, rq_qty, rq_fulfillment)
                    result = self.build_request_attributes(rq_id, b_id, r_id, rq_qty, rq_fulfillment)
                    return jsonify(Request=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
