import os
import csv
path = r"D:\files\csv_files"
os.chdir(path)

 # 1.
with open("employees.csv") as file:
    reader_obj = csv.reader(file)
    header_skip = next(reader_obj)
    for data in reader_obj:
        print(data[0])
# 2.
with open("employees.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
       # print(data)
       if int(data["pay"]) > 70000:
           print(data["pay"])

# or
with open("employees.csv") as file:
    reader_obj = csv.reader(file)
    header_skip = next(reader_obj)
    for data in reader_obj:
        if int(data[-1]) > 70000:
            print(data[-1])

# 3.
d = {}
with open("employees.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["gender"] not in d:
            d[data["gender"]] = [data["name"]]
        else:
            # d[data["gender"]] += [data["name"]]
            d[data["gender"]].append(data["name"])
print(d)
# 4.
d = {}
with open("employees.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["team"] not in d:
            d[data["team"]] = [data["name"]]
        else:
            d[data["team"]] += [data["name"]]
            # d[data["team"]].append(data["name"])
print(d)
# 5.
with open("test.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(sorted(reader_obj, key = lambda data: float(data["price"])))
# 6.
import os
import csv
path = r"D:\files\csv_files"
os.chdir(path)
sum = 0
with open("test.csv") as file:
    reader_obj = csv.reader(file)
    header_skip = next(reader_obj)
    for data in reader_obj:
        if data != []:
            sum = sum + int(data[1])


print(sum)

# 7.a.
import os
import csv
path = r"D:\files\csv_files"
os.chdir(path)
sum = 0
with open("vaccination_data.csv") as file:
    reader_obj = csv.reader(file)
    header_skip = next(reader_obj)
    for data in reader_obj:
        if data[5] != "":
            sum = sum + int(data[5])
print(sum)

# 7.b.
import os
import csv
path = r"D:\files\csv_files"
os.chdir(path)
d = {}
with open("vaccination_data.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["COUNTRY"] not in d:
            d[data["COUNTRY"]] = data["TOTAL_VACCINATIONS"]
        else:
            d[data["COUNTRY"]] += data["TOTAL_VACCINATIONS"]

print(d)

# 7.c.
import csv
import os
path = r"D:\files\csv_files"
os.chdir(path)
d = {}
with open("vaccination_data.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["COUNTRY"] not in d:
            d[data["COUNTRY"]] = data["WHO_REGION"]
        else:
            d[data["COUNTRY"]] += data["WHO_REGION"]

print(d)

# 7.d.
import csv
import os
from collections import Counter
path = r"D:\files\csv_files"
os.chdir(path)
d = {}
with open("vaccination_data.csv") as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        if data["COUNTRY"] not in d:
            d[data["COUNTRY"]] = data["PERSONS_VACCINATED_1PLUS_DOSE"]
        else:
            d[data["COUNTRY"]] += data["PERSONS_VACCINATED_1PLUS_DOSE"]

# 7.e
# import csv
# import os
# from collections import Counter
# path = r"D:\files\csv_files"
# os.chdir(path)
# d = {}
# with open("vaccination_data.csv") as file:
#     reader_obj = csv.DictReader(file, skipinitialspace = True)
#     for data in reader_obj:
#         if data["COUNTRY"] and data["PERSONS_VACCINATED_1PLUS_DOSE"] != ' ':
#                 d[data["COUNTRY"]] = data["PERSONS_VACCINATED_1PLUS_DOSE"]
#                 print(d[data["COUNTRY"]])
#
# res = sorted(d.items(), key=lambda item: (int(item[-1])) < 10000)
# print(res)