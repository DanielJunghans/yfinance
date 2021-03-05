#Code written by Daniel Junghans
#Danieljunghans.com
#Danjunghans@gmail.com

#yahoo_fin Documentation: https://github.com/ranaroussi/yfinance
import yfinance as yf
#CSV library will be used to export financial data scraped off of Yahoo Finance
import csv
import itertools
from yahoo_fin.stock_info import get_live_price
from yahoo_fin.stock_info import get_data

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

print('Select Sector (ConsumerCyclical/Materials)')
Sector = input()

###################################################################################################
###################################################################################################
Confirmed = 0
if Sector == 'ConsumerCyclical':
    Confirmed +=1
    #CONSUMER CYCLICAL
    Sector = ['tr','calm','epc','twnk','ipar','vgr',
    'bgs','core','fpafy','wmk','fdp','vitl','elf'
    ,'unfi','avo','lrn','chef','stkl','brbr','prdo',
    'ande','imkta','agro','sptn','rev','vff','coe',
    'new','one','vryyf','lsf','hmhc','nbev','free','cresy',
    'ngvc']
if Sector == 'Materials':
    Confirmed += 1
    #MATERIALS
    Sector = ['trox','cde','or','celtf','cstm','hbm',
    'gcp','ufs','iag','bcc','kro','mag','tse','sand','kalu','sa',
    'loma','ngd','fsm','silv','pilbf','foe','swm','svm','lac',
    'orocf','cenx','ocanf','hcc','drd','oec','kra','np','mos','door']

if Confirmed == 0:
    print('ERROR: PLEASE ENTER VALID SECTOR')
    exit()

print('')

###################################################################################################
###################################################################################################

#ALL RELEVANT FINANCIAL ACCOUNTS
Accounts =['Current_Ratio1','Current_Ratio2','Current_Ratio3','Current_Ratio4', 
    'Working_Capital1','Working_Capital2','Working_Capital3','Working_Capital4',
    'DTA1','DTA2','DTA3','DTA4','DTE1','DTE2','DTE3','DTE4','Gross_Profit_Margin1',
    'Gross_Profit_Margin2','Gross_Profit_Margin3','Gross_Profit_Margin4', 
    'Net_Profit_Margin1','Net_Profit_Margin2','Net_Profit_Margin3','Net_Profit_Margin4',
    'TAT1','TAT2','TAT3','ROA1','ROA2','ROA3','Inventory_Turnover1','Inventory_Turnover2',
    'Inventory_Turnover3','ADI1','ADI2','ADI3','FAT1','FAT2','FAT3','APT1','APT2','APT3',
    'AAP1','AAP2','AAP3','TIER1','TIER2','TIER3','TIER4','QOC1','QOC2','QOC3','QOC4','ROI']

#CREATING THE CSV
A = open('SIA_DATA.csv','w')
writer1 = csv.writer(A)
Col = ['Company'] + Accounts
writer1.writerow(Col)



print('                                                              Complete | Ticker')
print('###############################################################################')
#LOADING BAR
printProgressBar(0, len(Sector), prefix = 'Progress:', suffix = '   | ', length = 50)

















counter = 0

#This For loop will run for every Company in the SIA Portfolio and all functions
for Company in Sector:
    try:
        #collecting data and putting it in the data list
        Balance_Sheet = yf.Ticker(Company).balance_sheet
        Income_Statement = yf.Ticker(Company).financials
        Statement_Of_Cashflows = yf.Ticker(Company).cashflow
        #Income Statement
        Total_Revenue1 = Income_Statement.loc['Total Revenue'][0]
        Total_Revenue2 = Income_Statement.loc['Total Revenue'][1]
        Total_Revenue3 = Income_Statement.loc['Total Revenue'][2]
        try:
            Total_Revenue4 = Income_Statement.loc['Total Revenue'][3]
        except:
            Total_Revenue4 = 'N/A'

        Cost_Of_Revenue1 = Income_Statement.loc['Cost Of Revenue'][0]
        Cost_Of_Revenue2 = Income_Statement.loc['Cost Of Revenue'][1]
        Cost_Of_Revenue3 = Income_Statement.loc['Cost Of Revenue'][2]
        try:
            Cost_Of_Revenue4 = Income_Statement.loc['Cost Of Revenue'][3]
        except:
            Cost_Of_Revenue4 = 'N/A'

        Gross_Profit1 = Income_Statement.loc['Gross Profit'][0]
        Gross_Profit2 = Income_Statement.loc['Gross Profit'][1]
        Gross_Profit3 = Income_Statement.loc['Gross Profit'][2]
        try:
            Gross_Profit4 = Income_Statement.loc['Gross Profit'][3]
        except:
            Gross_Profit4 = 'N/A'

        Net_Income1 = Income_Statement.loc['Net Income'][0]
        Net_Income2 = Income_Statement.loc['Net Income'][1]
        Net_Income3 = Income_Statement.loc['Net Income'][2]
        try:
            Net_Income4 = Income_Statement.loc['Net Income'][3]
        except:
            Net_Income4 = 'N/A'

        Interest_Expense1 = Income_Statement.loc['Interest Expense'][0]
        Interest_Expense2 = Income_Statement.loc['Interest Expense'][1]
        Interest_Expense3 = Income_Statement.loc['Interest Expense'][2]
        try:
            Interest_Expense4 = Income_Statement.loc['Interest Expense'][3]
        except:
            Interest_Expense4 = 'N/A'

        Income_Tax1 = Income_Statement.loc['Income Tax Expense'][0]
        Income_Tax2 = Income_Statement.loc['Income Tax Expense'][1]
        Income_Tax3 = Income_Statement.loc['Income Tax Expense'][2]
        try:
            Income_Tax4 = Income_Statement.loc['Income Tax Expense'][3]
        except:
            Income_Tax4 = 'N/A'

        #Balance Sheet
        Total_Current_Assets1 = Balance_Sheet.loc['Total Current Assets'][0]
        Total_Current_Assets2 = Balance_Sheet.loc['Total Current Assets'][1]
        Total_Current_Assets3 = Balance_Sheet.loc['Total Current Assets'][2]
        try:
            Total_Current_Assets4 = Balance_Sheet.loc['Total Current Assets'][3]
        except:
            Total_Current_Assets4 = 'N/A'
        
        Total_Currnet_Liabilities1 = Balance_Sheet.loc['Total Current Liabilities'][0]
        Total_Currnet_Liabilities2 = Balance_Sheet.loc['Total Current Liabilities'][1]
        Total_Currnet_Liabilities3 = Balance_Sheet.loc['Total Current Liabilities'][2]
        try:
            Total_Currnet_Liabilities4 = Balance_Sheet.loc['Total Current Liabilities'][3]
        except:
            Total_Currnet_Liabilities4 = 'N/A'
        
        Total_Assets1 = Balance_Sheet.loc['Total Assets'][0]
        Total_Assets2 = Balance_Sheet.loc['Total Assets'][1]
        Total_Assets3 = Balance_Sheet.loc['Total Assets'][2]
        try:
            Total_Assets4 = Balance_Sheet.loc['Total Assets'][3]
        except:
            Total_Assets4 = 'N/A'

        Total_Liabilities1 = Balance_Sheet.loc['Total Liab'][0]
        Total_Liabilities2 = Balance_Sheet.loc['Total Liab'][1]
        Total_Liabilities3 = Balance_Sheet.loc['Total Liab'][2]
        try:
            Total_Liabilities4 = Balance_Sheet.loc['Total Liab'][3]
        except:
            Total_Liabilities4 = 'N/A'
        
        Inventory1 = Balance_Sheet.loc['Inventory'][0]
        Inventory2 = Balance_Sheet.loc['Inventory'][1]
        Inventory3 = Balance_Sheet.loc['Inventory'][2]
        try:
            Inventory4 = Balance_Sheet.loc['Inventory'][3]
        except:
            Inventory4 = 'N/A'
        
        Accounts_Payable1 = Balance_Sheet.loc['Accounts Payable'][0]
        Accounts_Payable2 = Balance_Sheet.loc['Accounts Payable'][1]
        Accounts_Payable3 = Balance_Sheet.loc['Accounts Payable'][2]
        try:
            Accounts_Payable4 = Balance_Sheet.loc['Accounts Payable'][3]
        except:
            Accounts_Payable4 = 'N/A'


        PPE1 = Balance_Sheet.loc['Property Plant Equipment'][0]
        PPE2 = Balance_Sheet.loc['Property Plant Equipment'][1]
        PPE3 = Balance_Sheet.loc['Property Plant Equipment'][2]
        try:
            PPE4 = Balance_Sheet.loc['Property Plant Equipment'][3]
        except:
            PPE4 = 'N/A'
        
        Stockholder_Equity1 = Balance_Sheet.loc['Total Stockholder Equity'][0]
        Stockholder_Equity2 = Balance_Sheet.loc['Total Stockholder Equity'][1]
        Stockholder_Equity3 = Balance_Sheet.loc['Total Stockholder Equity'][2]
        try:
            Stockholder_Equity4 = Balance_Sheet.loc['Total Stockholder Equity'][3]
        except:
            Stockholder_Equity4 = 'N/A'

        #Statement of Cashflows
        Cash_Flow_Operations1 = Statement_Of_Cashflows.loc['Total Cash From Operating Activities'][0]
        Cash_Flow_Operations2 = Statement_Of_Cashflows.loc['Total Cash From Operating Activities'][1]
        Cash_Flow_Operations3 = Statement_Of_Cashflows.loc['Total Cash From Operating Activities'][2]
        try:
            Cash_Flow_Operations4 = Statement_Of_Cashflows.loc['Total Cash From Operating Activities'][3]
        except:
            Cash_Flow_Operations4 = 'N/A'








        #Financial Ratios
        # Current Ratio
        Current_Ratio1 = Total_Current_Assets1/Total_Currnet_Liabilities1
        Current_Ratio2 = Total_Current_Assets2/Total_Currnet_Liabilities2
        Current_Ratio3 = Total_Current_Assets3/Total_Currnet_Liabilities3
        if Total_Revenue4 == 'N/A':
            Current_Ratio4 = 'N/A'
        else:
            Current_Ratio4 = Total_Current_Assets4/Total_Currnet_Liabilities4

        # Working Capital
        Working_Capital1 = Total_Current_Assets1-Total_Currnet_Liabilities1
        Working_Capital2 = Total_Current_Assets2-Total_Currnet_Liabilities2
        Working_Capital3 = Total_Current_Assets3-Total_Currnet_Liabilities3
        if Total_Revenue4 == 'N/A':
            Working_Capital4 = 'N/A'
        else:
            Working_Capital4 = Total_Current_Assets4-Total_Currnet_Liabilities4

        # Debt to Assets
        DTA1 = Total_Liabilities1/Total_Assets1
        DTA2 = Total_Liabilities2/Total_Assets2
        DTA3 = Total_Liabilities3/Total_Assets3
        if Total_Revenue4 == 'N/A':
            DTA4 = 'N/A'
        else:
            DTA4 = Total_Liabilities4/Total_Assets4

        # Debt ot Equity
        DTE1 = Total_Liabilities1/Stockholder_Equity1
        DTE2 = Total_Liabilities2/Stockholder_Equity2
        DTE3 = Total_Liabilities3/Stockholder_Equity3
        if Total_Revenue4 == 'N/A':
            DTE4 = 'N/A'
        else:
            DTE4 = Total_Liabilities4/Stockholder_Equity4

        # Gross Profit Margin
        Gross_Profit_Margin1 = Gross_Profit1/Total_Revenue1
        Gross_Profit_Margin2 = Gross_Profit2/Total_Revenue2
        Gross_Profit_Margin3 = Gross_Profit3/Total_Revenue3
        if Total_Revenue4 == 'N/A':
            Gross_Profit_Margin4 = 'N/A'
        else:
            Gross_Profit_Margin4 = Gross_Profit4/Total_Revenue4

        # Net profit Margin
        Net_Profit_Margin1 = Net_Income1/Total_Revenue1
        Net_Profit_Margin2 = Net_Income2/Total_Revenue2
        Net_Profit_Margin3 = Net_Income3/Total_Revenue3
        if Total_Revenue4 == 'N/A':
            Net_Profit_Margin4 = 'N/A'
        else:
            Net_Profit_Margin4 = Net_Income4/Total_Revenue4

        # Total Asset Turnover
        TAT1 = Total_Revenue1/(((Total_Assets1+Total_Assets2)/2))
        TAT2 = Total_Revenue2/(((Total_Assets2+Total_Assets3)/2))
        if Total_Revenue4 == 'N/A':
            TAT3 = 'N/A'
        else:
            TAT3 = Total_Revenue3/(((Total_Assets3+Total_Assets4)/2))

        # Return on Assets
        ROA1 = Net_Profit_Margin1 * TAT1
        ROA2 = Net_Profit_Margin2 * TAT2
        if Total_Revenue4 == 'N/A':
            ROA3 = 'N/A'
        else:
            ROA3 = Net_Profit_Margin3 * TAT3

        #Inventory Turnover
        Inventory_Turnover1 = Cost_Of_Revenue1/((Inventory1+Inventory2)/2)
        Inventory_Turnover2 = Cost_Of_Revenue2/((Inventory2+Inventory3)/2)
        if Total_Revenue4 == 'N/A':
            Inventory_Turnover3 = 'N/A'
        else:
            Inventory_Turnover3 = Cost_Of_Revenue3/((Inventory3+Inventory4)/2)

        # Average Days to Sell Inventory
        ADI1 = 365/Inventory_Turnover1
        ADI2 = 365/Inventory_Turnover2
        if Total_Revenue4 == 'N/A':
            ADI3 = 'N/A'
        else:
            ADI3 = 365/Inventory_Turnover3

        #Fixed Asset Turnover Ratio
        FAT1 = Total_Revenue1/((PPE1+PPE2)/2)
        FAT2 = Total_Revenue2/((PPE2+PPE3)/2)
        if Total_Revenue4 == 'N/A':
            FAT3 = 'N/A'
        else:
            FAT3 = Total_Revenue3/((PPE3+PPE4)/2)

        # Accounts Payable Turnover
        APT1 = Cost_Of_Revenue1/((Accounts_Payable1+Accounts_Payable2)/2)
        APT2 = Cost_Of_Revenue2/((Accounts_Payable2+Accounts_Payable3)/2)
        if Total_Revenue4 == 'N/A':
            APT3 = 'N/A'
        else:
            APT3 = Cost_Of_Revenue3/((Accounts_Payable3+Accounts_Payable4)/2)

        # Average Age of Payables
        AAP1 = 365/APT1
        AAP2 = 365/APT2
        if Total_Revenue4 == 'N/A':
            AAP3 = 'N/A'
        else:
            AAP3 = 365/APT3

        # Times Interest Earned Ratio
        TIER1 = (Net_Income1+Interest_Expense1+Income_Tax1)/Interest_Expense1
        TIER2 = (Net_Income2+Interest_Expense2+Income_Tax2)/Interest_Expense2
        TIER3 = (Net_Income3+Interest_Expense3+Income_Tax3)/Interest_Expense3
        if Total_Revenue4 == 'N/A':
            TIER4 = 'N/A'
        else:
            TIER4 = (Net_Income4+Interest_Expense4+Income_Tax4)/Interest_Expense4

        # Quality of Cash Flow 
        QOC1 = Cash_Flow_Operations1/Net_Income1
        QOC2 = Cash_Flow_Operations2/Net_Income2
        QOC3 = Cash_Flow_Operations3/Net_Income3
        if Total_Revenue4 == 'N/A':
            QOC4 = 'N/A'
        else:
            QOC4 = Cash_Flow_Operations4/Net_Income4

        Data_List = [Current_Ratio1,Current_Ratio2,Current_Ratio3,Current_Ratio4, 
        Working_Capital1,Working_Capital2,Working_Capital3,Working_Capital4,
        DTA1,DTA2,DTA3,DTA4,DTE1,DTE2,DTE3,DTE4,Gross_Profit_Margin1,Gross_Profit_Margin2,
        Gross_Profit_Margin3,Gross_Profit_Margin4, Net_Profit_Margin1,Net_Profit_Margin2,
        Net_Profit_Margin3,Net_Profit_Margin4,TAT1,TAT2,TAT3,ROA1,ROA2,ROA3,
        Inventory_Turnover1,Inventory_Turnover2,Inventory_Turnover3,ADI1,ADI2,ADI3,
        FAT1,FAT2,FAT3,APT1,APT2,APT3,AAP1,AAP2,AAP3,TIER1,TIER2,TIER3,TIER4,QOC1,QOC2,QOC3,QOC4]
        
        
        counter += 1 

        printProgressBar(counter, len(Sector), prefix = 'Progress:', suffix ='   | '+ str(Company), length = 50)

    except:
        pass



    