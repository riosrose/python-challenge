import os
import csv

# Path to the CSV file
budget_file_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
print("Looking for file at:", budget_file_path)

# Check if the file exists
if not os.path.exists(budget_file_path):
    print("File not found.")
    exit()

# Read the CSV file and confirm storing of the header
with open(budget_file_path, mode='r') as csvfile:
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
total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the CSV file
with open(budget_file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header
    
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        total_months += 1
        net_total += profit_loss
        
        if total_months > 1:
            change = profit_loss - previous_profit
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        previous_profit = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare results
analysis_results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print results
print(analysis_results)

# Write results to a text file in the analysis folder
output_file = os.path.join(os.path.dirname(__file__), "analysis", "financial_analysis.txt")
with open(output_file, 'w') as textfile:
    textfile.write(analysis_results)

print(f"Results have been written to {output_file}.")