# readlinesPrintlines.py
# read in and print out
# useage from c: prompt: python readlinesPrintlines.py [filename].[extension]
import sys, re, fileinput, time
from datetime import date
from datetime import datetime 
#filename  = "%s" % sys.argv[1]
#filename = "log_20160509.txt"
filename = "sdalog.txt"

print("filename = %s\n\n\n" % (filename))

infile = open(filename, 'r')
#infileLines = list(open(filename))
outfile = open('syslog_test_' + str(date.today()) + '.csv', 'w')
outfile.write('UI,date-accessed time-accessed,dataset-accessed,programs-used\n') # add header
#print "Total lines this file: ",len(lines)

pattern = "169.232.181.10."# m = re.search('(?<=abc)def', 'abcdef')

lines = infile.readlines()
#for line in lines:

index_key = 0

for index, line in enumerate(lines):
    
                # pull out the ip address for SSDA workstations and IT office workstations
        if re.match("^169.232.181.10.|127.0.0.1|169.232.10.|164.67.152.153|164.67.152.15.",line): 
            #print(line)
            continue
        else:
            print(line)
            print(line.split( ))
            line = line.split( )
            print(line[1])
            # reformat the date to datetime format and then drop the time part
            logdate = datetime.strptime(line[1],'%d/%b/%Y:%H:%M:%S')
            logdate = datetime.strftime(logdate, '%Y-%b-%d')
            line[1] = str(logdate)
            # toss out the ip address for privacy
            del line[0]
            #print(line)
            line = str(index_key) + "," + ",".join(line) + "\n"
            print(line)
            outfile.write(line)
            index_key = index_key+1
                
        #print(line)
        #outfile.write(line)
        #if not line: break
        
infile.close()
outfile.close()


print("outfile = %s\n\n\n" % (outfile))
