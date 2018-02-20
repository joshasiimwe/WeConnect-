
class Users(object):

    def __init__(self,username, userid):
        self.username = username
        self.userid = userid

class Businesses(object):

    def __init__(self,businessname, businessid, business_categoryid, business_category):
        self.businessname = businessname
        self.businessid = businessid
        self.business_categoryid = business_categoryid
        self.business_category = business_category

class Reviews(object):

    def __init__(self,review, reviewid):
        self.review = review
        self.reviewid = reviewid
