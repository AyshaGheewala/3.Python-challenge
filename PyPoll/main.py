# PyPoll
# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Define variables
    total_votes = 0
    candidates_list = []
    candidates_dict = {}
    vote_count = 0
    winner = ""

    for row in csvreader:

        # Find the total number of votes cast
        total_votes += 1

        # List of candidates
        candidate = (row[2])
        
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidates_dict[candidate] = 0

        candidates_dict[candidate] += 1
    
# Print analysis
analysis = f"""
Election Results
-------------------------
Total Votes: {total_votes}
------------------------- 
"""
print(analysis)

# Export text file with the results 
output_path = os.path.join("Analysis", "PyPoll_analysis.txt")
with open(output_path, "w") as file:
    file.write(analysis)

    # Total number & percentage of votes each candidate won
    for candidate in candidates_list:
        votes = candidates_dict[candidate]
        percentage = (votes / total_votes) * 100
        result = f"{candidate}: {round(percentage,3)}% ({votes})"
        print(result)
        file.write(f"{result}\n")

        # Identify the winner of the election
        if votes > vote_count:
            vote_count = votes
            winner = candidate

    # Print analysis
    analysis_ = f"""
    \n-------------------------
    \nWinner: {winner}
    \n-------------------------
    """
    print(analysis_)
    file.write(analysis_)
