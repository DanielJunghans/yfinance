import yfinance as yf

msft = yf.Ticker("MSFT")

Company_Data = msft.cashflow

print(Company_Data)
