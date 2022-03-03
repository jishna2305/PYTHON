class bank():
    def __init__(self,acnt,name,typ,amt):
        self.ac=acnt
        self.nam=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("Account name = ",self.nam)
        print("Account number = ",self.ac)
        print("Account type = ",self.type)
        print("Balance = ",self.amount)
    def withl(self,wl):
        return(self.amount-wl)
n=input("Enter name : ")
t=input("Enter type : ")
a=int(input("Enter number : "))
am=int(input("Enter amount : "))
obj=bank(a,n,t,am)
print("\nAccount details\n\n")
obj.printamt()
w=int(input("Enter amount to withdraw : "))
print("Balance = ",obj.withl(w))
