import random

class Create:

    def creating(self,accountNumbers,accountNames,accountBalance):
        self.accountNumbers = accountNumbers
        self.accountNames = accountNames
        self.accountBalance = accountBalance
        self.number = random.randint(10000,99999)
        self.accountNumbers.append(self.number)
        print("Enter accountant's name:",end=' ')
        self.name = input()
        self.accountNames.append(self.name)
        print("Enter the first deposit balance:",end=' ')
        self.balance = int(input())
        self.accountBalance.append(self.balance)
        print("Your account number is:",end=' ')
        print(self.number)




class Access(Create):

    def accessing(self,nameVerification,numberVerification,accountNumbers,accountNames,accountBalance):
        flag = 0
        self.nameVerification = nameVerification
        self.numberVerification = numberVerification
        self.accountNumbers = accountNumbers
        self.accountNames = accountNames
        self.accountBalance = accountBalance

        for i in self.accountNumbers:
            if(i==self.numberVerification):
                flag=1
                self.index = self.accountNumbers.index(self.numberVerification)
                print("Verified")
                while True:
                    print("Choose the option:")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Display Money")
                    print("4. Home Page")
                    choose = int(input())
                    if choose is 1:
                        print("Enter the amount that you want to deposit:", end=' ')
                        dep = int(input())
                        self.accountBalance[self.index] = self.accountBalance[self.index] + dep
                    elif choose is 2:
                        print("Enter the amount that you want to withdraw:", end=' ')
                        withdraw = int(input())
                        if withdraw <= self.accountBalance[self.index]:
                            self.accountBalance[self.index] = self.accountBalance[self.index] - withdraw
                        else:
                            print("Insufficient Balance")
                    elif choose is 3:
                        print(self.accountBalance[self.index])
                    elif choose is 4:
                        break

        if flag is 0:
            print("Access Denied")







accountNumbers = []
accountNames = []
accountBalance = []
createAccount = Create()
accessAccount = Access()
while True:
    print("-----HOME PAGE-----")
    print("1. Create your account")
    print("2. Access your account")
    print("3. Exit")
    print("Enter your choice",end=' ')
    choice = int(input())
    if choice is 1:
        createAccount.creating(accountNumbers,accountNames,accountBalance)
        print("Your savings account is created")

    elif choice is 2:
        print("Enter accountant name for verification:",end=' ')
        nameVerification = input()
        print("Enter account number for verification:", end=' ')
        numberVerification = int(input())
        accessAccount.accessing(nameVerification,numberVerification,accountNumbers,accountNames,accountBalance)

    elif choice is 3:
        print("-----THANKYOU-----")
        quit()









