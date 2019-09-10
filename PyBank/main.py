#Import dependencies
import os
import csv

#Define output file and create variables for the analyzed data
resultsFile = r"C:\Users\klsom\Documents\GitHub\Python\PyBank\Financial_Analysis.txt"
from decimal import Decimal
profitLoss = []
summaryProfitLoss = {}

####Why did I have to use this version?????
#Define location and read in CSV file
budgetFile = os.path.join(r"C:\Users\klsom\Documents\GitHub\Python\PyBank\Resources\budget_data.csv")
with open(budgetFile) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    #Skip header row
    next(csvReader)

    netTotal = 0
    totalMonths = 0

    #Convert budgetFile to a list
    for row in csvReader:
        profitLoss.append(row)
        netTotal += int(row[1])
        totalMonths += 1

    subtractPL = 0
    totalPL = 0
    averagePL = 0

    #Initialize calculation variables
    greatestDecrease = int(profitLoss[totalMonths-1][1])-int(profitLoss[totalMonths-2][1])
    greatestIncrease = int(profitLoss[totalMonths-1][1])-int(profitLoss[totalMonths-2][1])

    #Perform calculations
    for row in range(totalMonths,1,-1):
        subtractPL = int(profitLoss[row-1][1])-int(profitLoss[row-2][1])
        if subtractPL < greatestDecrease:
            minDate = profitLoss[row-1][0]
            greatestDecrease = subtractPL
        elif subtractPL > greatestIncrease:
            greatestIncrease = subtractPL
            maxDate = profitLoss[row-1][0]
        totalPL = totalPL + subtractPL

    totalPL = float(totalPL)
    totalMonths = float(totalMonths)
    averagePL = (totalPL/(totalMonths-1))

    #Print results of script
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths:.0f}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${averagePL:.2f}")
    print(f"Greatest Increase in Profits: {maxDate} $({greatestIncrease})")
    print(f"Greatest Decrease in Profits: {minDate} $({greatestDecrease})")

#Print results to text file
text_file=open(resultsFile,"w")
text_file.write("Financial Analysis")
text_file.write("\n----------------------------")
text_file.write(f"\nTotal Months: {totalMonths:.0f}")
text_file.write(f"\nTotal: ${netTotal}")
text_file.write(f"\nAverage Change: ${averagePL:.2f}")
text_file.write(f"\nGreatest Increase in Profits: {maxDate} $({greatestIncrease})")
text_file.write(f"\nGreatest Decrease in Profits: {minDate} $({greatestDecrease})")
text_file.close()
