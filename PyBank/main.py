import pandas as pd

csv_path = "budget_data.csv"
profitability_df = pd.read_csv(csv_path)
NumMonths=profitability_df["Date"].count()
#print(NumMonths)
TotalProfits=profitability_df["Profit/Losses"].sum()
#print(TotalProfits)
ProfitChange=profitability_df["Profit/Losses"].diff()
ProfitChangeMean=ProfitChange.mean()
#print(ProfitChangeMean)
profitability_df["Profit Delta"]=ProfitChange
#print(profitability_df)
MaxProfitChange=profitability_df["Profit Delta"].max()
MaxProfitIndex=profitability_df["Profit Delta"].idxmax(axis=0, skipna=True)
MaxDate=profitability_df.loc[MaxProfitIndex]["Date"]
#print(MaxProfitChange)
#print(MaxProfitIndex)
MinProfitChange=profitability_df["Profit Delta"].min()
MinProfitIndex=profitability_df["Profit Delta"].idxmin(axis=0, skipna=True)
MinDate=profitability_df.loc[MinProfitIndex]["Date"]
#print(MinProfitChange)
#print(MinProfitIndex)

print("Financial Analysis")
print("------------------------")
print("Total Months:"+ str(NumMonths))
print("Total Profits: $"+ str(TotalProfits))
print("Average Monthly Delta: $"+ str(ProfitChangeMean))
print("Greatest Increase in Profits: "+ str(MaxDate)+" ($"+str(MaxProfitChange)+")")
print("Greatest Decrease in Profits: "+ str(MinDate)+" ($"+str(MinProfitChange)+")")