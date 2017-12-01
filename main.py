from flask import Flask, jsonify
from handler.resource import ResourceHandler

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
    return ResourceHandler().getUserSuppliersByResourcesId(r_id)

@app.route('/DisasterApp/resources/<int:r_id>/needs')
def getPartsBySuplierId(r_id):
    return ResourceHandler().getUserConsumersByResourcesId(r_id)

if __name__=='__main__':
    app.run()

