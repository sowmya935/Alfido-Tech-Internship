import os
import shutil
import csv

# Task 1 - File Handling and Automation
# Name: Komireddy Sowmya
# Candidate ID: BS/REG/120177
# Domain: MERN Stack Developer Intern

# creating a simple expense tracker text file
f = open("expenses.txt", "w")
f.write("Monthly Expense Tracker\n")
f.write("=======================\n")
f.write("Food: 2000\n")
f.write("Transport: 500\n")
f.write("Books: 300\n")
f.write("Other: 200\n")
f.close()
print("expenses file created")

# reading the expense file
f = open("expenses.txt", "r")
lines = f.readlines()
print("\nExpense File Contents:")
for line in lines:
    print(line.strip())
f.close()

# writing employee details to csv
f = open("employees.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["EmpID", "Name", "Department", "Salary"])
writer.writerow(["101", "Ramesh", "Python Dev", "25000"])
writer.writerow(["102", "Priya", "Data Analyst", "28000"])
writer.writerow(["103", "Kiran", "Backend Dev", "30000"])
f.close()
print("\nemployee csv file created")

# reading and displaying csv
print("\nEmployee Records:")
f = open("employees.csv", "r")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()

# searching a specific record
print("\nSearching for EmpID 102...")
f = open("employees.csv", "r")
reader = csv.reader(f)
for row in reader:
    if row[0] == "102":
        print("found:", row)
f.close()

# file automation with error handling
try:
    # create archive folder
    if not os.path.exists("archive"):
        os.makedirs("archive")
        print("\narchive folder created")

    # rename expense file
    os.rename("expenses.txt", "expenses_may2026.txt")
    print("file renamed to expenses_may2026.txt")

    # move to archive
    shutil.move("expenses_may2026.txt", "archive/expenses_may2026.txt")
    print("file moved to archive folder")

    # copy csv to archive
    shutil.copy("employees.csv", "archive/employees_backup.csv")
    print("csv backup created in archive")

    # delete original csv
    os.remove("employees.csv")
    print("original csv removed")

except FileNotFoundError:
    print("file not found")

except PermissionError:
    print("permission denied")

except Exception as e:
    print("error occurred:", e)

# listing archive contents
print("\nfiles in archive folder:")
for file in os.listdir("archive"):
    print(" -", file)

print("\ntask 1 completed!")