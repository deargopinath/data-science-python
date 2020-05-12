import pandas as pd

pd.set_option('display.float_format', lambda x: '%.3f' % x)
#  Read Salaries.csv as a dataframe called salary
salary = pd.read_csv('Salaries.csv')
print("\n # Total salary cost per year and see how it has increased over years: ")
print (salary.groupby('Year').sum()['TotalPayBenefits'])

print("\n # 1 - Compute how much total salary cost has increased from year 2011 to 2014")
print (salary.groupby('Year').mean()['TotalPayBenefits'])

print("\n # 2 - Which Job Title in Year 2014 has highest mean salary?")
print (salary.groupby(['Year','JobTitle']).mean()['TotalPayBenefits'])

print("\n # 3 - How much money could have been saved in Year 2014 by stopping OverTimePay?")
print (salary.groupby('Year').sum()['OvertimePay'])

print ("\n # 4 -  Which are the top 5 common job in Year 2014 and how much do they cost SFO?")
commonFiveJobs = salary[salary['Year'] == 2014]['JobTitle'].value_counts().head(5)
print (commonFiveJobs)

# Calculate the Cost
totalCost = 0
for index,value in commonFiveJobs.iteritems():
    print(index,value)
    totalCost += sum(salary[ (salary['Year']== 2014) & (salary['JobTitle'] == index)]['TotalPayBenefits'])
print (" Total Cost of Top 5 Jobs in Year 2014 ", totalCost)

print("\n # 5 - Who was the top earning employee across all the years?")
topPaid = salary.groupby('EmployeeName').sum()['TotalPayBenefits']
print((topPaid.sort_values(axis=0)).tail(n=1))
