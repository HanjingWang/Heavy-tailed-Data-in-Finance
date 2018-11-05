# Heavy-tailed-Data-in-Finance

Discovery for the Heavy_tailed Data in Finance

10/08-10/15:

1. Collected the 20-year daily, weekly, monthly prices for 5 stocks
2. Updated the statistical output for the new data
3. Virtualized the 20-year daily, weekly, monthly data using histograms and time series using Plotly
4. Collected the big intraday data per minute and per second (didn't upload the data to Github because they are too big) Upload the data readme.txt in /data/intraday_data/
5. Compare the daily mean, median, log_return_mean, log_return_median, mean_median, log_return_mean_median for IBM_adjusted which shows
IBM (International Business Machines) Regular session data per minute from Jan 1998


10/16-10/22:

1. Virtualized all of the big intraday data samples and generated histograms and boxplots using matplotlib.
2. Update Statistical_Exploratory.py and Vitualization.py
3. Compared the daily mean, median, log_return_mean, log_return_median, mean_median, log_return_mean_median for all the intraday data I have.
4. Compared the daily mean, median, log_return_mean, log_return_median, mean_median, log_return_mean_median in different periods like every three days and every five days for all the intraday data I have.


10/23-10/29:

1. Update all the codes
2. Virtualized the log returns for all the data I collected and plot histograms for each dataset
3. Research the Weiszfeld algorithm for computing the geometric median and implement the Weiszfeld algorithm in python
4. Applied this estimator to get a simultaneous 5-dimensional estimate of the log returns for the 5 stocks you are tracking. Compared this with the mean estimators. 

10/30-11/5:

1. Updated the virtualizations for the histograms of log returns. Added mean lines and median lines.
2. Code the Subgradient for the cost function in Weiszfeld algorithm. Use backtracking to compute the geometric median.
3. Virtualized the geometric median generated from the weiszfeld algorithm and the subgradient. Also, made comparision for mean estimator and geometric median estimator
4. Compare the mean-of-medians estimator in different scales and made virtualizations.




