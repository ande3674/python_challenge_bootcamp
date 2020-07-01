import pandas as pd
import numpy as np


def main():
    #read csv into pandas dataframe
    py_bank_df = pd.read_csv('budget_data.csv') 

    # Total number of months in the dataset
    month_count = py_bank_df["Date"].count()

    # Net profit/losses
    net_profit = py_bank_df["Profit/Losses"].sum()

    # The average of the changes in "Profit/Losses" 
    profit_loss_delta_list = []

    for index, pl in enumerate(py_bank_df["Profit/Losses"]):

        if index == 0:
            profit_loss_delta_list.append(0)
        else:
            delta = pl - py_bank_df["Profit/Losses"][index-1]
            profit_loss_delta_list.append(delta)

    # Average of change in profits
    average_change = sum(profit_loss_delta_list[1:])/len(profit_loss_delta_list[1:])

    # Greatest increase in profits (date and amount)
    greatest_increase = max(profit_loss_delta_list)
    greatest_increase_date = py_bank_df["Date"][profit_loss_delta_list.index(max(profit_loss_delta_list))]

    # Greatest decrease in profits (date and amount)
    greatest_decrease = min(profit_loss_delta_list)
    greatest_decrease_date = py_bank_df["Date"][profit_loss_delta_list.index(min(profit_loss_delta_list))]

    # Print Financial Analysis
    financial_analysis = 'Financial Analysis\n----------------------------\n' + \
        f'Total Months: {month_count}\nTotal: ${net_profit:,.2f}\nAverage Change: ${average_change:,.2f}\n' + \
        f'Greatest Increase in Profits: {greatest_increase_date}: ${greatest_increase:,.2f}\n' + \
        f'Greatest Decrease in Profits: {greatest_decrease_date}: ${greatest_decrease:,.2f}'
    print(financial_analysis)

    # Export to text file
    analysis_file = open("py_bank_results.txt","w")
    analysis_file.write(financial_analysis)
    analysis_file.close()        

main()
