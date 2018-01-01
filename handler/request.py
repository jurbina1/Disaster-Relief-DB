from flask import jsonify
from dao.request import RequestDAO


class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['rq_id'] = row[0]
        result['b_id'] = row[1]
        result['r_id'] = row[2]
        result['rq_qty'] = row[3]
        result['rq_date'] = row[5]
        result['rq_fulfillment'] = row[6]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_name'] = row[1]
        result['r_category'] = row[2]
        result['r_type'] = row[3]
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
        b_id = args.get("b_id")
        r_id = args.get("r_id")
        rq_date = args.get("rq_date")
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
