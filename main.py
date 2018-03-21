from flask import Flask, jsonify, request, render_template
from handler.resource import ResourceHandler
from handler.buyer import BuyerHandler
from handler.seller import SellerHandler
from handler.announcement import AnnouncementHandler
from handler.request import RequestHandler
from handler.bankaccounts import BankAccountHandler
from handler.creditcard import CreditCardHandler
from handler.transaction import TransactionHandler
from handler.admin import AdminHandler

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Disaster Relief App!<br/>' \
           'The possible URLs are: <br/>' \
           '/DisasterApp<br/>' \
           '/DisasterApp/administrators<br/>' \
           '/DisasterApp/resources<br/>' \
           '/DisasterApp/buyers<br/>' \
           '/DisasterApp/sellers<br/>' \
           '/DisasterApp/announcements<br/>' \
           '/DisasterApp/requests<br/>' \
           '/DisasterApp/bankaccounts<br/>' \
           '/DisasterApp/creditcards<br/>' \
           '/DisasterApp/transactions'


@app.route('/DisasterApp')
def dashboard():
    result = ResourceHandler().getStatistic()
    return render_template('dashboard.html', stats=result)



@app.route('/DisasterApp/administrators', methods=['GET', 'POST'])
def getAllAdmins():
    if request.method == 'POST':
        return AdminHandler().insertAdmin(request.form)
    else:
        return AdminHandler().getAllAdmins()


@app.route('/DisasterApp/administrators/<int:admin_id>', methods=['GET', 'PUT', 'DELETE'])
def getAdminById(admin_id):
    if request.method == 'GET':
        return AdminHandler().getAdminById(admin_id)
    elif request.method == 'PUT':
        return AdminHandler().updateAdmin(admin_id, request.form)
    elif request.method == 'DELETE':
        return AdminHandler().deleteAdmin(admin_id)
    else:
        return jsonify(Error="Method not allowed."), 405




@app.route('/DisasterApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResource(request.args)

@app.route('/DisasterApp/resources/<int:r_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(r_id):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(r_id)
    elif request.method == 'PUT':
        return ResourceHandler().updateResource(r_id, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deleteResource(r_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/resources/<int:r_id>/sellers')
def getSellersByResourceId(r_id):
    return ResourceHandler().getSellersByResourceId(r_id)

@app.route('/DisasterApp/resources/<int:r_id>/buyers')
def getBuyersByResourceId(r_id):
    return ResourceHandler().getBuyersByResourceId(r_id)




@app.route('/DisasterApp/buyers', methods=['GET', 'POST'])
def getAllBuyers():
    if request.method == 'POST':
        return BuyerHandler().insertBuyer(request.form)
    else:
        if not request.args:
            return BuyerHandler().getAllBuyers()
        else:
            return BuyerHandler().searchBuyers(request.args)

@app.route('/DisasterApp/buyers/<int:b_id>', methods=['GET', 'PUT', 'DELETE'])
def getBuyerById(b_id):
    if request.method == 'GET':
        return BuyerHandler().getBuyerById(b_id)
    elif request.method == 'PUT':
        return BuyerHandler().updateBuyer(b_id, request.form)
    elif request.method == 'DELETE':
        return BuyerHandler().deleteBuyer(b_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/buyers/<int:b_id>/requests')
def getResourcesByBuyerId(b_id):
    return BuyerHandler().getResourcesByBuyerId(b_id)

@app.route('/DisasterApp/buyers/<int:b_id>/transactions')
def getTransactionsByBuyerId(b_id):
    return BuyerHandler().getTransactionsByBuyerId(b_id)




@app.route('/DisasterApp/sellers', methods=['GET', 'POST'])
def getAllSellers():
    if request.method == 'POST':
        return SellerHandler().insertSeller(request.form)
    else:
        if not request.args:
            return SellerHandler().getAllSellers()
        else:
            return SellerHandler().searchSeller(request.args)

@app.route('/DisasterApp/sellers/<int:s_id>', methods=['GET', 'PUT', 'DELETE'])
def getSellerById(s_id):
    if request.method == 'GET':
        return SellerHandler().getSellerById(s_id)
    elif request.method == 'PUT':
        return SellerHandler().updateSeller(s_id, request.form)
    elif request.method == 'DELETE':
        return SellerHandler().deleteSeller(s_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/sellers/<int:s_id>/announcements')
def getResourcesBySellerId(s_id):
    return SellerHandler().getResourcesBySellerId(s_id)

@app.route('/DisasterApp/sellers/<int:s_id>/transactions')
def getTransactionsBySellerId(s_id):
    return SellerHandler().getTransactionsBySellerId(s_id)




@app.route('/DisasterApp/announcements', methods=['GET', 'POST'])
def getAllAnnouncements():
    if request.method == 'POST':
        return AnnouncementHandler().insertAnnouncement(request.form)
    else:
        if not request.args:
            return AnnouncementHandler().getAllAnnouncements()
        else:
            return AnnouncementHandler().searchAnnouncement(request.args)

@app.route('/DisasterApp/announcements/<int:a_id>', methods=['GET', 'PUT', 'DELETE'])
def getAnnouncementById(a_id):
    if request.method == 'GET':
        return AnnouncementHandler().getAnnouncementById(a_id)
    elif request.method == 'PUT':
        return AnnouncementHandler().updateAnnouncement(a_id, request.form)
    elif request.method == 'DELETE':
        return AnnouncementHandler().deleteAnnouncement(a_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/announcements/<int:a_id>/resource')
def getResourcesByAnnouncementId(a_id):
    return AnnouncementHandler().getResourcesByAnnouncementId(a_id)

@app.route('/DisasterApp/announcements/<int:a_id>/seller')
def getSellerByAnnouncementId(a_id):
    return AnnouncementHandler().getSellerByAnnouncementId(a_id)

@app.route('/DisasterApp/announcements/active')
def getAvailableAnnouncements():
    return AnnouncementHandler().getAvailableAnnouncements()

@app.route('/DisasterApp/announcements/resources')
def getAllAvailableResources():
    if request.args:
        return AnnouncementHandler().searchAvailableResources(request.args)
    else:
        return AnnouncementHandler().getAllAvailableResources()




@app.route('/DisasterApp/requests', methods=['GET', 'POST'])
def getAllRequests():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.form)
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequest(request.args)

@app.route('/DisasterApp/requests/<int:rq_id>', methods=['GET', 'PUT', 'DELETE'])
def getRequestById(rq_id):
    if request.method == 'GET':
        return RequestHandler().getRequestById(rq_id)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(rq_id, request.form)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequest(rq_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/requests/<int:rq_id>/resource')
def getResourcesByRequestId(rq_id):
    return RequestHandler().getResourcesByRequestId(rq_id)

@app.route('/DisasterApp/requests/<int:rq_id>/buyer')
def getBuyerByRequestId(rq_id):
    return RequestHandler().getBuyerByRequestId(rq_id)

@app.route('/DisasterApp/requests/active')
def getAvailableRequests():
    return RequestHandler().getAvailableRequests()





@app.route('/DisasterApp/bankaccounts', methods=['GET', 'POST'])
def getAllBankAccounts():
    if request.method == 'POST':
        return BankAccountHandler().insertBankAccount(request.form)
    else:
        if not request.args:
            return BankAccountHandler().getAllBankAccounts()
        else:
            return BankAccountHandler().searchBankAccounts(request.args)

@app.route('/DisasterApp/bankaccounts/<int:ba_id>', methods=['GET', 'PUT', 'DELETE'])
def getBankAccountById(ba_id):
    if request.method == 'GET':
        return BankAccountHandler().getBankAccountById(ba_id)
    elif request.method == 'PUT':
        return BankAccountHandler().updateBankAccount(ba_id, request.form)
    elif request.method == 'DELETE':
        return BankAccountHandler().deleteBankAccount(ba_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/bankaccounts/<int:ba_id>/seller')
def getSellerByBankAccountId(ba_id):
    return BankAccountHandler().getSellerByBankAccountId(ba_id)




@app.route('/DisasterApp/creditcards', methods=['GET', 'POST'])
def getAllCreditCards():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(request.form)
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCards()
        else:
            return CreditCardHandler().searchCreditCards(request.args)

@app.route('/DisasterApp/creditcards/<int:c_id>', methods=['GET', 'PUT', 'DELETE'])
def getCreditCardById(c_id):
    if request.method == 'GET':
        return CreditCardHandler().getCreditCardById(c_id)
    elif request.method == 'PUT':
        return CreditCardHandler().updateCreditCard(c_id, request.form)
    elif request.method == 'DELETE':
        return CreditCardHandler().deleteCreditCard(c_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/creditcards/<int:c_id>/buyer')
def getBuyerByCreditCardId(c_id):
    return CreditCardHandler().getBuyerByCreditCardId(c_id)




@app.route('/DisasterApp/transactions', methods=['GET', 'POST'])
def getAllTransactions():
    if request.method == 'POST':
        return TransactionHandler().insertTransaction(request.form)
    else:
        if not request.args:
            return TransactionHandler().getAllTransactions()
        else:
            return TransactionHandler().searchTransactions(request.args)

@app.route('/DisasterApp/transactions/<int:t_id>', methods=['GET', 'PUT', 'DELETE'])
def getTransactionById(t_id):
    if request.method == 'GET':
        return TransactionHandler().getTransactionById(t_id)
    elif request.method == 'PUT':
        return TransactionHandler().updateTransaction(t_id, request.form)
    elif request.method == 'DELETE':
        return TransactionHandler().deleteTransaction(t_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DisasterApp/transactions/<int:t_id>/resource')
def getResourcesByTransactionId(t_id):
    return TransactionHandler().getResourcesByTransactionId(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/buyer')
def getBuyerByTransactionId(t_id):
    return TransactionHandler().getBuyerByTransactionId(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/seller')
def getSellerByTransactionId(t_id):
    return TransactionHandler().getSellerByTransactionId(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/creditcard')
def getCreditCardByTransactionId(t_id):
    return TransactionHandler().getCreditCardByTransactionId(t_id)

@app.route('/DisasterApp/transactions/<int:t_id>/bankaccount')
def getBankAccountByTransactionId(t_id):
    return TransactionHandler().getBankAccountByTransactionId(t_id)

@app.route('/DisasterApp/transactions/getTotal')
def getTransactionSum():
    if request.args:
        return TransactionHandler().getTransactionSum(request.args)
    else:
        return TransactionHandler().getTransactionTotalSum()

@app.route('/DisasterApp/transactions/donations')
def getDonations():
    return TransactionHandler().getDonations()

@app.route('/DisasterApp/transactions/reservations')
def getReservations():
    return TransactionHandler().getReservations()

if __name__=='__main__':
    app.run()

