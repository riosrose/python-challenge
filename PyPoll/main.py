import os
import csv

# Path to the CSV file
election_file_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
print("Looking for file at:", election_file_path)

# Check if the file exists
if not os.path.exists(election_file_path):
    print("File not found.")
    exit()

# Read the CSV file and confirm storing of the header
with open(election_file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Store the header row
    print("Header:", header)  # Print the header to verify

    # Print a sample of two rows of data
    for i, row in enumerate(reader):
        if i < 2:  # Only show the first two rows
            print("Sample Row:", row)
        else:
            break  # Exit the loop after two rows
        
        # Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(election_file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header

    for row in reader:
        voter_id, county, candidate = row
        
        # Count total votes
        total_votes += 1
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Prepare analysis results
analysis_results = (
    f"Total Votes: {total_votes}\n"
    f"Candidates and Votes:\n"
)

# Calculate percentages and determine the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Add winner to results
analysis_results += f"Winner: {winner}\n"

# Print results to terminal
print(analysis_results)

# Write results to a text file in the analysis folder
output_file = os.path.join(os.path.dirname(__file__), "analysis", "election_analysis.txt")
with open(output_file, 'w') as textfile:
    textfile.write(analysis_results)

print(f"Results have been written to {output_file}.")