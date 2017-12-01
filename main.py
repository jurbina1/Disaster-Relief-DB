from flask import Flask, jsonify, request
from handler.resource import ResourceHandler
from handler.buyer import BuyerHandler
from handler.seller import SellerHandler

app = Flask(__name__)

@app.route('/')
def home():
    return 'Disaster Relief'

@app.route('/DisasterApp/resources')
def getAllResources():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResource(request.args)

@app.route('/DisasterApp/resources/<int:r_id>')
def getResourcesById(sid):
    return ResourceHandler().getResourceById(sid)

@app.route('/DisasterApp/resources/<int:r_id>/sellers')
def getSellersByResourceId(r_id):
    return ResourceHandler().getSellersByResourceId(r_id)

@app.route('/DisasterApp/resources/<int:r_id>/buyers')
def getBuyersByResourceId(r_id):
    return ResourceHandler().getBuyersByResourceId(r_id)


@app.route('/DisasterApp/buyers')
def getAllBuyers():
    if not request.args:
        return BuyerHandler().getAllBuyers()
    else:
        return BuyerHandler().searchBuyers(request.args)

@app.route('/DisasterApp/buyers/<int:b_id>')
def getBuyerById(b_id):
    return BuyerHandler().getBuyerById(b_id)

@app.route('/DisasterApp/buyers/<int:b_id>/requests')
def getResourcesByBuyerId(b_id):
    return BuyerHandler().getResourcesByBuyerId(b_id)

@app.route('/DisasterApp/sellers')
def getAllSellers():
    if not request.args:
        return SellerHandler().getAllSellers()
    else:
        return SellerHandler().searchSeller(request.args)

@app.route('/Disaster/sellers/<int:s_id>')
def getSellerById(s_id):
    return SellerHandler().getSellerById(s_id)

@app.route('/DisasterApp/sellers/<int:s_id>/announcements')
def getResourcesBySellerId(s_id):
    return SellerHandler().getResourcesBySellerId(s_id)

if __name__=='__main__':
    app.run()

