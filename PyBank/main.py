

import os

# Module for reading CSV files
import csv
import statistics

csvpath = os.path.join('budget_data.csv',)


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    #initiation value 0

    Total = 0
    count = 0 
    previous_value = 0
    change = []
    diff = 0
    months = []
    
    for row in csvreader:
        if(count == 0):
            previous_value = row[1]
        else:
            diff = int(row[1]) - int(previous_value)
            change.append(diff)
            previous_value = int(row[1])
        count = count + 1       
        Total += int(row[1])
        change.append(diff)
        months.append(row[0])


    
    print(f"Financial Analysis")
    print(f"------------------")
    
    print('Total Months: ' + str(count))
    print(f'Total: ${str(sum_money)}')
    print(f'Average Change: ${str(statistics.mean(change))}')
    print(f'Greatest Increase in Profits: ' + str(max(months)) + '($' + str(max(change)) + ')')
    print(f'Greatest Decrease in Profits: ' + str(min(months)) + '($' + str(min(change)) + ')')
# Financial Analysis
#-----------------------

#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)