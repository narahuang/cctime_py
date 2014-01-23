import datetime,time
# This script calculates the number of AP recovered from now to 23:00 CST
# Nara Huang
#now = int(time.strftime("%H"))*60 + int(time.strftime("%M"))
#cct = 1380 - now
#print cct/8

print ( 1380 - (int(time.strftime("%H"))*60 + int(time.strftime("%M"))) )/8
