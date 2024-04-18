
import os
import csv
from collections import Counter

#Define variable for the analysis
#this list is hold all the records in election_data.csv file
#alter add all the voting as list of dictionary to the list
votedictionary=[]

#Define the file path to open the 
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open the CSV using the UTF-8 encoding
with open(csvpath,"r", encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #Exclude the collumn heders from the calculations
    csvheader=next(csvreader)
    #loop the entire records in the csv file
    for row in csvreader:
       #create a new record for each bellot id
       new_vote = {'Candidate': row[2], 'County': row[1],'BallotID':row[0]}
       #append the recods to the list from the csv file
       #this data will be used to print the summary of the election
       votedictionary.append(new_vote)
    #close the opened csv file
    csvfile.close

#summarise the data for analysis
#to use the "Counter", first "from collections import Counter" has to be imported
summary_list =Counter(d['Candidate'] for d in votedictionary)
#get the total number of votes
total_votes=summary_list.total()
#Get the list of unique candidates from the summary list to print the analysis data
candidate_list=list(summary_list)
#print the analysis to the terminal 

    #print summary to the terminal
print("Election Results") 
print("-------------------------")  
print(f"Total votes :{total_votes}")
print("-------------------------")
winner=""
highestvotes=0
#loop trough the candidate list to prin the summary using the candidate_list
for elem in candidate_list:
    #print(summary_list.elements[elem])
    #print to the terminal
    print(f"{elem} :{(summary_list[elem]/total_votes):.3%} {summary_list[elem]}")
    if summary_list[elem]>highestvotes:
        highestvotes=summary_list[elem]
        winner=elem

print("-------------------------")
#print the winner
print(f"The Winner is: {winner} having {highestvotes} votes.")
print("-------------------------")    

#and writes to a text file
highestvotes=0
winner=""
txtfilepath=os.path.join('.','analysis','output.txt') 
with open(txtfilepath,'w',encoding='utf-8') as file:
    
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total votes :{total_votes}\n")
    file.write("-------------------------\n")
    #loop trough the candidate list to prin the summary using the candidate_list
    for elem in candidate_list:
         #writes to the text file
        file.write(f"{elem} :{(summary_list[elem]/total_votes):.3%} ({summary_list[elem]})\n")
        if summary_list[elem]>highestvotes:
            highestvotes=summary_list[elem]
            winner=elem

    #Print the winner    
    file.write("-------------------------\n")
    file.write(f"The Winner is: {winner} having {highestvotes} votes.\n")
    file.write("-------------------------\n") 
file.close

    
    
