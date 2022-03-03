import csv
with open('Emp.csv',newline='')as csvfile1:
data=csv.DictReader(csvfile1)
print("empnoempname")
print("--------------------")
for i in data:
print(i['empno'],i['empname'])
