# Business challenge/requirement
# GoodsKart — largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal. 
# FairDeal has its own IT system to maintain records of customer, sales etc.
# For ease of maintenance and cost savings GoodsKart is integrating customer databases of both the organizations hence 
# customer data of FairDeal has to be converted in GoodsKart Customer Format.
#
# Key issues
# GoodsKart customer data has more fields than in FairDeal customer data. 
# Hence FairDeal data needs to be split and stored in GoodsKart Customer Object Oriented Data Structure
#
# Considerations
# System should convert the data at run time
# Data volume- NA
#
# Additional information- NA
# Business benefits
# GoodsKart can eventually sunset IT systems of FairDeal and reduce IT cost by 20-30% 
# 
# Approach to Solve
# You have to use fundamentals of Python taught in module 3.  
# 1. Read FairDealCustomerData.csv
# 2. Name field contains full name 
#   –use regular expression to separate title, first name, last name
# 3. Store the data in Customer Class
# 4. Create Custom Exception – CustomerNotAllowedException
# 5. Pass a customer to function "createOrder" and throw 
# CustomerNotAllowedException in case of blacklisted value is 1
#
# Enhancements for code
# You can try these enhancements in code
# 1.Change function createOrder to take productname and product code as input
# 2.Create Class Order. Return object of type Order in case customer is eligible


import re
import csv

# Exception for blacklisted customer
class CustomerNotAllowed(Exception):
    pass

# Customer data processing class
class CustomerData:
    def __init__(self, csvFileName):
        self.csvFileName = csvFileName
        self.blockedCustomers = set()
        self.allowedCustomers = set()

    def update(self):
        csvFile = open(self.csvFileName,'r')
        with open('FairDealCustomerData.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if(len(row) < 3):
                    continue
                lastName = row[0].strip()
                match = re.search(' ([A-Za-z]+)\.', row[1])
                title = ""
                firstName = ""
                if( match is not None):
                    title = match.group(0).strip()
                firstName = row[1].replace(title, '').strip()
                fullName = (firstName.upper() + " " + lastName.upper())
                if(row[2].strip() == "1"):
                    self.blockedCustomers.add(fullName)
                    print(fullName, " added to black list")
                else:
                    self.allowedCustomers.add(fullName)
                    print(fullName, " is allowed to place orders")

    def checkEligibility(self, fullName):
        if(fullName.upper() in self.blockedCustomers):
            print(fullName + " is not allowed to buy")
            raise CustomerNotAllowed()
        if (fullName.upper() in self.allowedCustomers):
            print(fullName + " can buy")
        else:
            print(fullName + " is not a registered customer")
            raise CustomerNotAllowed()

customerData = CustomerData('FairDealCustomerData.csv')
customerData.update()
while True:
    customerName = input("Enter the name of the customer for placing the order: ")
    if not customerName:
        break
    try:
        customerData.checkEligibility(customerName)
    except CustomerNotAllowed:
        pass
