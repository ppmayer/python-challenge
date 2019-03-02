import pandas as pd

#read csv file and create dataframe
csv_path = "election_data.csv"
elections_df = pd.read_csv(csv_path)

#Calculate total number of votes
TotalVotes=elections_df["Voter ID"].count()

#Create datafram that include votes per candidate and rename columns
CandidateVotes=elections_df["Candidate"].value_counts().reset_index()
CandidateVotes.rename(columns={"index":"Candidate","Candidate":"Number of Votes"},inplace=True)

#Add column that calculates the % of total votes
CandidateVotes["Percent of Votes"]=round(CandidateVotes["Number of Votes"]/TotalVotes*100)
CandidateVotes=CandidateVotes[["Candidate","Percent of Votes","Number of Votes"]]

#Identify winner
MaxVotes=CandidateVotes["Percent of Votes"].max()
MaxCandidate=CandidateVotes.loc[CandidateVotes["Percent of Votes"]==MaxVotes,"Candidate"]

#print to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: ",TotalVotes)
print("-------------------------------------------")
print (CandidateVotes.to_string(index=False))
print("-------------------------------------------")
print ("Winner: ",MaxCandidate.to_string(index=False))

#Write to .txt file 
OutputFile = open("PyPoll.txt", "w+")
print("Election Results", file = OutputFile)
print("-------------------------", file = OutputFile)
print("Total Votes: ",TotalVotes, file = OutputFile)
print("-------------------------------------------", file = OutputFile)
print (CandidateVotes.to_string(index=False), file = OutputFile)
print("-------------------------------------------")
print ("Winner: ",MaxCandidate.to_string(index=False), file = OutputFile)