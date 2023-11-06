# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variables
# Profit/loss for the first month
isfirstmonth = True
firstmonthpl = 0

# Profit/loss for the last month
lastmonthpl = 0

# Other variables
totalmonth = 0
total = 0
profitchange = 0
greatestincreasemonth = ""
greatestincrease = 0
greatestdecreasemonth = ""
greatestdecrease = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row without printing it out
    csv_header = next(csvreader)
 
    # Loop through looking for the data
    for row in csvreader:
        # Check first month
        if isfirstmonth == True:
            firstmonthpl = float(row[1])
            isfirstmonth = False
        
        # Check total month
        totalmonth = totalmonth + 1
        
        # Calculate total
        total = total + float(row[1])
        
        # Check profit change
        profitchange = float(row[1]) - lastmonthpl

        # Check greatest increase and greatest decrease

        if profitchange > greatestincrease:
            greatestincreasemonth = row[0]
            greatestincrease = profitchange
        
        if profitchange < greatestdecrease:
            greatestdecreasemonth = row[0]
            greatestdecrease = profitchange
        
        # Record profit/loss for the month
        lastmonthpl = float(row[1])
    

    # Calculate average change after loop (total number of changes = totalmonth-1)
    avgchange = (lastmonthpl - firstmonthpl) / (totalmonth - 1)
    
    # Print results
    
    line1 = "Financial Analysis"
    line2 = "----------------------------"
    line3 = "Total Months: " + str(totalmonth)
    line4 = "Total: $" +str(int(total))
    line5 = "Average Change: $" + str(round(avgchange,2))
    line6 = "Greatest Increase in Profits: " + str(greatestincreasemonth) + " ($" + str(round(greatestincrease)) + ")"
    line7 = "Greatest Decrease in Profits: " + str(greatestdecreasemonth) + " ($" + str(round(greatestdecrease)) + ")"
    
    alllines = (line1 , line2, line3, line4, line5, line6, line7)
    for line in alllines:
        print(line)

    # Specify the file to write to
    output_path = os.path.join("analysis", "financialanalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
writer = open(output_path, 'w', encoding='UTF-8')

# Write the file
for line in alllines:
    writer.write(line)
    writer.write("\n")

# Close file
writer.close 
    