#!/usr/bin/env python
# coding: utf-8

# In[50]:


#PyPoll Instructions & Output
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# Setting Dependencies
import csv
import os

# Uploading csv file & setting OS path
file_source = os.path.join(".","Resources","election_data.csv")

# Set file output
file_output = os.path.join(".","Analysis", "election_analysis.txt")

# Setting Variables
total_votes = 0

# Winner Tracker
winning_candidate = ""
winner_count = 0

# Candidate Tracker
candidate_votes = {}
candidates = []




# Read source file and view as list
with open(file_source) as election_data:
    reader = csv.reader(election_data)
    
    # Read & Store Header
    header = next(reader)
   
    #print(f"HEADER: {header}")
    first_row = next(reader)
    
    
    total_votes += 1
    
    for row in reader:
        # Adding total votes
        total_votes += 1 
        
        # Gets candidate name from each row
        candidate_name = row[2]
        
        # Find unique candidates by comparing each row and appending unique to list
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
            
            
        candidate_votes[candidate_name] += 1
            
    

# Storing & Printing election output
election_output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

print(election_output,end="")

# Output File
with open(file_output,"w") as txt_file:
    txt_file.write(election_output)

    # Calculating total votes
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes) * 100
        
        if(votes > winner_count):
            winner_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        print(voter_output, end="")
        
        txt_file.write(voter_output)
    

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)


# In[ ]:




