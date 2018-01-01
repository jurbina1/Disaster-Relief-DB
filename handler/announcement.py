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
        result['a_totalresources'] = row[7]
        result['a_date'] = row[8]

        return result

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
        s_id = args.get("s_id")
        r_id = args.get("r_id")
        a_date = args.get("a_date")
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
