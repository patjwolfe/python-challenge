#PyBank

import os
import csv
from datetime import datetime

csvpath = "/Users/patrickwolfe/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

min_month = datetime.strftime(Jan-2011, '%m-%Y')
max_month = min_month
print(min_month)


# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     for row in csvreader:
#         if datetime.strptime(row[0]) < min_month
#             min_month = row[0]
#         if row[0] > max_month
#             max_month = row[0]
#         if row[0] - last_month_profit_loss > greatest_increase_profits
#             greatest_increase_profits = row[0] - last_month_profit_loss
#         if row[0] - last_month_profit_loss < greatest_decrease_profits
#             greatest_decrease_profits = row[0] - last_month_profit_loss
#         row[0] = last_month_profit_loss

        
#     total_months = max_month - min_month
#     total_profit_loss = row[1] + total_profit_loss
#     average_change = total_profit_loss / total_months


# print(f"Total Months: {total_months}")
# print(f"Total ${total_profit_loss}")
# print(f"Average  Change: {average_change}")
# print(f"Greatest Increase in Profits: {greatest_increase_profits}")
# print(f"Greatest Decrease in Profits: {greatest_decrease_profits}")