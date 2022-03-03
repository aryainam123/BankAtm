class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
    def cashWithdrawl(self):
        print("Cash Withdrawd")
    def balanceEnquiry(self):
        print("Balance Enquiry")

atm = Atm(12345,54321)
atm.cashWithdrawl()
atm.balanceEnquiry()
        