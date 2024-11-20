import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Set variables
totalvotes = 0
candidates = {}  # A dictionary to hold candidate names and their vote counts

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row without printing it out
    csv_header = next(csvreader)
 
    # Loop through looking for votes
    for row in csvreader:
        
        # Calculate total votes
        totalvotes += 1

        # Track votes for each candidate
        candidate = row[2]  # Assuming candidate name is in the 3rd column (index 2)
        if candidate in candidates:
            candidates[candidate] += 1  # Add a vote if candidate already in dictionary
        else:
            candidates[candidate] = 1   # Initialize the vote count for the candidate

# Calculate percentages for each candidate
candidate_percentages = {}
for candidate, votes in candidates.items():
    candidate_percentages[candidate] = (votes / totalvotes) * 100

# Determine the winner by finding the candidate with the maximum vote count
winner = max(candidates, key=candidates.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percent = round(candidate_percentages[candidate], 3)
    print(f"{candidate}: {percent}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the file to write to
output_path = os.path.join("analysis", "electionresults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', encoding='UTF-8') as writer:
    writer.write("Election Results\n")
    writer.write("-------------------------\n")
    writer.write(f"Total Votes: {totalvotes}\n")
    writer.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percent = round(candidate_percentages[candidate], 3)
        writer.write(f"{candidate}: {percent}% ({votes})\n")
    writer.write("-------------------------\n")
    writer.write(f"Winner: {winner}\n")
    writer.write("-------------------------\n")