#PyPoll


import os
import csv

csvpath = "/Users/patrickwolfe/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes  = 0
khan_percent = 0.0
correy_percent = 0.0
li_percent = 0.0
otooley_percent= 0.0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
    
khan_percent = round(khan_votes / total_votes * 100, 2)
correy_percent = round(correy_votes / total_votes * 100, 2)
li_percent = round(li_votes / total_votes * 100, 2)
otooley_percent = round(otooley_votes / total_votes *100, 2)

if (khan_votes > correy_votes) and (khan_votes > li_votes) and (khan_votes > otooley_votes):
    top_vote_getter = "Khan"
elif (correy_votes > khan_votes) and (correy_votes > li_votes) and (correy_votes > otooley_votes):
    top_vote_getter = "Correy"
elif (li_votes > correy_votes) and (li_votes > khan_votes) and (li_votes > otooley_votes):
    top_vote_getter = "Li"
else:
    top_vote_getter = "O'Tooley"
    



print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print("-------------------------")
print(f"Winner: {top_vote_getter}")
