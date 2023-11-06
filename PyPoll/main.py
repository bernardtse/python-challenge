# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Set variables

# Candidate names
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"

# Candidate vote count
can1vote = 0
can2vote = 0
can3vote = 0

# Candidate vote percentage
can1percent = 0
can2percent = 0
can3percent = 0

# Other variables
totalvotes = 0
winner = ""

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row without printing it out
    csv_header = next(csvreader)
 
    # Loop through looking for votes
    for row in csvreader:
        
        # Calculate total vote
        totalvotes = totalvotes + 1

        # Votecount for individual candidates
        if row [2] == candidate1:
            can1vote = can1vote + 1
        if row [2] == candidate2:
            can2vote = can2vote + 1
        if row [2] == candidate3:
            can3vote = can3vote + 1
        
# Calculate vote percentage
can1percent = can1vote / totalvotes * 100
can2percent = can2vote / totalvotes * 100
can3percent = can3vote / totalvotes * 100

# Check winner
if can1vote > can2vote and can1vote > can3vote:
    winner = candidate1
elif can2vote > can1vote and can2vote > can3vote:
    winner = candidate2
elif can3vote > can1vote and can3vote > can2vote:
    winner = candidate3

# Print results

line1 = "Election Results"
line2 = "-------------------------"
line3 = "Total Votes: " + str(totalvotes)
line4 = "-------------------------"
line5 = candidate1 + ": " + str(round(can1percent, 3)) + "% (" + str(can1vote) + ")"
line6 = candidate2 + ": " + str(round(can2percent, 3)) + "% (" + str(can2vote) + ")"
line7 = candidate3 + ": " + str(round(can3percent, 3)) + "% (" + str(can3vote) + ")"
line8 = "-------------------------"
line9 = "Winner: " + winner
line10 = "-------------------------"

alllines = (line1 , line2, line3, line4, line5, line6, line7, line8, line9, line10)
for line in alllines:
    print(line)
    
# Specify the file to write to
output_path = os.path.join("analysis", "electionresults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
writer = open(output_path, 'w', encoding='UTF-8')

# Write the file
for line in alllines:
    writer.write(line)
    writer.write("\n")
    
# Close file
writer.close
