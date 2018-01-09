from flask import jsonify
from dao.announcement import AnnouncementDAO


class AnnouncementHandler:
    def build_announcement_dict(self, row):
        result = {}
        result['a_id'] = row[0]
        result['s_id'] = row[1]
        result['r_id'] = row[2]
        result['a_qty'] = row[3]
        result['a_price'] = row[4]
        result['a_totalprice'] = row[5]
        result['a_available'] = row[6]
        result['a_date'] = row[7]
        return result


    def build_resource_announced_dict(self, row):
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
        result['a_priceperunit'] = row[5]
        result['a_totalprice'] = row[6]
        result['a_available'] = row[7]
        result['a_date'] = row[8]
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

    def getAllAnnouncements(self):
        dao = AnnouncementDAO()
        announcement_list = dao.getAllAnnouncements()
        if not announcement_list:
            return jsonify(Error="Announcement Not Found"), 404
        else:
            result_list = []
            for row in announcement_list:
                result = self.build_announcement_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def getAnnouncementById(self, a_id):
        dao = AnnouncementDAO()
        announcement_list = dao.getAnnouncementById(a_id)
        if not announcement_list:
            return jsonify(Error="Announcement Not Found"), 404
        else:
            result = self.build_announcement_dict(announcement_list)
        return jsonify(Announcement=result)

    def getResourcesByAnnouncementId(self, a_id):
        dao = AnnouncementDAO()
        announcement_list = dao.getResourcesByAnnouncementId(a_id)
        if not announcement_list:
            return jsonify(Error="Announcement Not Found"), 404
        else:
            result = self.build_resource_dict(announcement_list)
        return jsonify(Resource=result)

    def getSellerByAnnouncementId(self, a_id):
        dao = AnnouncementDAO()
        announcement_list = dao.getSellerByAnnouncementId(a_id)
        if not announcement_list:
            return jsonify(Error="Announcement Not Found"), 404
        else:
            result = self.build_seller_dict(announcement_list)
        return jsonify(Seller=result)

    def searchAnnouncement(self, args):
        s_id = args.get("seller")
        r_id = args.get("resource")
        a_date = args.get("date")
        dao = AnnouncementDAO()
        announcement_list = []
        if (len(args) == 3) and s_id and r_id and a_date:
            announcement_list = dao.getAnnouncementBySellerResourceandDate(a_date, s_id,r_id)
        elif (len(args) == 2) and s_id and r_id:
            announcement_list = dao.getAnnouncementBySellerandResource(s_id, r_id)
        elif (len(args) == 2) and s_id and a_date:
            announcement_list = dao.getAnnouncementBySellerandDate(s_id, a_date)
        elif (len(args) == 2) and r_id and a_date:
            announcement_list = dao.getAnnouncementByResourceandDate(r_id, a_date)
        elif (len(args) == 1) and s_id:
            announcement_list = dao.getAnnouncementBySeller(s_id)
        elif (len(args) == 1) and r_id:
            announcement_list = dao.getAnnouncementByResource(r_id)
        elif (len(args) == 1) and a_date:
            announcement_list = dao.getAnnouncementByDate(a_date)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not announcement_list:
            return jsonify(Error="Announcement Not Found"), 404
        else:
            result_list = []
            for row in announcement_list:
                result = self.build_announcement_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def getAvailableAnnouncements(self):
        dao = AnnouncementDAO()
        announcement_list = dao.getAvailableAnnouncements()
        if not announcement_list:
            return jsonify(Error="Announcement Not Found"), 404
        else:
            result_list = []
            for row in announcement_list:
                result = self.build_announcement_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def getAllAvailableResources(self):
        dao = AnnouncementDAO()
        announcement_list = dao.getAllAvailableResources()
        if not announcement_list:
            return jsonify(Error="Resources Not Found"), 404
        else:
            result_list = []
            for row in announcement_list:
                result = self.build_resource_announced_dict(row)
                result_list.append(result)
            return jsonify(Announcements=result_list)

    def searchAvailableResources(self, args):
        region= args.get("region")
        city = args.get("city")
        dao = AnnouncementDAO()
        announcement_list = []
        if (len(args) == 1) and city:
            announcement_list = dao.getAvailableResourcesByCity(city)
        elif (len(args) == 1) and region:
            announcement_list = dao.getAvailableResourcesByRegion(region)
        else:
            return jsonify(Error = "Malformed query string"), 400
        if not announcement_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in announcement_list:
                result = self.build_resource_announced_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)


