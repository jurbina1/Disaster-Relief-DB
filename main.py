from flask import Flask, jsonify, request
from handler.resource import ResourceHandler
from handler.buyer import BuyerHandler

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

@app.route('/DisasterApp/resources/<int:r_id>/supplies')
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

@app.route('/DisasterApp/buyers/<int:sid>')
def getBuyerById(sid):
    return BuyerHandler().getBuyerById(sid)

@app.route('/DisasterApp/buyers/<int:sid>/requests')
def getResourcesByBuyerId(sid):
    return BuyerHandler().getResourcesByBuyerId(sid)

if __name__=='__main__':
    app.run()

