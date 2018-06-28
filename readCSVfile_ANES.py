# readlinesPrintlines.py
# read in and print out
# useage from c: prompt: python readlinesPrintlines.py [filename].[extension]
import sys, re, fileinput, time
from datetime import date
import datetime as dt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import matplotlib.dates as mdates
import random


#filename  = "%s" % sys.argv[1]
filename = "syslog_test_anes2_2016-12-07.csv"

print("filename = %s\n\n\n" % (filename))

infile = open(filename, 'r')
#infileLines = list(open(filename))
outfile = open('report_test_anes2' + str(date.today()) + '.txt', 'wt')
#df = pd.read_csv('syslog_test_2016-05-20.csv', header=None, names=['UI','date-accessed', 'dataset-accessed', 'programs-used'], index_col=['UI'])

df = pd.DataFrame(pd.read_csv(filename, header=1, names=['UI','date-accessed', 'dataset-accessed', 'programs-used'], index_col=['UI']))
#print (str("\nEntire frame\n"))
#print(df)

df['date-accessed'] = pd.to_datetime(df['date-accessed'])

dateList = df['date-accessed'].tolist()

x=dateList
y = [i+random.gauss(0,1) for i,_ in enumerate(x)]
plt.plot(x,y)

plt.title(r'Usage of ANES2 recode dataset: Sept-Dec 2016')
plt.grid(True)
plt.xlabel('dates')
plt.ylabel('y-axis')
# beautify the x-labels
plt.gcf().autofmt_xdate()
#plt.show()

plt.title(r'Usage of ANES2 recode dataset: Sept-Dec 2016')
plt.grid(True)
plt.xlabel('dates')
plt.ylabel('y-axis')
plt.gcf().autofmt_xdate()
plt.hist(data[dateList], rwidth=0.75)

aggrigateDatasets = (df.groupby(['dataset-accessed','programs-used']).count())
print (str("\nAggrigate data\n"))
print(aggrigateDatasets)
outfile.write(str("\nAggrigate data\n"))
outfile.write(str(aggrigateDatasets))

print (str("\nDatasets Accessed\n"))
outfile.write(str("\nDatasets Accessed\n"))
aggrigateDatasets = (df.groupby(['dataset-accessed','date-accessed']).count())
print(aggrigateDatasets)
outfile.write(str(aggrigateDatasets))


print (str("\nDatasets Accessed\n"))
outfile.write(str("\nDatasets Accessed\n"))
aggrigateDatasets = (df.groupby(['date-accessed','dataset-accessed']).count())
print(aggrigateDatasets)
outfile.write(str(aggrigateDatasets))

#aggrigateDatasets = (df.groupby(['dataset-accessed']).count())
aggrigateDates = ((df.groupby(['date-accessed']).count()))
print(aggrigateDates)


print (str("\nDate List\n"))
#print(df.drop_duplicates(["date-accessed"]))
dates = df.drop_duplicates(["date-accessed"])
print("dates\n")
print(dates)

infile.close()
outfile.close()

print("outfile = %s\n\n\n" % (outfile))
