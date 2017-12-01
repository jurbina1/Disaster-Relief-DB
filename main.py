from flask import Flask, jsonify, request
from handler.resource import ResourceHandler

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
def getResourceById(sid):
    return ResourceHandler().getResourceById(sid)

@app.route('/DisasterApp/resources/<int:r_id>/supplies')
def getSellersByResourceId(r_id):
    return ResourceHandler().getSellersByResourceId(r_id)

@app.route('/DisasterApp/resources/<int:r_id>/buyers')
def getBuyersByResourcesId(r_id):
    return ResourceHandler().getBuyersByResourceId(r_id)

if __name__=='__main__':
    app.run()

