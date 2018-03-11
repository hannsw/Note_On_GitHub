#! Python3
# removeCsvHeader.py - Remove the headers(1st row) from all CSV files

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current dir
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename +'.....')

    # Read the CSV file in (skip first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip the first row
        csvRows.append(row) # each row is a element in the list csvRows
    csvFileObj.close()

    # Write out the CSV File
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
