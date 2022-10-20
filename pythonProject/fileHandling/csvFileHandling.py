import csv
import os
path = r"D:\files\csv_files"
os.chdir(path)
# comma seperated values (csv)

# reading data from csv file
with open("sample.csv") as file:
    reader_obj = csv.reader(file)
    for data in reader_obj:
        print(data)
print()
with open("sample.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(data)

# writing data into csv file
with open("sample1.csv", "w") as file:
    writer_obj = csv.writer(file)
    writer_obj.writerow(["empName", "empID", "salary"])
    writer_obj.writerow(["Supriya", "685148", "4LPA"])

# writerrows()
    writer_obj.writerows([["Abhi", "684149", "5LPA"],["Sumukha", "685150", "6LPA"],["Banu", "685151", "7LPA"]])

# creating headers
with open("sample2.csv", "w") as file:
    writer_obj = csv.DictWriter(file, ["Serial No", "Module name", "Test Case Type"])
    writer_obj.writeheader()
    writer_obj.writerows([{"Serial No": "1", "Module name": "Trains", "Test Case Type": "Fuctionality Test Case"},
                          {"Serial No": "2", "Module name": "Bus", "Test Case Type": "Integration Test Case"},
                          {"Serial No": "3", "Module name": "Cruise", "Test Case Type": "System Test Case"}])

# to remove empty line after every row in excel use "newline" = ""
with open("sample3.csv", "w", newline="") as file:
    writer_obj = csv.DictWriter(file, ["Serial No", "Module name", "Test Case Type"])
    writer_obj.writeheader()
    writer_obj.writerows([{"Serial No": "1", "Module name": "Trains", "Test Case Type": "Fuctionality Test Case"},
                          {"Serial No": "2", "Module name": "Bus", "Test Case Type": "Integration Test Case"},
                          {"Serial No": "3", "Module name": "Cruise", "Test Case Type": "System Test Case"}])

# to skip if any spaces in value
with open("sample4.csv", "w", newline="") as file:
    writer_obj = csv.DictWriter(file, ["Serial No", "Module name", "Test Case Type"])
    writer_obj.writeheader()
    writer_obj.writerows([{"Serial No": "1", "Module name": "Trains", "Test Case Type": "Fuctionality Test Case"},
                          {"Serial No": "2", "Module name": "Bus", "Test Case Type": "Integration Test Case"},
                          {"Serial No": "3", "Module name": "Cruise", "Test Case Type": "System Test Case"}])