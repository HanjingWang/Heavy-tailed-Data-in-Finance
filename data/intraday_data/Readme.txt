Data is from http://www.kibot.com/buy.aspx.

The Data includes:

1. IBM (International Business Machines) Regular session data from Jan 1998    
2. IVE (S&P 500 Value Index) Data from Sep 2009
3. OIH (Market Vectors Oil Services ETF) Regular session data from Dec 2011 
4. WDC (Western Digital) Data from Feb 2010

1. What is the format of your minute data?
We use standard comma-delimited text files. This is the order of the fields in every 1 minute or higher interval file: 
Date,Time,Open,High,Low,Close,Volume.

For example, IBM_adjusted.txt IBM_unadjusted.txt OIH_adjusted.txt OIH_unadjusted.txt

2. What is the format of your tick data?
The order of the fields in the tick files (with bid/ask prices) is: Date,Time,Price,Bid,Ask,Size. 
Our bid/ask prices are recorded whenever a trade occurs and they represent the "national best bid and offer" (NBBO) 
prices across multiple exchanges and ECNs.

For example, IVE_tickidask.txt WDC_tickidask.txt

3. What is the format of your aggregate bid/ask data?
The order of the fields in our aggregate bid/ask files is: Date,Time,BidOpen,BidHigh,BidLow,BidClose,AskOpen,AskHigh,AskLow,AskClose

For example, IVE_bidask1min.txt