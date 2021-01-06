
import uuid
import pymysql
import logging
import databasefile
import uuid
import json
from pyfcm import FCMNotification
import collections

from datetime import timedelta,date,datetime
import time

import calendar
import pytz 
import stripe
#import datetime


class dyy(dict):
    def __str__(self):
        return json.dumps(self)
    def __repr__(self):
        return json.dumps(self)

class m(dict):
    def __str__(self):
        return json.dumps(self)
    def __repr__(self):
        return json.dumps(self)

d33={"start_time":"09:00","end_time":"5:00"}

a = datetime.strptime(d33['start_time'], "%H:%M")


kk=[]

kk.append(d33['start_time'])
b=a+timedelta(minutes=30)
c=b.strftime("%H:%M")
kk.append(c)
d=a+timedelta(minutes=30 *2 )
e=d.strftime("%H:%M")
kk.append(e)
f=a+timedelta(minutes=30*3)
g=f.strftime("%H:%M")
kk.append(g)
h=a+timedelta(minutes=120)
i=h.strftime("%H:%M")
kk.append(i)
j=a+timedelta(minutes=150)
k=j.strftime("%H:%M")
kk.append(k)
l=a+timedelta(minutes=180)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=210)
m=l.strftime("%H:%M")
l=a+timedelta(minutes=240)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=270)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=300)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=330)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=360)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=390)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=420)
m=l.strftime("%H:%M")
kk.append(m)
l=a+timedelta(minutes=450)
m=l.strftime("%H:%M")
kk.append(m)


print(kk,"sss")




def AddDaysInCurrentDate(noofdays):
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(tz=ist)
    ist_time = ist_time + timedelta(days=noofdays)
    ist_f_time = str(ist_time.strftime("%Y-%m-%d"))

    return ist_f_time


def CurrentDatetime():
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(tz=ist)
    ist_f_time = str(ist_time.strftime("%Y-%m-%d"))

    return ist_f_time


import calendar
import pytz 

def dayslist(startDate,endDate,customholidays,weekholidays):
    timeslot=["9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30","5:00"]
    serviceoption={"serviceoption":[{"serviceName":"abc","time":"30"},{"serviceName":"abcd","time":"30"},{"serviceName":"abcde","time":"15"}],"userId":"1234prashant"}
    date_format = "%Y-%m-%d"
    a = datetime.strptime(startDate, date_format)
    b = datetime.strptime(endDate, date_format)
    



   # end date

    delta = b-a
    

    c=[]   
    day_name= ['1', '2', '3', '4', '5', '6','7']
    # as timedelta
    k=[]

    l=[]

    for i in range(delta.days + 1):
        
        day = a + timedelta(days=i)
       
        d=day.strftime('%Y-%m-%d')
       
       
        kkk=calendar.day_name[day.weekday()] 
        k.append(kkk)
        

        
        l.append({"date":d,'day':kkk})
    for i in l:
        mmie={"timeslot":timeslot}

        date=i['date']
        day=i['day']
        for n in weekholidays:
            if n == day:
                l.remove(i)
        for kn in customholidays:
            
            if kn == date:
               
                l.remove(i)
        del i['day']

        print(type(i))
    for i in l:
        if 'day' not in i:
            i.update({"day":''})
        del i['day']
        i.update(mmie)
    result={"result":l}
    print(type(result))
    result.update(serviceoption)
   
    return result
f=dayslist('2020-08-15','2020-08-21',['2020-08-15','2020-08-16'],['1'])







# def finaldata(y13,t):
#     y11=y13
#     yr=t

#     for i in y11:
#         date=i['date']
#         time=i['timeslot']
#         for k in yr:
#             dates=k['date']
#             timestart=k['timestart']
#             totaltime=int(k['totaltime'])
            
#             if date == dates:
#                 if totaltime == 30:
#                     if timestart in time:
                    
#                         if timestart == '9:00':
#                             y="9:00"
                           
#                             time.remove(y)
                            
#                         elif timestart == '9:30':
#                             y="9:30"
                            
#                             time.remove(y)
                            
#                         elif timestart == '10:00':
                          
#                             j="10:00"
                            
#                             time.remove(j)
#                         elif timestart == '10:30':
#                             y="10:30"
                            
#                             time.remove(y)
                           
#                         elif timestart == '11:00':
                            
#                             j="11:00"
                           
#                             time.remove(j)
#                         elif timestart == '11:30':
#                             y="11:30"
                           
#                             time.remove(y)
                            
#                         elif timestart == '12:00':
#                             y="12:00"
                            
#                             time.remove(y)
                           
#                         elif timestart == '12:30':
                            
#                             time.remove('12:30')
                            
#                         elif timestart == '1:00':
                            
#                             j="1:00"
                            
#                             time.remove(j)
#                         elif timestart == '1:30':
#                             y="1:30"
                           
#                             time.remove(y)
                           
#                         elif timestart == '2:00':
                           
#                             j="2:00"
                            
#                             time.remove(j)
#                         elif timestart == '2:30':
#                             y="2:30"
                          
#                             time.remove(y)
                            
#                         elif timestart == '3:00':
                           
#                             j="3:00"
                            
#                             time.remove(j)
#                         elif timestart == '3:30':
#                             y="3:30"
                            
#                             time.remove(y)
                           
#                         elif timestart == '4:00':
#                             y="4:00"
                           
#                             time.remove(y)
#                         elif timestart == '4:30':
#                             y="4:30"
                           
#                             time.remove(y)
                            
#                         else:
#                             j="4:30"
#                             time.remove(j)
                


#                 else:
#                     if timestart in time:
#                         if timestart == '9:00':
#                             y="9:00"
#                             j="9:30"
                           
#                             time.remove(y)
#                             time.remove(j)
                           
#                         elif timestart == '10:00':
#                             y="10:30"
#                             j="10:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '11:00':
#                             y="11:30"
#                             j="11:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '12:00':
#                             y="12:30"
#                             j="12:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '1:00':
#                             y="1:30"
#                             j="1:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '2:00':
#                             y="2:00"
#                             j="2:30"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '3:00':
#                             y="3:00"
#                             j="3:30"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '4:00':
#                             y="4:30"
#                             j="4:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '9:30':
#                             y="9:30"
#                             j="10:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '10:30':
#                             y="10:30"
#                             j="11:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '11:30':
#                             y="11:30"
#                             j="12:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '12:30':
#                             y="12:30"
#                             j="1:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '1:30':
#                             y="1:30"
#                             j="2:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '2:30':
#                             y="2:30"
#                             j="3:00"
#                             time.remove(y)
#                             time.remove(j)
#                         elif timestart == '3:30':
#                             y="3:30"
#                             j="4:00"
#                             time.remove(y)
#                             time.remove(j)
#                         else:
#                             j="5:00"
#                             time.remove(j)
#     u={'result':y13}
#     u.update({"serviceoption":[{"serviceName":"abc","time":"30"},{"serviceName":"abcd","time":"30"}],"userId":"1234prashant"})
#     return json.dumps(u)



def finaldata1(y13,t,time):
    y11=y13
    yr=t
    ts=time
    for kkbs in y11:
        kkbs.update({"timeslot":ts})

    for i in y11:

        print(type(i))
        date=i['date']
        time=i['timeslot']
        for k in yr:
            dates=k['date']
            timestart=k['timestart']
            totaltime=int(k['totaltime'])
            a = datetime.strptime(timestart, "%H:%M")
            d=a.strftime("%H:%M")
            if date == dates:
                if totaltime == 30:
                    if timestart in time:
                        time.remove(d)
                else:
                    if totaltime ==60:
                        if timestart in time:
                            time.remove(d)
                            c=a+timedelta(minutes=30)
                            c=c.strftime("%H:%M")
                            time.remove(c)
                    elif  totaltime == 15:
                        a=timestart
                        if timestart == "9:30" or timestart == "09:30":
                            time=["09:00"]
                        elif timestart == "9:15" or timestart == "09:15":
                            time=[ ]
                        if timestart == "9:00" or timestart == "09:00":
                            time=[]
                        elif timestart == "09:45" or timestart == "9:45":
                            time=["09:00","09:30"]
                        elif timestart == "10:00" or timestart == "10:00":
                            time=["09:00","09:30"]
                        elif timestart == "10:15":
                            time=["09:00","09:30","10:00"]
                        elif timestart == "10:30":
                            time=["09:00","09:30","10:00"]
                        elif timestart == "10:45":
                            time=["09:00","09:30","10:00","10:30"]
                        elif timestart == "11:00":
                            time=["09:00","09:30","10:00","10:30"]
                        elif timestart == "11:15":
                            time=["09:00","09:30","10:00","10:30","11:00"]
                        elif timestart == "11:30":
                            time=["09:00","09:30","10:00","10:30","11:00"]
                        elif timestart == "11:45":
                            time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                        elif timestart == "12:00":
                            time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                        elif timestart == "12:15":
                            time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                        elif timestart == "12:30":
                            time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                        

                        
                        a = datetime.strptime(timestart, "%H:%M")
                        b=a+timedelta(minutes=15)
                        c=b.strftime("%H:%M")
                        time.append(c)
                        d=a+timedelta(minutes=45)
                        e=d.strftime("%H:%M")
                        time.append(e)
                        f=a+timedelta(minutes=75)
                        g=f.strftime("%H:%M")
                        time.append(g)
                        h=a+timedelta(minutes=105)
                        ii=h.strftime("%H:%M")
                        time.append(ii)
                        j=a+timedelta(minutes=135)
                        k=j.strftime("%H:%M")
                        time.append(k)
                        l=a+timedelta(minutes=165)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=195)
                        m=l.strftime("%H:%M")
                        l=a+timedelta(minutes=225)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=255)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=285)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=315)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=345)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=375)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=405)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=435)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        del i['timeslot']
                        i.update({"timeslot":time})
                    
                    elif  totaltime == 45:
                        a=timestart
                        time=[]
                        # if timestart == "9:30" or timestart == "09:30":
                        #     time=["09:00"]
                        # elif timestart == "9:15" or timestart == "09:15":
                        #     time=["09:00"]
                        # if timestart == "9:00" or timestart == "09:00":
                        #     time=[]
                        # elif timestart == "09:45" or timestart == "9:45":
                        #     time=["09:00","09:30","09:15"]
                        # elif timestart == "10:00" or timestart == "10:00":
                        #     time=["09:00","09:30"]
                        # elif timestart == "10:15":
                        #     time=["09:00","09:30","10:00"]
                        # elif timestart == "10:30":
                        #     time=["09:00","09:30","10:00"]
                        # elif timestart == "10:45":
                        #     time=["09:00","09:30","10:00","10:30"]
                        # elif timestart == "11:00":
                        #     time=["09:00","09:30","10:00","10:30"]
                        # elif timestart == "11:15":
                        #     time=["09:00","09:30","10:00","10:30","11:00"]
                        # elif timestart == "11:30":
                        #     time=["09:00","09:30","10:00","10:30","11:00"]
                        # elif timestart == "11:45":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                        # elif timestart == "12:00":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                        # elif timestart == "12:15":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                        # elif timestart == "12:30":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                        

                        
                        a = datetime.strptime(timestart, "%H:%M")
                        d=a+timedelta(minutes=45)
                        e=d.strftime("%H:%M")
                        time.append(e)
                        f=a+timedelta(minutes=75)
                        g=f.strftime("%H:%M")
                        time.append(g)
                        h=a+timedelta(minutes=105)
                        ii=h.strftime("%H:%M")
                        time.append(ii)
                        j=a+timedelta(minutes=135)
                        k=j.strftime("%H:%M")
                        time.append(k)
                        l=a+timedelta(minutes=165)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=195)
                        m=l.strftime("%H:%M")
                        l=a+timedelta(minutes=225)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=255)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=285)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=315)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=345)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=375)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=405)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=435)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        del i['timeslot']
                        i.update({"timeslot":time})
                    else:
                       
                        a=timestart
                        time=[]
                        # if timestart == "9:30" or timestart == "09:30":
                        #     time=["09:00"]
                        # elif timestart == "9:15" or timestart == "09:15":
                        #     time=["09:00"]
                        # if timestart == "9:00" or timestart == "09:00":
                        #     time=[]
                        # elif timestart == "09:45" or timestart == "9:45":
                        #     time=["09:00","09:30","09:15"]
                        # elif timestart == "10:00" or timestart == "10:00":
                        #     time=["09:00","09:30"]
                        # elif timestart == "10:15":
                        #     time=["09:00","09:30","10:00"]
                        # elif timestart == "10:30":
                        #     time=["09:00","09:30","10:00"]
                        # elif timestart == "10:45":
                        #     time=["09:00","09:30","10:00","10:30"]
                        # elif timestart == "11:00":
                        #     time=["09:00","09:30","10:00","10:30"]
                        # elif timestart == "11:15":
                        #     time=["09:00","09:30","10:00","10:30","11:00"]
                        # elif timestart == "11:30":
                        #     time=["09:00","09:30","10:00","10:30","11:00"]
                        # elif timestart == "11:45":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                        # elif timestart == "12:00":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                        # elif timestart == "12:15":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                        # elif timestart == "12:30":
                        #     time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                        

                        
                        a = datetime.strptime(timestart, "%H:%M")
                        f=a+timedelta(minutes=75)
                        g=f.strftime("%H:%M")
                        time.append(g)
                        h=a+timedelta(minutes=105)
                        ii=h.strftime("%H:%M")
                        time.append(ii)
                        j=a+timedelta(minutes=135)
                        k=j.strftime("%H:%M")
                        time.append(k)
                        l=a+timedelta(minutes=165)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=195)
                        m=l.strftime("%H:%M")
                        l=a+timedelta(minutes=225)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=255)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=285)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=315)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=345)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=375)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=405)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        l=a+timedelta(minutes=435)
                        m=l.strftime("%H:%M")
                        time.append(m)
                        del i['timeslot']
                        i.update({"timeslot":time})




                        



                        
    u={'result':y13}
    u.update({"serviceoption":[{"serviceName":"abc","time":"30"},{"serviceName":"abcd","time":"30"},{"serviceName":"abced","time":"15"}],"userId":"1234prashant"})
    return json.dumps(u)



def finaldata12(y13,t,time):
    y11=y13
    yr=t
    ts=time
    for kkbs in y11:
        kkbs.update({"timeslot":ts})

    for i in y11:

        print(type(i))
        date=i['date']
        time=i['timeslot']
        for k in yr:
            dates=k['date']
            timestart=k['timestart']
            totaltime=int(k['totaltime'])
            if 'counter' not in k:
                k.update({"counter":"0"})
            counter=int(k['counter'])
            if counter == 0:
                a=timestart
                time=[]
                if timestart == "9:30" or timestart == "09:30":

                    time.extend("09:15",4)
                    time.extend("09:00",4)
                elif timestart == "9:15" or timestart == "09:15":
                    time.extend("09:00",4)
                if timestart == "9:00" or timestart == "09:00":
                    time=[]
                elif timestart == "09:45" or timestart == "9:45":
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                elif timestart == "10:00" or timestart == "10:00": 
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                    time.extend("09:45",4)
                elif timestart == "10:15":
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                    time.extend("09:45",4)
                    time.extend("10:00",4)
                elif timestart == "10:30":
                    time=["09:00","09:30","10:00"]
                elif timestart == "10:45":
                    time=["09:00","09:30","10:00","10:30"]
                elif timestart == "11:00":
                    time=["09:00","09:30","10:00","10:30"]
                elif timestart == "11:15":
                    time=["09:00","09:30","10:00","10:30","11:00"]
                elif timestart == "11:30":
                    time=["09:00","09:30","10:00","10:30","11:00"]
                elif timestart == "11:45":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                elif timestart == "12:00":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                elif timestart == "12:15":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                elif timestart == "12:30":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                

                
                a = datetime.strptime(timestart, "%H:%M")
                b=a+timedelta(minutes=15)
                c=b.strftime("%H:%M")
                time.extend(c,4)
                d=a+timedelta(minutes=45)
                e=d.strftime("%H:%M")
                time.extend(e,4)
                f=a+timedelta(minutes=75)
                g=f.strftime("%H:%M")
                time.extend(g,4)
                h=a+timedelta(minutes=105)
                ii=h.strftime("%H:%M")
                time.extend(ii,4)
                j=a+timedelta(minutes=135)
                k=j.strftime("%H:%M")
                time.extend(k,4)
                l=a+timedelta(minutes=165)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=195)
                m=l.strftime("%H:%M")
                l=a+timedelta(minutes=225)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=255)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=285)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=315)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=345)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=375)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=405)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                l=a+timedelta(minutes=435)
                m=l.strftime("%H:%M")
                time.extend(m,4)
                del i['timeslot']
                i.update({"timeslot":time})


            if counter == 1:
                a=timestart
                time=[]
                if timestart == "9:30" or timestart == "09:30":

                    time.extend("09:15",4)
                    time.extend("09:00",4)
                elif timestart == "9:15" or timestart == "09:15":
                    time.extend("09:00",4)
                if timestart == "9:00" or timestart == "09:00":
                    time=[]
                elif timestart == "09:45" or timestart == "9:45":
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                elif timestart == "10:00" or timestart == "10:00": 
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                    time.extend("09:45",4)
                elif timestart == "10:15":
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                    time.extend("09:45",4)
                    time.extend("10:00",4)
                elif timestart == "10:30":
                    time=["09:00","09:30","10:00"]
                elif timestart == "10:45":
                    time=["09:00","09:30","10:00","10:30"]
                elif timestart == "11:00":
                    time=["09:00","09:30","10:00","10:30"]
                elif timestart == "11:15":
                    time=["09:00","09:30","10:00","10:30","11:00"]
                elif timestart == "11:30":
                    time=["09:00","09:30","10:00","10:30","11:00"]
                elif timestart == "11:45":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                elif timestart == "12:00":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                elif timestart == "12:15":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                elif timestart == "12:30":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                

                
                a = datetime.strptime(timestart, "%H:%M")
                b=a+timedelta(minutes=15)
                c=b.strftime("%H:%M")
                time.extend(c,3)
                d=a+timedelta(minutes=45)
                e=d.strftime("%H:%M")
                time.extend(e,3)
                f=a+timedelta(minutes=75)
                g=f.strftime("%H:%M")
                time.extend(g,3)
                h=a+timedelta(minutes=105)
                ii=h.strftime("%H:%M")
                time.extend(ii,3)
                j=a+timedelta(minutes=135)
                k=j.strftime("%H:%M")
                time.extend(k,3)
                l=a+timedelta(minutes=165)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=195)
                m=l.strftime("%H:%M")
                l=a+timedelta(minutes=225)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=255)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=285)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=315)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=345)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=375)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=405)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                l=a+timedelta(minutes=435)
                m=l.strftime("%H:%M")
                time.extend(m,3)
                del i['timeslot']
                i.update({"timeslot":time})


            elif counter ==2:
                a=timestart
                time=[]
                if timestart == "9:30" or timestart == "09:30":

                    time.extend("09:15",4)
                    time.extend("09:00",4)
                elif timestart == "9:15" or timestart == "09:15":
                    time.extend("09:00",4)
                if timestart == "9:00" or timestart == "09:00":
                    time=[]
                elif timestart == "09:45" or timestart == "9:45":
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                elif timestart == "10:00" or timestart == "10:00": 
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                    time.extend("09:45",4)
                elif timestart == "10:15":
                    time.extend("09:15",4)
                    time.extend("09:30",4)
                    time.extend("09:00",4)
                    time.extend("09:45",4)
                    time.extend("10:00",4)
                elif timestart == "10:30":
                    time=["09:00","09:30","10:00"]
                elif timestart == "10:45":
                    time=["09:00","09:30","10:00","10:30"]
                elif timestart == "11:00":
                    time=["09:00","09:30","10:00","10:30"]
                elif timestart == "11:15":
                    time=["09:00","09:30","10:00","10:30","11:00"]
                elif timestart == "11:30":
                    time=["09:00","09:30","10:00","10:30","11:00"]
                elif timestart == "11:45":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                elif timestart == "12:00":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                elif timestart == "12:15":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                elif timestart == "12:30":
                    time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                

                
                a = datetime.strptime(timestart, "%H:%M")
                b=a+timedelta(minutes=15)
                c=b.strftime("%H:%M")
                time.extend(c,2)
                d=a+timedelta(minutes=45)
                e=d.strftime("%H:%M")
                time.extend(e,2)
                f=a+timedelta(minutes=75)
                g=f.strftime("%H:%M")
                time.extend(g,2)
                h=a+timedelta(minutes=105)
                ii=h.strftime("%H:%M")
                time.extend(ii,2)
                j=a+timedelta(minutes=135)
                k=j.strftime("%H:%M")
                time.extend(k,2)
                l=a+timedelta(minutes=165)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=195)
                m=l.strftime("%H:%M")
                l=a+timedelta(minutes=225)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=255)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=285)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=315)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=345)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=375)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=405)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                l=a+timedelta(minutes=435)
                m=l.strftime("%H:%M")
                time.extend(m,2)
                del i['timeslot']
                i.update({"timeslot":time})

            
            else:
                a = datetime.strptime(timestart, "%H:%M")
                d=a.strftime("%H:%M")
                if date == dates:
                  
                       
                        if  totaltime == 15:
                            a=timestart
                            time=[]
                            if timestart == "9:30" or timestart == "09:30":

                                time.extend("09:15",4)
                                time.extend("09:00",4)
                            elif timestart == "9:15" or timestart == "09:15":
                                time.extend("09:00",4)
                            if timestart == "9:00" or timestart == "09:00":
                                time=[]
                            elif timestart == "09:45" or timestart == "9:45":
                                time.extend("09:15",4)
                                time.extend("09:30",4)
                                time.extend("09:00",4)
                            elif timestart == "10:00" or timestart == "10:00": 
                                time.extend("09:15",4)
                                time.extend("09:30",4)
                                time.extend("09:00",4)
                                time.extend("09:45",4)
                            elif timestart == "10:15":
                                time.extend("09:15",4)
                                time.extend("09:30",4)
                                time.extend("09:00",4)
                                time.extend("09:45",4)
                                time.extend("10:00",4)
                            elif timestart == "10:30":
                                time=["09:00","09:30","10:00"]
                            elif timestart == "10:45":
                                time=["09:00","09:30","10:00","10:30"]
                            elif timestart == "11:00":
                                time=["09:00","09:30","10:00","10:30"]
                            elif timestart == "11:15":
                                time=["09:00","09:30","10:00","10:30","11:00"]
                            elif timestart == "11:30":
                                time=["09:00","09:30","10:00","10:30","11:00"]
                            elif timestart == "11:45":
                                time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                            elif timestart == "12:00":
                                time=["09:00","09:30","10:00","10:30","11:00","11:30"]
                            elif timestart == "12:15":
                                time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]
                            elif timestart == "12:30":
                                time=["09:00","09:30","10:00","10:30","11:00","11:30","12:00"]

                            

                            
                            a = datetime.strptime(timestart, "%H:%M")
                            b=a+timedelta(minutes=15)
                            c=b.strftime("%H:%M")
                            time.extend(c,1)
                            d=a+timedelta(minutes=45)
                            e=d.strftime("%H:%M")
                            time.extend(e,1)
                            f=a+timedelta(minutes=75)
                            g=f.strftime("%H:%M")
                            time.extend(g,1)
                            h=a+timedelta(minutes=105)
                            ii=h.strftime("%H:%M")
                            time.extend(ii,1)
                            j=a+timedelta(minutes=135)
                            k=j.strftime("%H:%M")
                            time.extend(k,1)
                            l=a+timedelta(minutes=165)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=195)
                            m=l.strftime("%H:%M")
                            l=a+timedelta(minutes=225)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=255)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=285)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=315)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=345)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=375)
                            m=l.strftime("%H:%M")
                            time.append(m)
                            l=a+timedelta(minutes=405)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            l=a+timedelta(minutes=435)
                            m=l.strftime("%H:%M")
                            time.extend(m,1)
                            del i['timeslot']
                            i.update({"timeslot":time})





                        



                        
    u={'result':y13}
    u.update({"serviceoption":[{"serviceName":"abc","time":"30"},{"serviceName":"abcd","time":"30"},{"serviceName":"abced","time":"15"}],"userId":"1234prashant"})
    return json.dumps(u)




logger = logging.getLogger()
logger.setLevel(logging.INFO)


import string 
import random 
  
# initializing size of string  
N = 70
  
# using random.choices() 
# generating random strings  
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N)) 
  
# print result 
print("The generated random string : " + str(res)) 







def DecodeInputdata(data):
    data = json.loads(data.decode("utf-8"))                 
    return data


def CreateHashKey(FirstKey,SecoundKey):
    # hash = hashlib.sha256()
    # hash.update(('%s%s' % (FirstKey,SecoundKey)).encode('utf-8'))
    Hashkey = uuid.uuid1()

    return Hashkey


def DecodeInputdata(data):
    data = json.loads(data.decode("utf-8"))                 
    return data









def lambda_handler(event, context):
    
    logger.info(event)
    logger.info(context)

    
    if event['path'] =="/userregistration":

        v1="1"
        if event['httpMethod'] == "POST":
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            name=i['name']
            print(name)
            phone=i['phone']
            email=i['email']
            password=i['password']
            typeName=i['typeName']
            spaceName=i['spaceName']
            confirmPassword=i['confirmPassword']
            print("ss")
            if confirmPassword == password:
                print("sse")

                UserId=CreateHashKey(name,email)
                spaceId=CreateHashKey(spaceName,name)
                flag="i"
                WhereCondition = "and name='"+str(name)+"' or email ='"+str(email)+"'"
                count = databasefile.SelectCountQuery("userMaster",WhereCondition,"")
                print(count)


                if int(count) > 0:
                    print("dd")
                    h={}
                    h['result']='User Already Exist with phone or email or name,Please rename all '
                    hpp=dyy(h)
                    return {'statusCode':200,'body':json.dumps(hpp),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        } }
                else:
                    if flag =="i":
                        print("11111111111111111111111")
                        column = "email,phone,password,usertypeId,userId,name,typeName,spaceName,spaceId"            
                        values = " '" + str(email) + "','" + str(phone) + "','" + str(password) + "','" + str('2')+ "','" + str(UserId)+ "','" + str(name) + "','" + str(typeName)+ "','" + str(spaceName)+ "','" + str(spaceId) + "' "
                        data = databasefile.InsertQuery("userMaster",column,values)       
                        if data != "0":

                            column = 'name,email,phone,password,usertypeId,userId,typeName,spaceName,spaceId'
                            data = databasefile.SelectQuery("userMaster",column,WhereCondition,"","","")
                            print(data)
                            p=[]
                            for i in data['result']:
                                g=dyy(i)
                                p.append(g)
                            h={}
                            h['result']=p
                            hpp=dyy(i)


                           
                            
                            

                            return { 'statusCode': 200, 'body':json.dumps(hpp),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
                        else:
                            return "qq"
            else:
                h={}
                h['result']='confirmPassword & password are not same'
                hpp=d(i)
                return { 'statusCode': 200, 'body':json.dumps(hpp),'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }}
    elif event['path'] =="/allspaces":

        v1="1"
        if event['httpMethod'] == "GET":
           
            

            column = 'name,email,phone,password,usertypeId,userId,typeName,spaceName,spaceId'
            data = databasefile.SelectQuery("userMaster",column,"","","","")
            print(data)
            p=[]
            for i in data['result']:
                i['category']='barber'
                i['spacelogo']="https://uplad-documents.s3.ap-south-1.amazonaws.com/shoppicture/defaultuser.jpg"
                g=dyy(i)
               
                p.append(g)
            h={}
            h['result']=p
            hpp=dyy(h)


           
            
            

            return { 'statusCode': 200, 'body':json.dumps(hpp),'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }}
                       
    
    elif event['path'] == "/userdata":
        print("www")
        if event['httpMethod'] == "POST":
            p=event['headers']['Authorization']
            print(event['headers']['Authorization'])
            pdn=p.split(" ")
            print(pdn[1])

           
            
           
            column="name"
            WhereCondition= "  and token = '" + str(pdn[1])+ "'"

            data = databasefile.SelectQuery("userMaster",column,WhereCondition,"","","")
            print(data)
            if data['status'] !='false':
                       
            
                p=[]
                
                
                asjj={}
                asjj['name']=data['result'][0]['name']
                print(asjj)
                    


               
                hpp=dyy(asjj)
                hp={}
                hp['result']=asjj
                hp=dyy(hp)
               

                

               
                
                

                return { 'statusCode': 200, 'body':json.dumps(hp),'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    }}
            else:
                h={}
                h['result']='Please enter correct credentials'
                return { 'statusCode': 401, 'body':json.dumps(h),'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    }}
    elif event['path'] == "/deleteappiontment":
        print("www")
        if event['httpMethod'] == "POST":
            p=event['headers']['Authorization']
            pdn=p.split(" ")
            print(pdn[1])
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(type(i))            
            print(i)
            spaceId=i['spaceId']

           
            
           
            column="spaceId"
            WhereCondition= "  and token = '" + str(pdn[1])+ "' and spaceId= '" + str(spaceId)+ "'" 

            data = databasefile.SelectQuery("userMaster",column,WhereCondition,"","","")
            print(data)
            if data['status'] !='false':
                appointmentName=i['appointmentName']
                column="Status='"+str(1)+"'"
                WhereCondition=" and spaceId='"+str(spaceId)+"'"
                j=databasefile.UpdateQuery("appiontmentmeetMaster",column,WhereCondition)
                if j['status'] !='false':

                


                   
                    
                    

                    return { 'statusCode': 200, 'body':u,'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
                else:
                    h={}
                    h['result']='Please Enter correct credentials'
                    return { 'statusCode': 401, 'body':json.dumps(h),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
                
            else:
                h={}
                h['result']='Please Enter correct credentials'
                return { 'statusCode': 401, 'body':json.dumps(h),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
    if event['path'] == "/userlogin":
        print("www")
        if event['httpMethod'] == "POST":
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            email=i['email']
            password=i['password']
            
           
            column="email,password,spaceId,userId"
            WhereCondition= "  and email = '" + str(email)+ "' and password='"+password+"'"
            data = databasefile.SelectQuery("userMaster",column,WhereCondition,"","","")
            print(data)
            if data['status'] !='false':
                h=[]
                for i in data['result']:
                    k=dyy(i)

                    stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

                    a=stripe.Token.create(
                      pii={"id_number": i['userId']},
                    )

                    asjj={}
                    asjj['token']=a['id'] +str(a['id'][::-1])+str(a['id'][::-6])+str(a['id'][::-1])+str(a['id'][::-5])+str(a['id'][::-2])+str(a['id'][::-3])+str(a['id'][::-4])
                    print(asjj)
                    asjj['spaceId']=i['spaceId']
                    WhereCondition= "  and email = '" + str(email)+ "' and password='"+password+"'"
                    column="token ='"+ str(asjj['token'])+"'"
                    data = databasefile.UpdateQuery("userMaster",column,WhereCondition)

               
                hpp=dyy(asjj)
                print({'statusCode':200,'body':hpp})
                return {'statusCode':200,'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },'body':json.dumps(hpp)}
            else:
                return {'statusCode':200,'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },'body':json.dumps({'result':'Wrong password and email ,Please Enter Correct Credentails','status':'false'})}

    elif event['path'] == "/myappiontments":
        print("www")
        if event['httpMethod'] == "POST":
            p=event['headers']['Authorization']
            pdn=p.split(" ")
            print(pdn[1])
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(type(i))            
            print(i)
            spaceId=i['spaceId']

           
            
           
            column="spaceId"
            WhereCondition= "  and token = '" + str(pdn[1])+ "' and spaceId= '" + str(spaceId)+ "'" 

            data = databasefile.SelectQuery("userMaster",column,WhereCondition,"","","")
            print(data)
            if data['status'] !='false':
                t=type(event['body'])
                print(event['body'])
                print(t)
                i=json.loads(event['body'])
                print(type(i))            
                print(i)
                spaceId=i['spaceId']
                column = 'distinct(appointmentName),spaceId,default_timeout'
                WhereCondition="and appointmentId='"+str(spaceId)+"' and status='"+str(0)+"'"
                data = databasefile.SelectQuery("appiontmentmeetMaster ",column,WhereCondition,"","","")
                
            
                print(data)
               
                            
                if data['result']!="":
                    print(data['result'],"sgsg")
                    



                  
                    for ien in data['result']:
                        
                        appiontmentName=ien['appointmentName']

                        SpaceId=ien['spaceId']
                        column="appointmentId,appiontmentName,start_time,end_time"
                        WhereCondition="and appointmentId='"+str(SpaceId)+"' and appiontmentName='"+str(appiontmentName)+"'"

                        
                        datainterval=  databasefile.SelectQuery("appiontmentintervalMaster",column,WhereCondition,"","","")
                        hj=[]
                        print(datainterval['result'],"sd")
                        for y in datainterval['result']:
                            hj.append(y)
                        ien.update({"interval":datainterval['result']})


                        column="appointmentId,appiontmentName,serviceName,time"
                        WhereCondition="and appointmentId='"+str(SpaceId)+"' and appiontmentName='"+str(appiontmentName)+"'"

                        
                        datai=  databasefile.SelectQuery("serviceoptionMaster",column,WhereCondition,"","","")
                        print(datai['result'],"sdd")
                        hjb=[]
                        for y in datai['result']:
                            hjb.append(hjb)
                        ien.update({"serviceoption":datai['result']})




                        
                        
                    u={}
                    u['result']=data['result']
                    u=json.dumps(u)


                   
                    
                    

                    return { 'statusCode': 200, 'body':u,'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
                else:
                    h={}
                    h['result']='Please add Appiontment ,there is no such appiontments'
                    return { 'statusCode': 200, 'body':json.dumps(h),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
            else:
                h={}
                h['result']='Please Enter correct credentials'
                return { 'statusCode': 401, 'body':json.dumps(h),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}

    elif event['path'] == "/dropdown":
        print("qwqw")
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            typeName=i['typeName']
           
            WhereCondition = " and name = '" + str(typeName) +"'"
            count = databasefile.SelectCountQuery("typeNameMaster",WhereCondition,"")
            if int(count) > 0:
                return {'statusCode':404}
            else:
                if flag =="i":
                    print("11111111111111111111111")
                    column = "typeName"                
                    values = " '" + str(typeName)  + "' "
                    data = databasefile.InsertQuery("typeNameMaster",column,values)       
                    if data != "0":

                        column = 'typeName'
                        data = databasefile.SelectQuery("typeNameMaster",column,WhereCondition,"","","")
                        print(data)
                        p=[]
                        for i in data['result']:
                            g=d(i)
                            p.append(g)
                        h={}
                        h['result']=p
                        hpp=d(i)


                       
                        
                        

                        return { 'statusCode': 200, 'body':json.dumps(hpp)}
                    else:
                        return "qq"
        else:
            column = 'typeName'
            data = databasefile.SelectQuery("typeNameMaster",column," ","","","")
            print(data)
            p=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            h={}
            h['result']=p
            hpp=d(i)


           

            
            

            return { 'statusCode': 200, 'body':json.dumps(hpp)}
    elif event['path'] =="/logo":
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            typeName=i['typeName']
            name=i['name']
            spaceName=i['spaceName']
           
            WhereCondition = " and spaceName = '" + str(spaceName) +"'"
            count = databasefile.SelectCountQuery("spaceMaster",WhereCondition,"")
            if int(count) > 0:
                return {'statusCode':404}
            else:
                if flag =="i":
                    print("11111111111111111111111")
                    column = "name,typeName,spaceName"      
                    values = " '" + str(name)+ "','" + str(typeName) + "','" + str(spaceName)   + "' "
                 
                    data = databasefile.InsertQuery("spaceMaster",column,values)       
                    if data != "0":

                        column = 'typeName,name,spaceName'
                        data = databasefile.SelectQuery("spaceMaster",column,WhereCondition,"","","")
                        print(data)
                        p=[]
                        for i in data['result']:
                            g=d(i)
                            p.append(g)
                        h={}
                        h['result']=p
                        hpp=d(i)


                       
                        
                        

                        return { 'statusCode': 200, 'body':json.dumps(hpp)}
                    else:
                        return "qq"
        else:
            column = 'typeName,name,spaceName'
            data = databasefile.SelectQuery("spaceMaster",column,WhereCondition,"","","")
            print(data)
            p=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            h={}
            h['result']=p
            hpp=d(i)


           
            
            

            return { 'statusCode': 200, 'body':json.dumps(hpp)}
    elif event['path'] == "/updatedefaultmeetMaster":
        t=type(event['body'])
        print(event['body'])
        print(t)
        i=json.loads(event['body'])
        print(i)
        print(type(i))
        time=i['time']
        typeNameId=i['typeNameId']
        userId=i['userId']
       
        column="time='" + time+ "'and typeNameId='" + typeNameId+ "'"
        whereCondition= "  and userId= '" + str(userId)+ "' "
        output=databasefile.UpdateQuery("defaultmeetMaster",column,whereCondition)
        if output!='0':
            t={}
            t['result']='updated Successfully'
            hpp=mm(t)
            return {'statusCode':200,'body':json.dumps(hpp)}
        else:
            return {'statusCode':200,'body':'Don"t Exist'}
   
    elif event['path'] =="/defaultmeetinf":
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            time=i['time']
            typeNameId=i['typeNameId']
            userId=i['userId']
           
            WhereCondition = " and userId = '" + str(userId) +"'"
            count = databasefile.SelectCountQuery("defaultmeetMaster",WhereCondition,"")
            if int(count) > 0:
                return {'statusCode':404}
            else:
                if flag =="i":
                    print("11111111111111111111111")
                    column = "time,typeNameId,userId"      
                    values = " '" + str(name)+ "','" + str(typeNameId) + "','" + str(userId)   + "' "
                 
                    data = databasefile.InsertQuery("defaultmeetMaster",column,values)       
                    if data != "0":

                        column = 'time,typeNameId,userId'
                        data = databasefile.SelectQuery("defaultmeetMaster",column,WhereCondition,"","","")
                        print(data)
                        p=[]

                        for i in data['result']:
                            g=d(i)
                            p.append(g)
                        h={}
                        h['result']=p
                        hpp=d(i)


                       
                        
                        

                        return { 'statusCode': 200, 'body':json.dumps(hpp)}
                    else:
                        return "qq"
        else:
            column =  'time,typeNameId,userId'
            data = databasefile.SelectQuery("defaultmeetMaster",column,WhereCondition,"","","")
            print(data)
            p=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            h={}
            h['result']=p
            hpp=d(i)


       
        
        

        return { 'statusCode': 200, 'body':json.dumps(hpp)}

    elif event['path'] == "/showintervalgolf":
        print("www")
        if event['httpMethod'] == "POST":
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            userId=i['userId']
            column = 'ba.date,ba.userId,ba.timestart,ba.totaltime,bagm.counter'
            WhereCondition=" and ba.bookingId=bagm.bookingId "
            data = databasefile.SelectQuery("bookappointment as ba ,bookappointmentGolfMapping as bagm",column,'',"","","")
            print(data)
            timeslot=kk
                        
            if data!='0':
                



                a=CurrentDatetime()
                b=AddDaysInCurrentDate(720)
                customholidays=['2020-08-15','2020-08-16']
                weekholidays=['1']
                
                serviceoption={"serviceoption":[{"serviceName":"abc","time":"30"},{"serviceName":"abcd","time":"30"},{"serviceName":"abcde","time":"15"}],"userId":"1234prashant"}
                
                date_format = "%Y-%m-%d"
                a = datetime.strptime(a, date_format)
                b = datetime.strptime(b, date_format)
                



               # end date

                delta = b-a
                

                c=[]   
                day_name= ['1', '2', '3', '4', '5', '6','7']
                # as timedelta
                k=[]

                l=[]

                for i in range(delta.days + 1):
                    
                    day = a + timedelta(days=i)
                   
                    d=day.strftime('%Y-%m-%d')
                    kkk=calendar.day_name[day.weekday()] 
                    k.append(kkk)
                    

                    
                    l.append({"date":d,'day':kkk})
                for i in l:
                    

                    date=i['date']
                    day=i['day']
                    for n in weekholidays:
                        if n == day:
                            l.remove(i)
                    for kn in customholidays:
                        
                        if kn == date:
                           
                            l.remove(i)
                    del i['day']

                    print(type(i))
                for i in l:
                    if 'day' not in i:
                        i.update({"day":''})
                    del i['day']
                    i.update(mmie)
                # result={"result":l}
                print(l,"er")
                u=finaldata12(l,data['result'],timeslot)


               
                
                

                return { 'statusCode': 200, 'body':u,'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    }}
    elif event['path'] == "/showinterval":
        print("www")
        if event['httpMethod'] == "POST":
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            userId=i['userId']
            column = 'date,userId,timestart,totaltime'
            data = databasefile.SelectQuery("bookappointment",column,'',"","","")
            print(data)
            timeslot=kk
            print(kk)
                       
            if data!='0':
                a=CurrentDatetime()
                b=AddDaysInCurrentDate(720)
                customholidays=['2020-08-15','2020-08-16']
                weekholidays=['1']
                
                serviceoption={"serviceoption":[{"serviceName":"abc","time":"30"},{"serviceName":"abcd","time":"30"},{"serviceName":"abcde","time":"15"}],"userId":"1234prashant"}
                
                date_format = "%Y-%m-%d"
                a = datetime.strptime(a, date_format)
                b = datetime.strptime(b, date_format)
                



               # end date

                delta = b-a
                

                c=[]   
                day_name= ['1', '2', '3', '4', '5', '6','7']
                # as timedelta
                k=[]

                l=[]

                for i in range(delta.days + 1):
                    
                    day = a + timedelta(days=i)
                   
                    d=day.strftime('%Y-%m-%d')
                    kkk=calendar.day_name[day.weekday()] 
                    k.append(kkk)
                    

                    
                    l.append({"date":d,'day':kkk})
                for i in l:
                    

                    date=i['date']
                    day=i['day']
                    for n in weekholidays:
                        if n == day:
                            l.remove(i)
                    for kn in customholidays:
                        
                        if kn == date:
                           
                            l.remove(i)
                    del i['day']

                    print(type(i))
                for i in l:
                    if 'day' not in i:
                        i.update({"day":''})
                    del i['day']
                    #i.update(mmie)
               
                print(l,"er")
                u=finaldata1(l,data['result'],kk)


               
                
                

                return { 'statusCode': 200, 'body':u,'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    }}
    elif event['path'] == "/updateappiontmentmeeting":
        t=type(event['body'])
        print(event['body'])
        print(t)
        i=json.loads(event['body'])
        print(i)
        print(type(i))
        time=i['time']
        Type=i['type']
        userId=i['userId']
       
        column="time='" + time+ "'and type='" + Type+"'"
        whereCondition= "  and userId= '" + str(userId)+ "' "
        output=databasefile.UpdateQuery("appiontmentmeeting",column,whereCondition)
        if output!='0':
            t={}
            t['result']='updated Successfully'
            hpp=mm(t)
            return {'statusCode':200,'body':json.dumps(hpp)}
        else:
            return {'statusCode':200,'body':'Don"t Exist'}
   
    elif event['path'] =="/appiontmentmeeting":
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            time=i['time']
            Type=i['type']
            userId=i['userId']
           
            WhereCondition = " and userId = '" + str(userId) +"'"
            count = databasefile.SelectCountQuery("appiontmentmeeting",WhereCondition,"")
            if int(count) > 0:
                return {'statusCode':404}
            else:
                if flag =="i":
                    print("11111111111111111111111")
                    column = "time,type,userId"      
                    values = " '" + str(name)+ "','" + str(Type) + "','" + str(userId)   + "' "
                 
                    data = databasefile.InsertQuery("appiontmentmeeting",column,values)       
                    if data != "0":

                        column = 'time,type,userId'
                        data = databasefile.SelectQuery("appiontmentmeeting",column,WhereCondition,"","","")
                        print(data)
                        p=[]
                        for i in data['result']:
                            g=d(i)
                            p.append(g)
                        h={}
                        h['result']=p
                        hpp=d(i)


                       
                        
                        

                        return { 'statusCode': 200, 'body':json.dumps(hpp)}
                    else:
                        return "qq"
        else:
            column = 'time,type,userId'
            data = databasefile.SelectQuery("appiontmentmeeting",column,WhereCondition,"","","")
            print(data)
            p=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            h={}
            h['result']=p
            hpp=d(i)


           
            
            

            return { 'statusCode': 200, 'body':json.dumps(hpp)}
    elif event['path'] =="/weekholidays":
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            Days=i['Days']
            userId=i['userId']
           
            WhereCondition = " and userId = '" + str(userId) +"'"
            count = databasefile.SelectCountQuery("weekholidays",WhereCondition,"")
            if int(count) > 0:
                return {'statusCode':404}
            else:
                if flag =="i":
                    print("11111111111111111111111")
                    column = "Days,userId"      
                    values = " '" + str(Days) + "','" + str(userId)   + "' "
                 
                    data = databasefile.InsertQuery("weekholidays",column,values)       
                    if data != "0":

                        column = 'Days,userId'
                        data = databasefile.SelectQuery("weekholidays",column,WhereCondition,"","","")
                        print(data)
                        p=[]
                        for i in data['result']:
                            g=d(i)
                            p.append(g)
                        h={}
                        h['result']=p
                        hpp=d(i)


                       
                        
                        

                        return { 'statusCode': 200, 'body':json.dumps(hpp)}
                    else:
                        return "qq"
        else:
            column = 'Days,userId'
            data = databasefile.SelectQuery("weekholidays",column,WhereCondition,"","","")
            print(data)
            p=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            h={}
            h['result']=p
            hpp=d(i)


           
            
            

            return { 'statusCode': 200, 'body':json.dumps(hpp)}
    elif event['path'] =="/bookappointmentgolf":
        
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            date=i['date']

            
            timestart=i['timestart']
            totaltime=i['totaltime']
            name=i['name']
            password=i['password']
            email=i['email']
            userId=CreateHashKey(email,name)
            bookingId=CreateHashKey(timestart,date)
            whereCondition="and date='"+str(date)+"' and timestart='"+str(timestart)+"' and  appiontmentId ='"+str("1234prashant")+"'"
            count = databasefile.SelectCountQuery("bookappointment",whereCondition,"")
            print(count)
            count=int(count)
            if  count ==0:
                column = "date,appiontmentId,timestart,totaltime,bookingId,userId"      
                values = " '" + str(date)+ "','" + str("1234prashant") + "','" + str(timestart)+ "','" + str(totaltime) + "','" + str(res)+ "','" + str(userId)      + "' "

                data = databasefile.InsertQuery("bookappointment",column,values)
                column="appiontmentId,bookingId,counter"
                values= " '" + str("1234prashant")+ "','" + str(bookingId) + "','" + str(1)+ "'"
                data = databasefile.InsertQuery("bookappointmentGolfMapping",column,values)

             
                     

                column = "name,usersId,password,email"      
                values = " '" + str(name)+ "','" + str(userId) + "','" + str(password)+ "','" + str(email)      + "' "
             
                data = databasefile.InsertQuery("UserMaster",column,values) 
            else:
                if count ==1:
                    column = "date,appiontmentId,timestart,totaltime,bookingId,userId"      
                    values = " '" + str(date)+ "','" + str("1234prashant") + "','" + str(timestart)+ "','" + str(totaltime) + "','" + str(res)+ "','" + str(userId)      + "' "
                    data = databasefile.InsertQuery("bookappointment",column,values)
                    column="counter=" + str(2)+ "'"
                    WhereCondition=" and appiontmentId='"+str(appiontmentId) +"'"
                    data = databasefile.UpdateQuery("bookappointmentGolfMapping",column,WhereCondition)


                    column = "name,usersId,password,email"      
                    values = " '" + str(name)+ "','" + str(userId) + "','" + str(password)+ "','" + str(email)      + "' "
                    data = databasefile.InsertQuery("UserMaster",column,values) 
                if count ==2:
                    column = "date,appiontmentId,timestart,totaltime,bookingId,userId"      
                    values = " '" + str(date)+ "','" + str("1234prashant") + "','" + str(timestart)+ "','" + str(totaltime) + "','" + str(res)+ "','" + str(userId)      + "' "
                 
                    data = databasefile.InsertQuery("bookappointment",column,values) 
                    column="counter=" + str(3)+ "'"
                    WhereCondition=" and appiontmentId='"+str(appiontmentId) +"'"
                    data = databasefile.UpdateQuery("bookappointmentGolfMapping",column,WhereCondition)    

                    column = "name,usersId,password,email"      
                    values = " '" + str(name)+ "','" + str(userId) + "','" + str(password)+ "','" + str(email)      + "' "
                 
                    data = databasefile.InsertQuery("UserMaster",column,values)
                if count==3:
                    column = "date,appiontmentId,timestart,totaltime,bookingId,userId"      
                    values = " '" + str(date)+ "','" + str("1234prashant") + "','" + str(timestart)+ "','" + str(totaltime) + "','" + str(res)+ "','" + str(userId)      + "' "
                 
                    data = databasefile.InsertQuery("bookappointment",column,values) 

                    column="counter=" + str(3)+ "'"
                    WhereCondition=" and appiontmentId='"+str(appiontmentId) +"'"
                    data = databasefile.UpdateQuery("bookappointmentGolfMapping",column,WhereCondition)    

                    column = "name,usersId,password,email"      
                    values = " '" + str(name)+ "','" + str(userId) + "','" + str(password)+ "','" + str(email)      + "' "
                 
                    data = databasefile.InsertQuery("UserMaster",column,values) 




           
           
            print("11111111111111111111111")
                
            if data != "0":


                column = 'date,userId,timestart,totaltime,bookingId,appiontmentId'
                data = databasefile.SelectQuery("bookappointment",column,"","","","")
                print(data)
                # p=[]
                # for i in data['result']:
                #     g=m(i)
                #     p.append(g)
                h={}
                h['result']=data['result']
                print()
                
                return { 'statusCode': 200, 'body':json.dumps(h),'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    }}
    elif event['path'] == "/addappiontmentmeetinterval":
        print("appiontmentName")
        t=type(event['body'])
        print(event['body'])
        print(t)
        i=json.loads(event['body'])
        print(i)
        print(type(i))
        s=CurrentDatetime()
        p=AddDaysInCurrentDate(720)

        appiontmentName=i['appiontment']
        default_timeout=i['default_timeout']
        userId=i['userId']
        spaceId=i['spaceId']
        WhereCondition = "and appointmentId ='"+str(userId)+"'"
        count = databasefile.SelectCountQuery("appiontmentmeetMaster",WhereCondition,"")
        count=0

        if int(count) > 0:
            interval=i['interval']
            WhereCondition=" and appointmentId ='"+str(userId)+"'"
            delinterval=databasefile.DeleteQuery('appiontmentintervalMaster',WhereCondition)
            delServiceOption=databasefile.DeleteQuery('serviceoptionMaster',WhereCondition)
            deltod=databasefile.DeleteQuery('setDatetodMaster',WhereCondition)
            delweek=databasefile.DeleteQuery('setDateweekMaster',WhereCondition)
            delcustom=databasefile.DeleteQuery('setDatecustomMaster',WhereCondition)

            for m in interval:
                start_time=m['start_time']
                end_time=m['end_time']
                column = "start_time,end_time,appiontmentId ,default_timeout"  
                values = " '" + str(start_time)+ "','" + str(end_time) + "','" + str(userId) + "','" + str(default_timeout)  + "' "
                data = databasefile.InsertQuery("appiontmentintervalMaster",column,values) 
            
            serviceoption=i['serviceoption']

            
            for k in serviceoption:
                serviceName=k['serviceName']
                time=k['time']
                print("11111111111111111111111")
                column = "serviceName, time,appiontmentId"      
                values = " '" + str(serviceName)+ "','" + str( time) + "','" + str(userId)   + "' "
                data = databasefile.InsertQuery("serviceoptionMaster",column,values)      

            setDate=i['setDate']
            
            for l in setDate:
                today=l['today']
                column = " today,appiontmentId"      
                values = " '" + str(today)+ "','" + str(userId)   + "' "
                data = databasefile.InsertQuery("setDatetodMaster",column,values)   

                week =l['week']
                
                if week != ""or week !=None:
                    for ll in week:
                        column = " days,appiontmentId"      
                        values = " '" + str(ll)+ "','" + str(userId)   + "' "
                        data = databasefile.InsertQuery("setDateweekMaster",column,values)   

                customday=l['customday']
                
                if customday !=""or customday !=None:
                    for o in customday:
                        column = " date,appiontmentId"      
                        values = " '" + str(o)+ "','" + str(userId)   + "' "
                        data = databasefile.InsertQuery("setDatecustomMaster",column,values)  
            t={}
            t['result']='Interval Updated Successfully'
            hpp=mm(t)
            return {'statusCode':200,'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    },'body':json.dumps(hpp)} 
        else:
            flag="i"
            if flag =="i":
                print("11111111111111111111111")
                column = "appointmentName,default_timeout,appointmentId,startDate,endDate,spaceId"      
                values = " '" + str(appiontmentName)+ "','" + str(default_timeout) + "','" + str(spaceId)  + "','" + str(s) + "','" + str(p)  + "','" + str(spaceId) + "' "
                data = databasefile.InsertQuery("appiontmentmeetMaster",column,values)      

                interval=i['interval']
               


                for m in interval:
                    start_time=m['start_time']
                    end_time=m['end_time']
                    column = "start_time,end_time,appointmentId ,default_timeout,appiontmentName"
                    values = " '" + str(start_time)+ "','" + str(end_time) + "','" + str(spaceId) + "','" + str(default_timeout) + "','" + str( appiontmentName)  + "' "
                    data = databasefile.InsertQuery("appiontmentintervalMaster",column,values) 
                serviceoption=i['serviceoption']
                for k in serviceoption:
                    serviceName=k['serviceName']
                    time=k['time']
                    print("11111111111111111111111")
                    column = "serviceName, time,appointmentId,appiontmentName"  
                    values = " '" + str(serviceName)+ "','" + str( time) + "','" + str(spaceId) + "','" + str( appiontmentName)+ "' "
                    data = databasefile.InsertQuery("serviceoptionMaster",column,values)      

                setDate=i['setDate']
                for l in setDate:
                    today=l['today']
                    column = " today,appointmentId"      
                    values = " '" + str(today)+ "','" + str(userId)   + "' "
                    data = databasefile.InsertQuery("setDatetodMaster",column,values)   

                    week =l['week']
                    if week != ""or week !=None:
                        for ll in week:
                            column = " days,appointmentId"      
                            values = " '" + str(ll)+ "','" + str(userId)   + "' "
                            data = databasefile.InsertQuery("setDateweekMaster",column,values)   

                    customday=l['customday']
                    if customday !=""or customday !=None:
                        for o in customday:
                            column = " date,appointmentId"      
                            values = " '" + str(o)+ "','" + str(userId)   + "' "
                            data = databasefile.InsertQuery("setDatecustomMaster",column,values) 
                    weekholidays=l['weekholidays']
                    customholidays=l['customholidays']

                    # for j in weekholidays:
                    #         column = "days,userId"   
                    #         values = " '" + str(j) + "','" + str(userId)   + "' "
                    #         data = databasefile.InsertQuery("weekholidays",column,values) 
                    # for y in customholidays:
                    #         column = "date,userId"
                    #         values = " '" + str(y) + "','" + str(userId)   + "' "
                    #         data = databasefile.InsertQuery("weekholidays",column,values)  





       
       
       
                t={}
                
                t['result']='Interval Added Successfully'
                
                return {'statusCode':200,'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    },'body':json.dumps(t)} 
    elif event['path'] =="/bookappointment":
        
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            date=i['date']

            
            timestart=i['timestart']
            totaltime=i['totaltime']
           
            userId=i['userId']

            spaceId=i['spaceId']
            bookingId=i['UserId']


           
           
            print("11111111111111111111111")
            column = "date,appiontmentId,timestart,totaltime,bookingId,userId"      
            values = " '" + str(date)+ "','" + str(spaceId) + "','" + str(timestart)+ "','" + str(totaltime) + "','" + str(res)+ "','" + str(userId)      + "' "
         
            data = databasefile.InsertQuery("bookappointment",column,values)     

           
         
            data = databasefile.InsertQuery("UserMaster",column,values)     
            if data != "0":


                column = 'date,userId,timestart,totaltime,bookingId,appiontmentId'
                data = databasefile.SelectQuery("bookappointment",column,"","","","")
                print(data)
                # p=[]
                # for i in data['result']:
                #     g=m(i)
                #     p.append(g)
                h={}
                h['result']=data['result']
                print()
                
                return { 'statusCode': 200, 'body':json.dumps(h),'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                    }}
    elif event['path'] =="/userssignup":

        v1="1"
        if event['httpMethod'] == "POST":
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            name=i['name']
            print(name)
            phone=i['phone']
            email=i['email']
            password=i['password']
            confirmPassword=i['confirmPassword']
            print("ss")
            if confirmPassword == password:
                print("sse")

                userId=CreateHashKey(name,email)
               
                flag="i"
                WhereCondition = "and name='"+str(name)+"' or email ='"+str(email)+"'"
                count = databasefile.SelectCountQuery("usermaster",WhereCondition,"")
                print(count)


                if int(count) > 0:
                    print("dd")
                    h={}
                    h['result']='User Already Exist with phone or email or name,Please rename all '
                    hpp=dyy(h)
                    return {'statusCode':201,'body':json.dumps(hpp),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        } }
                else:
                    if flag =="i":
                        print("11111111111111111111111")
                        column = "email,phone,password,usersId,name"            
                        values = " '" + str(email) + "','" + str(phone) + "','" + str(password) + "','" + str(userId)+ "','" + str(name)+ "' "
                        data = databasefile.InsertQuery("usermaster",column,values)       
                        if data != "0":

                            column = 'name,email,phone,password,usersId as UserId'
                            data = databasefile.SelectQuery("usermaster",column,WhereCondition,"","","")
                            print(data)
                            p=[]
                            for i in data['result']:
                                g=dyy(i)
                                p.append(g)
                            h={}
                            h['result']=p
                            hpp=dyy(i)


                           
                            
                            

                            return { 'statusCode': 200, 'body':json.dumps(hpp),'headers': {
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                        }}
                        else:
                            return "qq"
            else:
                h={}
                h['result']='confirmPassword & password are not same'
                hpp=d(i)
                return { 'statusCode': 201, 'body':json.dumps(hpp),'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }}
    elif event['path'] == "/userslogin":
        print("www")
        if event['httpMethod'] == "POST":
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            email=i['email']
            password=i['password']
            
           
            column="email,password,usersId as UserId"
            WhereCondition= "  and email = '" + str(email)+ "' and password='"+password+"'"
            data = databasefile.SelectQuery("usermaster",column,WhereCondition,"","","")
            print(data)
            if data['status'] !='false':
                h=[]
                for i in data['result']:
                    k=dyy(i)

                    stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

                    a=stripe.Token.create(
                      pii={"id_number": i['UserId']},
                    )

                    asjj={}
                    asjj['token']=a['id'] +str(a['id'][::-1])+str(a['id'][::-6])+str(a['id'][::-1])+str(a['id'][::-5])+str(a['id'][::-2])+str(a['id'][::-3])+str(a['id'][::-4])
                    print(asjj)
                    asjj['UserId']=i['UserId']
                    WhereCondition= "  and email = '" + str(email)+ "' and password='"+password+"'"
                    column="token ='"+ str(asjj['token'])+"'"
                    data = databasefile.UpdateQuery("usermaster",column,WhereCondition)

               
                hpp=dyy(asjj)
                print({'statusCode':200,'body':hpp})
                return {'statusCode':200,'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },'body':json.dumps(hpp)}
            else:
                return {'statusCode':201,'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },'body':json.dumps({'result':'Wrong password and email ,Please Enter Correct Credentails','status':'false'})}

    elif event['path'] =="/allbookings":
        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
           
            UserId=i['UserId']

           
           
            

            column = 'date,userId,timestart,totaltime,bookingId,appiontmentId'
            WhereCondition=" and bookingId='"+str(bookingId)+"'"
            data = databasefile.SelectQuery("bookappointment",column,"","","","")
            print(data)
            for i in data['result']:
                tm=i['timestart']
                t=int(i['totaltime'])
                a = datetime.strptime(tm, "%H:%M")
                d=a+timedelta(minutes=t)
                e=d.strftime("%H:%M")
                i.update({"appiontmentName":"Doctor"})
                i.update({"timeEnd":e})

            # p=[]
            # for i in data['result']:
            #     g=m(i)
            #     p.append(g)
            h={}
            h['result']=data['result']
            print()
            
            return { 'statusCode': 200, 'body':json.dumps(h),'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                }}
                    
                    
    elif event['path'] =="/allholidays":

        if event['httpMethod'] == "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
         
            userId=i['userId']
           
            WhereCondition = " and userId = '" + str(userId) +"'"
            

            column = 'Date,userId'
            column='Days'
            data = databasefile.SelectQuery("customholidays",column,WhereCondition,"","","")
            data2=databasefile.SelectQuery("weekholidays",column,WhereCondition,"","","")
            print(data)
            p=[]
            lla=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            for j in data2['result']:
                ll=d(i)
                lla.append(ll)

            h={}
            h['result']={'customholidays':p,'weekholidays':lla}
            hpp=d(h)
            return { 'statusCode': 200, 'body':json.dumps(hpp)}
                
    
    else:
        if event['httpMethod']== "POST":
            print("w")
            t=type(event['body'])
            print(event['body'])
            print(t)
            i=json.loads(event['body'])
            print(i)
            print(type(i))
            Days=i['Date']
            userId=i['userId']
           
            WhereCondition = " and userId = '" + str(userId) +"'"
            count = databasefile.SelectCountQuery("customholidays",WhereCondition,"")
            if int(count) > 0:
                return {'statusCode':404}
            else:
                if flag =="i":
                    print("11111111111111111111111")
                    column = "Date,userId"      
                    values = " '" + str(Days) + "','" + str(userId)   + "' "
                 
                    data = databasefile.InsertQuery("customholidays",column,values)       
                    if data != "0":

                        column = 'Date,userId'
                        data = databasefile.SelectQuery("customholidays",column,WhereCondition,"","","")
                        print(data)
                        p=[]
                        for i in data['result']:
                            g=d(i)
                            p.append(g)
                        h={}
                        h['result']=p
                        hpp=d(i)


                       
                        
                        

                        return { 'statusCode': 200, 'body':json.dumps(hpp)}
                    else:
                        return "qq"
        else:
            column = 'Date,userId'
            data = databasefile.SelectQuery("customholidays",column,WhereCondition,"","","")
            print(data)
            p=[]
            for i in data['result']:
                g=d(i)
                p.append(g)
            h={}
            h['result']=p
            hpp=d(i)


           
            
            

            return { 'statusCode': 200, 'body':json.dumps(hpp)}


       
        






