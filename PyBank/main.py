import pandas as pd

#read csv file and create dataframe
csv_path = "budget_data.csv"
profitability_df = pd.read_csv(csv_path)

#Calculate total number of months
NumMonths=profitability_df["Date"].count()

#Calculate total profits
TotalProfits=profitability_df["Profit/Losses"].sum()

#Calculate profit/loss deltas and average delta
ProfitChange=profitability_df["Profit/Losses"].diff()
ProfitChangeMean=ProfitChange.mean()

#Add profit deltas as column to dataframe
profitability_df["Profit Delta"]=ProfitChange

#Identify max and min profit deltas and corresponding date
MaxProfitChange=profitability_df["Profit Delta"].max()
MaxProfitIndex=profitability_df["Profit Delta"].idxmax(axis=0, skipna=True)
MaxDate=profitability_df.loc[MaxProfitIndex]["Date"]
MinProfitChange=profitability_df["Profit Delta"].min()
MinProfitIndex=profitability_df["Profit Delta"].idxmin(axis=0, skipna=True)
MinDate=profitability_df.loc[MinProfitIndex]["Date"]

#print to terminal
print("Financial Analysis")
print("------------------------")
print("Total Months:"+ str(NumMonths))
print("Total Profits: $"+ str(TotalProfits))
print("Average Monthly Delta: $"+ str(round(ProfitChangeMean)))
print("Greatest Increase in Profits: "+ str(MaxDate)+" ($"+str(MaxProfitChange)+")")
print("Greatest Decrease in Profits: "+ str(MinDate)+" ($"+str(MinProfitChange)+")")

#Write to .txt file 
OutputFile = open("PyBank.txt", "w")
#print("test", file = OutputFile)
print("Financial Analysis", file = OutputFile)
print("------------------------", file = OutputFile)
print("Total Months:"+ str(NumMonths), file = OutputFile)
print("Total Profits: $"+ str(TotalProfits), file = OutputFile)
print("Average Monthly Delta: $"+ str(round(ProfitChangeMean)), file = OutputFile)
print("Greatest Increase in Profits: "+ str(MaxDate)+" ($"+str(round(MaxProfitChange))+")", file = OutputFile)
print("Greatest Decrease in Profits: "+ str(MinDate)+" ($"+str(round(MinProfitChange))+")", file = OutputFile)