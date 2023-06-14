import pandas as pd
import csv
from datetime import datetime,timedelta
from cal_setup import get_calendar_service
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
 
 
# To store number of days in all months from
# January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 
# This function counts number of leap years
# before the given date
 
 
def countLeapYears(d):
 
    years = d.y
 
    # Check if the current year needs to be considered
    # for the count of leap years or not
    if (d.m <= 2):
        years -= 1
 
    # An year is a leap year if it is a multiple of 4,
    # multiple of 400 and not a multiple of 100.
    return int(years / 4) - int(years / 100) + int(years / 400)
 
 
# This function returns number of days between two
# given dates
def getDifference(dt1, dt2):
 
    # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'
 
    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d
 
    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
 
    # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += countLeapYears(dt1)
 
    # SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'
 
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
 
    # return difference between two counts
    return (n2 - n1)
 
 
# Driver program

 

'''function to check remaining days '''
def timeRemainingUpdate(yr_now,month_now,day_now,n):
    for i in range(1,n):
        maturity_date=fd_rows[i][3]
        dom=list(maturity_date)
        d=int(dom[0])*10 +int(dom[1])
        m=int(dom[3])*10+int(dom[4])
        y=int(dom[6])*1000+int(dom[7])*100+int(dom[8])*10+int(dom[9])
        #print(d,m,y)
        
      
        df.loc[i-1,'time remaining (days)']=  getDifference(Date(day_now,month_now,yr_now),Date(d,m,y))


'''function definition for urgent FDs'''
def urgentAttentionFDs(yr_now,month_now,day_now,n):





    for j in range(1,n):
        maturity_date=fd_rows[j][3]
        dom=list(maturity_date)
        d=int(dom[0])*10 +int(dom[1])
        m=int(dom[3])*10+int(dom[4])
        y=int(dom[6])*1000+int(dom[7])*100+int(dom[8])*10+int(dom[9])
        if(  getDifference(Date(day_now,month_now,yr_now),Date(d,m,y))<=7):
            print("The FD at bank ",fd_rows[j][0]," with FD number ",fd_rows[j][1]," is going to complete in ",getDifference(Date(day_now,month_now,yr_now),Date(d,m,y))," days")

def updateToGoogleCalendar():
    for j in range(1,n):
        maturity_date=fd_rows[j][3]
        dom=list(maturity_date)
        d2=dom[0]+dom[1]
        m2=dom[3]+dom[4]
        y2=dom[6]+dom[7]+dom[8]+dom[9]
        start=y2+"-"+m2+"-"+d2
        end=y2+"-"+m2+"-"+d2
        summary1="The FD at bank "+fd_rows[j][0]+" with FD number "+fd_rows[j][1]+" is going to complete"
        
        event_result = service.events().insert(calendarId='primary',
        body={
           "summary":'FD completion ' ,
           "description": summary1,
           "start": {"date": start, "timeZone": 'Asia/Kolkata'},
           "end": {"date": end, "timeZone": 'Asia/Kolkata'},
        }
        ).execute()


path='/home/shreesha/FD-Reminders/Codes/FD.csv'
df = pd.read_csv(path)
#print(df)
with open(path) as fd_csv:
    fd_reader = csv.reader(fd_csv)
    fd_rows = list(fd_reader)
n=len(fd_rows)

#print(datetime.now())
current_time=datetime.now()
years=int(current_time.year)
days=int(current_time.strftime("%d"))
months=int(current_time.strftime("%m"))
print()
#updating time remaining into csv file for all data at once
timeRemainingUpdate(years,months,days,n)
print()


urgentAttentionFDs(years,months,days,n)
print()

'''update to google calendar'''
service=get_calendar_service()

updateToGoogleCalendar()


df.to_csv(path,index=False)
print()
print(df)

                
   
