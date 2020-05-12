# Assignment IV - Retail Domain
#
# Business challenge/requirement
#   BigMart is one of the biggest retailer of Europe and has operations across multiple countries. 
#   You are a data analyst in IT team of BigMart. 
#   Invoice and SKU wise Sales Data for Year 2011 is shared with you. 
#   You need to prepare meaningful charts to showcase the various sales trends for 2011 to top management. 
#
# Approach to Solve
#   You have to use fundamentals of Matplotlib covered in module 5 and plot following 4 chart/graph
#   1. Plot Total Sales Per Month for Year 2011.  
#      How the total sales have increased over months in Year 2011. 
#      Which month has lowest Sales?
#   2. Plot Total Sales Per Month for Year 2011 as Bar Chart.
#      Is Bar Chart Better to visualize than Simple Plot?
#   3. Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
#   4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.  
#      In which range most of the invoice amounts are concentrated?
#
# Enhancements for code
# You can try these enhancements in code
#   1. Change the bar chart to show the value of bar 
#   2. In Pie Chart Play With Parameters shadow=True, startangle=90 and see how different the chart looks 
#   3. In scatter plot change the color of Scatter Points

import pandas as pd
import matplotlib.pyplot as plt
plt.show()
sales_data = pd.read_csv('BigMartSalesData.csv')

# 1
print (" Getting Sales Data for Year 2011")
sales2011 = sales_data[sales_data['Year'] == 2011]
print (" getting Amount for Each Month")
monthlySales2011 = sales2011.groupby('Month').sum()['Amount']
print(monthlySales2011)
plt.plot(monthlySales2011.index,monthlySales2011.values)
plt.xlabel("Sales in Euro")
plt.ylabel("Month Number")
plt.title("Sales Per Month in Year 2011")
plt.savefig("monthly-sales-report-2011.png")
plt.show()

# 2
plt.bar(monthlySales2011.index,monthlySales2011.values,color="red") # Change the color and play
plt.xlabel("Sales in Euro")
plt.ylabel("Month Number")
plt.title("Sales Per Month in Year 2011")
plt.show()

# 3
sales_country_wise = sales2011.groupby('Country').sum()['Amount']
plt.title("Country Wise Contribution For 2011")
plt.pie(sales_country_wise.values,labels=sales_country_wise.index,autopct='%1.1f%%')
plt.show()

# 4
invoiceReport = sales2011.groupby('InvoiceNo').sum()['Amount']
print(invoiceReport)
plt.scatter(invoiceReport.values,invoiceReport.values)
plt.grid(True)
plt.show()