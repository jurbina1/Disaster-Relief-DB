from flask import Flask, jsonify, request
from handler.resource import ResourceHandler
from handler.seller import SellerHandler

app = Flask(__name__)

@app.route('/')
def home():
    return 'Disaster Relief'

@app.route('/DisasterApp/resources')
def getAllSuppliers():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResource(request.args)

@app.route('/DisasterApp/resources/<int:r_id>')
def getSupplierById(sid):
    return ResourceHandler().getResourceById(sid)

@app.route('/DisasterApp/resources/<int:r_id>/supplies')
def getPartsBySuplierId(r_id):
    return ResourceHandler().getSellersByResourceId(r_id)

@app.route('/DisasterApp/resources/<int:r_id>/buyers')
def getPartsBySuplierId(r_id):
    return ResourceHandler().getBuyersByResourceId(r_id)

@app.route('/DisasterApp/sellers')
def getAllSuppliers():
    if not request.args:
        return SellerHandler().getAllSellers()
    else:
        return SellerHandler().searchSeller(request.args)

@app.route('/Disaster/sellers/<int:s_id>')
def getSellerById(s_id):
    return SellerHandler().getSupplierById(s_id)

@app.route('/DisasterApp/sellers/<int:s_id>/parts')
def getResourcesBySellerId(s_id):
    return SellerHandler().getResourcesBySellerId(s_id)

if __name__=='__main__':
    app.run()

