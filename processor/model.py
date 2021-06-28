from sklearn.svm import SVR


rbf_svr = SVR(kernel="rbf", C =1000.0, gamma=0.85)

def learn( open_price_list, close_price_list):
    rbf_svr.fit(open_price_list, close_price_list)

def predict(open_price):
    return rbf_svr.predict(open_price)