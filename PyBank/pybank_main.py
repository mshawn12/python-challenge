#!/usr/bin/env python
# coding: utf-8

# In[44]:


## PyBank Instructions & output results
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Setting Dependencies
import csv
import os

# Uploading csv file & setting OS path
file_source = os.path.join(".","Resources","budget_data.csv")

# Set file output
file_output = os.path.join(".","Analysis", "budget_analysis.txt")

# Setting variables
total_months = 0
total = 0
net_change_list = []
month_of_changes = []

greatest_increase =["",0]
greatest_decrease =["",99999999999999]


# Read source file and view as list
with open(file_source) as financial_data:
    reader = csv.reader(financial_data)
    
    # Read & Store Header
    header = next(reader)
   
    #print(f"HEADER: {header}")
    first_row = next(reader)
    
    total += int(first_row[1])
    previous_net = int(first_row[1])

    total_months += 1
    
    for row in reader:
        # Tracking & calculating totals
        total_months += 1
        total += int(row[1])

        # Net Change - going row by row, appending changes each time
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        
        # Calculating Greatest Increase: Loops through all values and finds which one is the greatest
        if (net_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        # Calculating Greatest Decrease -- comparing it to values set above 
        if (net_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        
        
# Creating variable to calculate average change
net_monthly_average = sum(net_change_list)/len(net_change_list)
        
# Storing & Printing Financial Analysis output
financial_output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    
)

print(financial_output)

# Output File
with open(file_output,"w") as txt_file:
    txt_file.write(financial_output)


# In[ ]:




