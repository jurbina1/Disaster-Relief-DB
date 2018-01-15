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
        result['u_address'] = row[5]
        result['u_city'] = row[6]
        result['u_region'] = row[7]
        result['u_phone'] = row[8]
        result['u_age'] = row[9]
        return result

    def build_admin_attributes(self, admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age):
        result = {}
        result['admin_id'] = admin_id
        result['u_name'] = u_name
        result['u_lastname'] = u_lastname
        result['u_email'] = u_email
        result['u_password'] = u_password
        result['u_address'] = u_address
        result['u_city'] = u_city
        result['u_region'] = u_region
        result['u_phone'] = u_phone
        result['u_age'] = u_age
        return result


    def getAllAdmins(self):
        dao = AdminDAO()
        admin_list = dao.getAllAdmins()
        if not admin_list:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            result_list = []
            for row in admin_list:
                result = self.build_admin_dict(row)
                result_list.append(result)
            return jsonify(Administrators=result_list)

    def getAdminById(self, admin_id):
        dao = AdminDAO()
        admin_list = dao.getAdminById(admin_id)
        if not admin_list:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            result = self.build_admin_dict(admin_list)
        return jsonify(Administrator=result)

    def insertAdmin(self, form):
        if len(form) != 9:
            return jsonify(Error = "Malformed post request"), 400
        else:
            u_name = form['u_name']
            u_lastname = form['u_lastname']
            u_email = form['u_email']
            u_password = form['u_password']
            u_address = form['u_address']
            u_city = form['u_city']
            u_region = form['u_region']
            u_phone = form['u_phone']
            u_age = form['u_age']
            if u_name and u_lastname and u_email and u_password and u_address and u_city and u_region and u_phone and u_age:
                dao = AdminDAO()
                admin_id = dao.insert(u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                result = self.build_admin_attributes(admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                return jsonify(Admin=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteAdmin(self, admin_id):
        dao = AdminDAO()
        if not dao.getAdminById(admin_id):
            return jsonify(Error = "Admin not found."), 404
        else:
            dao.delete(admin_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateAdmin(self, admin_id, form):
        dao = AdminDAO()
        if not dao.getAdminById(admin_id):
            return jsonify(Error = "Admin not found."), 404
        else:
            if len(form) != 9:
                return jsonify(Error="Malformed update request"), 400
            else:
                u_name = form['u_name']
                u_lastname = form['u_lastname']
                u_email = form['u_email']
                u_password = form['u_password']
                u_address = form['u_address']
                u_city = form['u_city']
                u_region = form['u_region']
                u_phone = form['u_phone']
                u_age = form['u_age']
                if u_name and u_lastname and u_email and u_password and u_address and u_city and u_region and u_phone and u_age:
                    dao = AdminDAO()
                    dao.update(admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                    result = self.build_admin_attributes(admin_id, u_name, u_lastname, u_email, u_password, u_address, u_city, u_region, u_phone, u_age)
                    return jsonify(Admin=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
