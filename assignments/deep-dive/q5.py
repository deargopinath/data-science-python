# 5.
# Design a software for bank system. There should be options like cash withdraw	 cash credit and change password. 
# According to user input	 the software should provide required output.
# Hint: Use if else statements and functions.~

import getpass

class OnlineBank:
    def __init__(self):
        self.balance = 0.0

    def showMenu(self):
        print("\nWelcome to Online Bank.\n______________________\n")
        print ("[1] Account Summary")
        print ("[2] Cash Withdrawal")
        print ("[3] Cash Credit")
        print ("[4] Change password")
        print ("[5] Logout\n")      
        
    def accountSummary(self):
        print ("\nAvailable balance: £ ", self.balance)

    def cashWithdrawal(self):
        amount = float(input("Please enter the amount to withdraw: "))
        if (amount < 0):
            print("Invalid amount")
            return
        if (amount > self.balance):
            print("Insufficient balance. Please enter a lower amount")
            return
        self.balance -= amount
        print ("Success. An amount of £ ", amount, " was debited from your account.")
        self.accountSummary()

    def cashCredit(self):
        amount = float(input("Please enter the amount to deposit: "))
        if (amount < 0):
            print("Invalid amount")
            return
        self.balance += amount
        print ("Success. An amount of £ ", amount, " was credited to your account.")
        self.accountSummary()

    def changePassword(self):
        oldPassword = getpass.getpass("Please enter the current pasword: ")
        newPassword = getpass.getpass("Please enter the new pasword: ")
        newPasswordAgain = getpass.getpass("Please enter the new pasword again: ")
        if(newPassword != newPasswordAgain):
            print("Passwords do not match.")
            return
        print ("Success. Password was changed sucessfully")

    def run(self):
        while True:
            self.showMenu()
            option = input("Please select an option: ")
            if(option == "1"):
                self.accountSummary()
            elif(option == "2"):
                self.cashWithdrawal()
            elif(option == "3"):
                self.cashCredit()
            elif(option == "4"):
                self.changePassword()
            elif(option == "5"):
                print("Thank you for banking with Online Bank")
                break
            else:
                print("Invalid option")
                             
onlineBank = OnlineBank() 
onlineBank.run()
