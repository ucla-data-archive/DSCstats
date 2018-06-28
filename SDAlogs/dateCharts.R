# notes to create charts with dates
getwd()
setwd("/media/jamie/7EDC14F5DC14A983/r-data/dateCharts/")

library(readr)
library(ggplot2)
install.packages("lubridate")
library(lubridate)



sdaData <- read_csv("syslog_test_2016-05-19.csv", 
                                   col_types = cols(`04/Apr/2016:14:45:12` = col_character()))
View(sdaData)

# STRucture
str(sdaData)

# column names
names(sdaData)

#summary stats
summary(sdaData)

# rename the date column - colnuames function
colnames(sdaData) <- c("Dates", "Study", "SDA Function")

View(sdaData)

base <- ggplot(sdaData, aes(Study, Dates)) + geom_line()
base

# first column as a data.frame
sdaData[1]

# first column as a vector
sdaData[,1]

Study <- factor(c(sdaData$Study))
"SDA Function" <- factor(c(sdaStudy$"SDA Function"))
Study

sdaData$Study

plot(Study)

levels(Studies)
nlevels(Studies)


SDAsyslog<- read.csv("/media/jamie/7EDC14F5DC14A983/r-data/sdaLogSample/syslog_test_2018-06-27.csv")
View(SDAsyslog)

#df = ssda.DataFrame(pd.read_csv(filename, header=1, names=['UI','date-accessed', 'dataset-accessed', 'programs-used'], index_col=['UI']))

#df['date-accessed'] = pd.to_datetime(df['date-accessed'])

#dateList = df['date-accessed'].tolist()

#x=dateList
#y = [i+random.gauss(0,1) for i,_ in enumerate(x)]
#plt.plot(x,y)
# beautify the x-labels
#plt.gcf().autofmt_xdate()
#plt.show()
