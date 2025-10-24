import csv
import os
import pprint



os.chdir('/Users/pjangala/Desktop')
print(os.getcwd())

data={}
with open('Emp.csv','r') as f:
    csv_reader=csv.DictReader(f)
    for row in csv_reader:
        data[row['Emp Name']]=row


pprint.pprint(data['John'])


        

