#Code written by Daniel Junghans
#Danieljunghans.com
#Danjunghans@gmail.com

#yahoo_fin Documentation: https://github.com/ranaroussi/yfinance
import yfinance as yf
#CSV library will be used to export financial data scraped off of Yahoo Finance
import csv
import itertools

#All of the companies in the SIA portfolio
Companies = ['calm','syk','evtc']
#,'blkb','dlb',
#'ens','hban','door','ecpg','pb','zagg','laz',
#'hlx','mos','ha','brew','ctb','glll']

#All of the Accounting Accounts
Accounts =['Total Current Assets','Cost Of Revenue',
'Total Cash From Operating Activities']

#Setting up the CSV file
A = open('SIA_DATA.csv','w')
writer1 = csv.writer(A)
Col = ['Company'] + Accounts
writer1.writerow(Col)

#creating the last company tracker
Last_Company = Companies[0]

#list containing all of the info
Data_List = []

#This For loop will run for every Company in the SIA Portfolio and all functions
for Company, Account in itertools.product(Companies,Accounts):

    #checks to see if the company is different 
    if not Company == Last_Company:
        print("Completed=",Last_Company)
        writer1.writerow([Last_Company]+Data_List)
        Data_List = []
        Last_Company = Company

    #collecting data and putting it in the data list
    Balance_Sheet = yf.Ticker(Company).balance_sheet
    Income_Statement = yf.Ticker(Company).financials
    Statement_Of_Cashflows = yf.Ticker(Company).cashflow

    try:
        Value = Balance_Sheet.loc[Account][0]
        Data_List.append(Value)

    except:
        pass
    
    try:
        Value = Income_Statement.loc[Account][0]
        Data_List.append(Value)

    except:
        pass

    try:
        Value = Statement_Of_Cashflows.loc[Account][0]
        Data_List.append(Value)

    except:
        pass

print("Completed=",Last_Company)
writer1.writerow([Last_Company]+Data_List)


########TO DO
#use yahoo_fin to gather company tickers based on sector and market cap

