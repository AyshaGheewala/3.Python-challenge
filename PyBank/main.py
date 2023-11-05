# PyBank
# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Define variables
    total_months = 0
    net_total = 0
    total_changes = 0
    change = 0
    change_count = 0
    previous_revenue = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""


    for row in csvreader:

        # Find the total number of months 
        total_months += 1

        # Calculate the net total amount of Profit/Losses
        profit_loss = int(row[1])
        net_total += profit_loss

        # Changes in profit/losses
        if row[0] != "Jan-10":
            change = profit_loss - previous_revenue
            total_changes += change
            change_count += 1
        previous_revenue = profit_loss

        # Greatest Increase in profits
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]

        # Greatest Decrease in profits
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]

    # Calculate the average
    average = total_changes / change_count

# Print analysis
analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${round(average,2)} 
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""
print(analysis)

# Export text file with the results 
output_path = os.path.join("Analysis", "Pybank_analysis.txt")
with open(output_path, "w") as file:
    file.write(analysis)





        
       