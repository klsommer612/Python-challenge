#Import dependencies
import os
import csv

#Define output file and create variables for the analyzed data
resultsFile = "Election_Results.txt"
from decimal import Decimal
ballot = []
summaryVotes = []

#Define location and read in CSV file
electionFile = os.path.join("Resources","budget_data.csv")
with open(electionFile,newline="") as csvfile:
    csvReader = csv.reader(csvfile)
    #Skip the header
    next(csvReader)

    voteCount = 0

    #Tally votes
    for row in csvReader:
        voteCount = voteCount + 1
        candidate = row[2]

        if candidate in ballot:
            candidateVotes = ballot.index(candidate)
            summaryVotes[candidateVotes] = summaryVotes[candidateVotes] + 1
        else:
            ballot.append(candidate)
            summaryVotes.append(1)
   
percentageOfVotes = []
totalVotes = summaryVotes[0]
trackIndex = 0

#Percentage of votes and winner
for count in range(len(ballot)):
    vote_percentage = summaryVotes[count]/voteCount*100
    percentageOfVotes.append(vote_percentage)
    if summaryVotes[count] > totalVotes:
        totalVotes = summaryVotes[count]
        print(totalVotes)
        trackIndex = count
winner = ballot[trackIndex]

#Print results of script
print("Election Results")
print("--------------------------")
print(f"Total Votes: {voteCount}")
print("--------------------------")
for count in range(len(ballot)):
    print(f"{ballot[count]}: {percentageOfVotes[count]:.3f}% ({summaryVotes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#Print results to text file
text_file=open(resultsFile,"w")
text_file.write("\nElection Results")
text_file.write("\n----------------------------")
text_file.write(f"\nTotal Votes : {voteCount:.0f}")
text_file.write("\n----------------------------")
for count in range(len(ballot)):
    text_file.write(f"\n{ballot[count]}: {percentageOfVotes[count]:.3f}% ({summaryVotes[count]})")
text_file.write("\n----------------------------")
text_file.write(f"\nWinner: {winner}")
text_file.write("\n---------------------------")
text_file.close()
