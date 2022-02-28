import os
import csv

pollData_csv = os.path.join("..","Resources","election_data.csv")
#currentDirectory = os.getcwd()
#print(currentDirectory)
#print(pollData)

# Open the CSV file
import csv

# dictionary with candidates as keys and votes as values
candidates = dict()
count=[]


# read the data file
with open(pollData_csv, 'r') as csv_file:
    elections_data = csv.reader(csv_file, delimiter=',')
    next(elections_data) # skip the header
    for row in elections_data: # iterate over all rows
       candidate = row[2] # candidate name
       # if candidate name is not in the dictionary, update the dictionary
       if candidate not in candidates.keys():
            candidates.update({candidate:0})
       # increment the number of votes by one
       candidates[candidate] += 1

      
    total_votes = sum(candidates.values())
    winner = max(candidates, key=lambda k: candidates[k])
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes:,}")
    print(f"winner:, {winner}")


    print("----------------------------")

# write results
    file_to_output = "resultsPoll.txt"
    with open(file_to_output, "w") as txt_file:
      txt_file.write(".....................................\n")
      txt_file.write(f"Total Votes: {total_votes:,}\n")
      txt_file.write(f"Winner: {winner} \n")
      txt_file.write(".....................................")
      
