#PyPoll


import os
import csv

csvpath = "/Users/patrickwolfe/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

total_votes = 0
khan_votes, correy_votes, li_votes, otooley_votes  = 0
khan_percent, correy_percent, li_percent, otooley_percent= 0.000


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == "Khan"
            khan_votes = khan_votes + 1
        elif row[2] == "Correy"
            correy_votes = correy_votes + 1
        elif row[2] == "Li"
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley"
            otooley_votes = otooley_votes + 1
    
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

print("Election Results"
print("-------------------------")
print(f"Total Votes: {total_votes}")"
print("-------------------------")
print(f"Khan: {khan_percent} ({khan_votes}")
print(f"Correy: {correy_percent} ({correy_votes})")
print(f"Li: {li_percent} ({li_votes})")
print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
print("-------------------------")
# Winner: Khan