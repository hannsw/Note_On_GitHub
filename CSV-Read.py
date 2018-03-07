import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
# then use exampleData[row][col] to get str/value

#--------------------------------------------
#Read a line each time
import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print(row)   # row[N] get all values in coloum N
