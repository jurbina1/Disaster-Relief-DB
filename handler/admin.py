from flask import jsonify
from dao.admin import AdminDAO

class AdminHandler:
    def build_admin_dict(self, row):
        result = {}
        result['admin_id'] = row[0]
        result['u_name'] = row[1]
        result['u_lastname'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_region'] = row[5]
        result['u_phone'] = row[6]
        result['u_age'] = row[7]
        return result

    def getAllAdmins(self):
        dao = AdminDAO()
        admin_list = dao.getAllAdmins()
        if not admin_list:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            result_list = []
            for row in admin_list:
                result = []#self.build_buyer_dict(row)
                result_list.append(result)
            return jsonify(Administrators=admin_list)

    def getAdminById(self, admin_id):
        dao = AdminDAO()
        admin_list = dao.getAdminById(admin_id)
        if not admin_list:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            result_list = []
            for row in admin_list:
                result = []#self.build_buyer_dict(row)
                result_list.append(result)
        return jsonify(Administrator=admin_list)