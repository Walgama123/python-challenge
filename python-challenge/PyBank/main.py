
import os
import csv

 #Define variable for the analysis
number_of_months=0
net_total=0.00
net_change=0.00
averagechange=0.00
last_month_value=0.00
current_month_change=0.00
greatest_increase=0.00
greatest_increase_month=""
greatest_decrease=0.00
greatest_decrease_month=""
#this variable is used to identified the firt momth of the list
#it is valued is changed to false for rest of the months in the list
firstmonth=True

#Define the file path to open the 
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Open the CSV using the UTF-8 encoding
with open(csvpath,"r", encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
      
    for row in csvreader:
        number_of_months=number_of_months+1
        net_total=net_total+float(row[1])
        if firstmonth==False:
            current_month_change=float(row[1])-last_month_value
        else:
            current_month_change=0
        #Assign the current month value to calculate the next month change
        last_month_value=float(row[1])
        #summup the net_change
        net_change=net_change+current_month_change
        #Reassign the greatest increase and gretest descrese
        if current_month_change>greatest_increase:
            greatest_increase=current_month_change
            greatest_increase_month=row[0]

        if current_month_change<greatest_decrease:
            greatest_decrease=current_month_change
            greatest_decrease_month=row[0] 
        #reset the first month flag to false
        firstmonth=False
       
    #Close the budget_data.csv file        
    csvfile.close
    
#Create summary file
txtpath = os.path.join('.', 'analysis', 'output.txt')

with open(txtpath, 'w') as file:
    # Write data to the file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months : {number_of_months}\n")
    file.write(f"Total:: ${int(net_total)}\n")
    file.write(f"Average Change: ${int(net_change/(number_of_months-1))}\n")    
    file.write(f"Greatest Increase in Profits::{greatest_increase_month} ( ${int(greatest_increase)})\n")
    file.write(f"Greatest Decrease in Profits::{greatest_decrease_month} ( ${int(greatest_decrease)})\n")
file.close
#print the analysis to the terminal 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {number_of_months}")
print(f"Total:: ${int(net_total)}")
print(f"Average Change: ${int(net_change/(number_of_months-1))}")    
print(f"Greatest Increase in Profits::{greatest_increase_month} ( ${int(greatest_increase)})")
print(f"Greatest Decrease in Profits::{greatest_decrease_month} ( ${int(greatest_decrease)})")