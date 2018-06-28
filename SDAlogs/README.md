# SSDAlogs
process the SDA logs

readSDAlogs.py:  reads the SDA log file  
- pulls out the ip address for SSDA and IT office workstations  - check to see if current since move  
- reformat the datetime to drop the date  
- toss out the ip addresses for privacy  
- output a CSV file,  named  syslog_test_  + date + .csv


readCSVfile.py  
- reads the csv file from readSDAlogs.py
