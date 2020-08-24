

import os
import csv
import statistics


cvspath = os.path.join('election_data.csv',)
OutputFile = 'resultfile.txt'                                   
Total = 0                      
CandidateVotes = 0                                    
WinnerVotes = 0  
Votes = []                   
ListCandidate = []            
Winner = ''


with open(cvspath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

    for row in csvreader:
        Name = row[2]
        Votes.append(Name)

        Total += 1

        if ListCandidate.count(Name) == 0:
            ListCandidate.append(Name)


print('Election Results')
print('----------------')
print('Total Votes : ' + str(Total))
print('----------------')


for name in ListCandidate:


    CandidateVotes = Votes.count(name)


    Percentage = CandidateVotes/Total * 100
    

    if WinnerVotes < CandidateVotes:
        WinnerVotes = CandidateVotes
        Winner = name
    
    print(name + ' : ' + '{:.2f}'.format(Percentage) + '% - (' + str(CandidateVotes) + ')')

print('----------------')
print('Winner : ' + Winner)
print('----------------')



f = open(OutputFile, "w")       


f.write('Election Results\n')
f.write('----------------\n')
f.write('Total Votes : ' + str(Total) + '\n')
f.write('----------------\n')


for name in ListCandidate:


    CandidateVotes = Votes.count(name)

    Percentage = CandidateVotes/Total * 100
    
    f.write(name + ' : ' + '{:.2f}'.format(Percentage) + '% - (' + str(CandidateVotes) + '\n')

f.write('----------------\n')
f.write('Winner : ' + Winner + '\n')
f.write('----------------\n')

f.close

