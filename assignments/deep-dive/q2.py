# 2.
# Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Hint: Use if/elif to deal with conditions.

def binarySearch(data, x):
    if (len(data) == 1):
	    if(data[0] == x):
	        return True
	    else:
	        return False
    mid = (len(data)//2)
    return binarySearch(data[:mid], x) or binarySearch(data[mid:], x)

# Read data 
companyData = [s for s in input("Enter data as a list of words:\n").split()]
print("Sorted list is:\n", sorted(companyData))
# Search for an element
while True:
    element = input("Enter the element to find: ")
    if not element:
        break
    if (binarySearch(companyData, element)):
        print ("Success: Element found in company data")
    else:
        print ("Failure: Element does not exist in company data")