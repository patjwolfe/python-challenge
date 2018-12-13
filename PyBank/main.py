#PyBank

import os
import csv
import datetime

csvpath = "/Users/patrickwolfe/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

last_month_profit_loss = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
total_profit_loss = 0
total_months = 1
current_profit_loss = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    start_month = next(csvreader)
    for row in csvreader:
        end_month = row[0]
        current_profit_loss = int(row[1])
        if current_profit_loss  > greatest_increase_profits:
            greatest_increase_profits = current_profit_loss
            greatest_increase_month = row[0]
        if current_profit_loss  < greatest_decrease_profits:
            greatest_decrease_profits = current_profit_loss
            greatest_decrease_month = row[0]
        total_profit_loss = total_profit_loss + current_profit_loss 
        total_months = total_months + 1


# total_months = datetime.datetime.strptime(max_month, date_format) - datetime.datetime.strptime(min_month, date_format)

average_change = total_profit_loss / total_months

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})")



output_path = "02-Homework/03-Python/Instructions/PyBank/Resources/output.txt"


with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("----------------------------")
    csvwriter.writerow(f"Total Months: {total_months}")
    csvwriter.writerow(f"Total ${total_profit_loss}")
    csvwriter.writerow(f"Average Change: ${average_change}")
    csvwriter.writerow(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})")
