import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variables
is_first_month = True
first_month_pl = 0
last_month_pl = 0
total_months = 0
total = 0
greatest_increase = {"month": "", "amount": 0}
greatest_decrease = {"month": "", "amount": 0}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Loop through the rows
    for row in csvreader:
        month = row[0]
        current_month_pl = float(row[1])
        
        # Check if it's the first month
        if is_first_month:
            first_month_pl = current_month_pl
            is_first_month = False
        
        # Update totals
        total_months += 1
        total += current_month_pl
        
        # Calculate the profit/loss change
        if total_months > 1:  # Skip change calculation for the first month
            profit_change = current_month_pl - last_month_pl
            
            # Update greatest increase
            if profit_change > greatest_increase["amount"]:
                greatest_increase = {"month": month, "amount": profit_change}
            
            # Update greatest decrease
            if profit_change < greatest_decrease["amount"]:
                greatest_decrease = {"month": month, "amount": profit_change}
        
        # Update the last month's profit/loss
        last_month_pl = current_month_pl

    # Calculate average change
    avg_change = (last_month_pl - first_month_pl) / (total_months - 1)

# Prepare the results
results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${int(total)}",
    f"Average Change: ${round(avg_change, 2)}",
    f"Greatest Increase in Profits: {greatest_increase['month']} (${round(greatest_increase['amount'])})",
    f"Greatest Decrease in Profits: {greatest_decrease['month']} (${round(greatest_decrease['amount'])})",
]

# Convert results to a single string
output = "\n".join(results)

# Print results to the console
print(output)

# Write results to the file
output_path = os.path.join("analysis", "financialanalysis.txt")
with open(output_path, 'w', encoding='UTF-8') as writer:
    writer.write(output)