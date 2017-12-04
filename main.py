from flask import Flask, jsonify, request
from handler.resource import ResourceHandler
from handler.buyer import BuyerHandler
from handler.seller import SellerHandler
from handler.announcement import AnnouncementHandler
from handler.request import RequestHandler
from handler.bankaccounts import BankAccountHandler
from handler.creditcard import CreditCardHandler
from handler.transaction import TransactionHandler

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Disaster Relief App!'

@app.route('/DisasterApp/resources')
def getAllResources():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResource(request.args)

@app.route('/DisasterApp/resources/<int:r_id>')
def getResourceById(sid):
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

@app.route('/DisasterApp/sellers/<int:s_id>/resources')
def getResourcesBySellerId(s_id):
    return SellerHandler().getResourcesBySellerId(s_id)




@app.route('/DisasterApp/announcements')
def getAllAnnouncements():
    if not request.args:
        return AnnouncementHandler().getAllAnnouncements()
    else:
        return AnnouncementHandler().searchAnnouncement(request.args)

@app.route('/Disaster/announcements/<int:a_id>')
def getAnnouncementById(a_id):
    return AnnouncementHandler().getAnnouncementById(a_id)

@app.route('/DisasterApp/announcements/<int:a_id>/resource')
def getResourcesByAnnouncementId(a_id):
    return AnnouncementHandler().getResourcesByAnnouncementId(a_id)

@app.route('/DisasterApp/announcements/<int:a_id>/seller')
def getResourcesByAnnouncementId(a_id):
    return AnnouncementHandler().getSellerByAnnouncementId(a_id)




@app.route('/DisasterApp/requests')
def getAllRequests():
    if not request.args:
        return RequestHandler().getAllRequests()
    else:
        return RequestHandler().searchRequest(request.args)

@app.route('/Disaster/requests/<int:rq_id>')
def getAnnouncementById(rq_id):
    return RequestHandler().getRequestById(rq_id)

@app.route('/DisasterApp/requests/<int:rq_id>/resource')
def getResourcesByAnnouncementId(rq_id):
    return RequestHandler().getResourcesByRequestId(rq_id)

@app.route('/DisasterApp/requests/<int:rq_id>/buyer')
def getResourcesByAnnouncementId(rq_id):
    return RequestHandler().getBuyerByRequestId(rq_id)




@app.route('/DisasterApp/bankaccounts')
def getAllBankAccounts():
    if not request.args:
        return BankAccountHandler().getAllBankAccounts()
    else:
        return BankAccountHandler().searchBankAccounts(request.args)

@app.route('/Disaster/bankaccounts/<int:ba_id>')
def getBankAccountById(ba_id):
    return BankAccountHandler().getBankAccountById(ba_id)

@app.route('/DisasterApp/bankaccounts/<int:ba_id>/seller')
def getResourcesByAnnouncementId(ba_id):
    return BankAccountHandler().getSellerByBankAccountId(ba_id)




@app.route('/DisasterApp/creditcard')
def getAllCreditCards():
    if not request.args:
        return CreditCardHandler().getAllCreditCards()
    else:
        return CreditCardHandler().searchCreditCards(request.args)

@app.route('/Disaster/creditcard/<int:c_id>')
def getCreditCardById(c_id):
    return CreditCardHandler().getCreditCardById(c_id)

@app.route('/DisasterApp/creditcard/<int:c_id>/buyer')
def getBuyerByCreditCardId(c_id):
    return CreditCardHandler().getBuyerByCreditCardId(c_id)




@app.route('/DisasterApp/transactions')
def getAllTransactions():
    if not request.args:
        return TransactionHandler().getAllTransactions()
    else:
        return TransactionHandler().searchTransactions(request.args)

@app.route('/Disaster/transactions/<int:t_id>')
def getTransactionById(t_id):
    return TransactionHandler().getTransactionById(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/resource')
def getResourcesByTransactionId(t_id):
    return TransactionHandler().getResourcesByTransactionId(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/buyer')
def getBuyerByTransactionId(t_id):
    return TransactionHandler().getBuyerByTransactionId(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/seller')
def getSellerByTransactionId(t_id):
    return TransactionHandler().getSellerByTransactionId(t_id)



if __name__=='__main__':
    app.run()

