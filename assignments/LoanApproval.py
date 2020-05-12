import csv

allowedProfessions = set()
with open('bank-data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip heading row
    next(csvreader)
    for row in csvreader:
        if(len(row) < 4):
            continue
        if(row[3].upper() == "YES"):
            allowedProfessions.add(row[1].upper())
print("Eligible professions are:\n", allowedProfessions)

while True:
    inputProfession = input("Enter the profession of the applicant: ")
    if not inputProfession:
        break
    if(inputProfession.upper() in allowedProfessions):
        print("Yes. Applicant is eligible for loan account")
    else:
        print("Not eligible")
