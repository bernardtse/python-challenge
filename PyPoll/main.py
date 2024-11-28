import os
import csv

# Set path for file
csvpath = os.path.join("resources", "election_data.csv")

# Set variables
totalvotes = 0
candidates = {}  # A dictionary to hold candidate names and their vote counts

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row
    csv_header = next(csvreader)
 
    # Loop through looking for votes
    for row in csvreader:
        # Calculate total votes
        totalvotes += 1

        # Track votes for each candidate
        candidate = row[2]  # Candidate name is in the 3rd column (index 2)
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate percentages for each candidate
candidate_percentages = {candidate: (votes / totalvotes) * 100 for candidate, votes in candidates.items()}

# Determine the winner
winner = max(candidates, key=candidates.get)

# Prepare the results
results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {totalvotes}",
    "-------------------------",
]
for candidate, votes in candidates.items():
    percent = round(candidate_percentages[candidate], 3)
    results.append(f"{candidate}: {percent}% ({votes})")
results.extend([
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
])

# Convert results to a single string
output = "\n".join(results)

# Print results to the console
print(output)

# Write results to the file
output_path = os.path.join("analysis", "electionresults.txt")
with open(output_path, 'w', encoding='UTF-8') as writer:
    writer.write(output)