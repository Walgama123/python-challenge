# VBA-challenge


Background
This project is aimed at practicing basic VBA scripting fundamentals.

Scripting fundamentals covered in this project.
	Using “For Each” loop Iterate through each sheet in excel workbook.
	Using “For loop” iterate for all the rows in a given sheet.
	Conditional formatting like change background color, number formatting cells by using “If , Else If and Else”  
	How to find the first row and last row for the currently running entity 
	How to add and rename new columns to a sheet.
Data source  
	The sample excel file contains opening daily changes of the stock prices of some selected companies for several years. Each sheet contains multiple companies’ data for a given year. Format of the data set is  as follows:
<ticker>	<date>	<open>	<high>	<low>	<close>	<vol>

Instructions
	Create a script that loops through all the stocks for one year and outputs the following information:
	Add ticker symbol
	Yearly change from the opening price at the beginning of a given year to the closing price at the end of that year.
	The percentage change from the opening price at the beginning of a given year to the closing price at the end of that year.
	The total stock volume of the stock. 

Formulas for the calculation.
	Yearly Change = Closing Price - Opening Price
	Percentage Change = (Yearly Change / Opening Price) * 100
	Total Stock Volume = Sum of Volume for all Trading Days

Sub modules 
	StockPriceSummary
		This sub procedure iterates through all the sheets as well as the all the records and do the required calculation to find out the summaries for each tickers.
		Further summary of the records set is printed for each tickers.
	FindGereatestValues
		This module accept one parameter as a worksheet and find out the highest increased ,lowest decreased and the total volume for a given year.
	ResetWork
		This sub function is used to initialized all the sheet in the workbook to run a new summary calculation. 




