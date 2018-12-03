# Heavy-tailed-Data-in-Finance

Discovery for the Heavy_tailed Data in Finance

10/08-10/15:

1. Collected the 20-year daily, weekly, monthly prices for 5 stocks
2. Updated the statistical output for the new data
3. Visualized the 20-year daily, weekly, monthly data using histograms and time series using Plotly
4. Collected the big intraday data per minute and per second (didn't upload the data to Github because they are too big) Upload the data readme.txt in /data/intraday_data/
5. Compare the daily mean, median, log_return_mean, log_return_median, mean_median, log_return_mean_median for IBM_adjusted which shows
IBM (International Business Machines) Regular session data per minute from Jan 1998


10/16-10/22:

1. Visualized all of the big intraday data samples and generated histograms and boxplots using matplotlib.
2. Update Statistical_Exploratory.py and Vitualization.py
3. Compared the daily mean, median, log_return_mean, log_return_median, mean_median, log_return_mean_median for all the intraday data I have.
4. Compared the daily mean, median, log_return_mean, log_return_median, mean_median, log_return_mean_median in different periods like every three days and every five days for all the intraday data I have.


10/23-10/29:

1. Update all the codes
2. Visualized the log returns for all the data I collected and plot histograms for each dataset
3. Research the Weiszfeld algorithm for computing the geometric median and implement the Weiszfeld algorithm in python
4. Applied this estimator to get a simultaneous 5-dimensional estimate of the log returns for the 5 stocks you are tracking. Compared this with the mean estimators. 

10/30-11/5:

1. Updated the visualizations for the histograms of log returns. Added mean lines and median lines.
2. Code the Subgradient for the cost function in Weiszfeld algorithm. Use backtracking to compute the geometric median.
3. Visualized the geometric median generated from the weiszfeld algorithm and the subgradient. Also, made comparision for mean estimator and geometric median estimator
4. Compare the mean-of-medians estimator in different scales and made virtualizations.


11/6 - 11/12:
1. Modified the codes for computing the geometric median, including applying the weiszfeld algorithm as well as the subgradient decent.
2. Uploaded the geometric median for 5 stocks for each year.
3. Modified the visualizations according to the geometric median and median-of-means

11/13 - 11/19:
1. Coutinued to update the code and visualizations.
2. Made data samples of size 2^19, 2^21, 2^22, 2^25 from my big intraday data. Plot the median error against log_N^k for the median-of-means estimators. N is the sample size and k shows that we seperate the data into how many parts when we compute the median-of-means.
3. I am exploring the difference between almost equally seperate the data and randomly seperate the data when we compute the median-of-means.

11/21 - 11/26:
1. Work on the convergence of the geometric median. Created a file named the geometric_median_convergence.txt including the trace of the points for each year when computing the geomatrix median. 

The results are that for Weiszfeld algorithm, they did converge for each year. But for subgradient decent, we need a suitable learning rate to make it converge for log returns of each day.

2. Plot the geometric median for the 5 stocks for each month compared to mean and median. There are 240 months in total. 
3. For the plot median error against log_N^k I made this week, I splited data randomly when I compute the median-of-means and replicate 10 times for each scale. For that plot lask week, I splited data equally.

11/27-12/3:

1. Checked the error for computing the geometric median. The geometric median of the rotated data is not the same as that of the original data
2. Debuged the code and recompute the geometric median for the 5 stocks. Visualized them yearly and monthly.
3. Modified the plot of computing the median error for different sample size and different number of partitions. Make permutations for each step.


