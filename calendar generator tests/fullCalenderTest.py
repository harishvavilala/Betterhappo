# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 15:07:13 2019
Full calender test 1.0
@author: s516936

All dates are represented in MM-DD-YYYY 
All funcitons needing dates in inputs or as outputs will use this order
Dates are stored in touples 

"""
#Functions_____________________________________________________________________

"""
This function will take a number of days from 1-365 and and a year.
It will output the corasponding date.
(01,2019 -> 01/01/2019 ; 365 -> 12/31/2019) 
""" 
def numDayToMDY(dayNum,year):# -> month, Day, Year
    leap = not((year % 100) %4 == 0 or ((year % 1000) - (year % 100)) % 4 == 0) 
    monthDays =  (31,28+leap,31,30,31,30,31,31,30,31,30,31)
    for month in range(12):
        if dayNum > monthDays[month]:
            dayNum-=monthDays[month]
        else:
            return month+1,dayNum,year
#funtion test
# for x in range(200,366):
#     print(numDayToMDY(x,2019))


"""
This function will take a date. 
It will output the number of days from 1-366.
(01/01/2019 -> 01 ;12/31/2019 -> 365) 
""" 
def MDYToNumDay(month = 0 ,day = 0,year = 0, date = ()): #-> int
    if len(date)>0:
        month= date[0]
        day = date[1]
        year = date[2]
    leap = not((year % 100) %4 == 0 or ((year % 1000) - (year % 100)) % 4 == 0) 
    monthDays =  (31,28+leap,31,30,31,30,31,31,30,31,30,31)
    numDays = day
    for i in range(month-1):
        numDays += monthDays[i] 
    return numDays

#function test
# year = 2019
# leap = not((year % 100) %4 == 0 or ((year % 1000) - (year % 100)) % 4 == 0) 
# monthDays =  (31,28+leap,31,30,31,30,31,31,30,31,30,31)
# for x in range(6):
#     for y in range(1,monthDays[x]+1,1):
#         print(x+1,y,year)
#         print(MDYToNumDay(x+1 ,y,year))
#         print()


"""
This function will take an int and a date. 
It will output the date that is however many days befor or after the date.
(2 , 01/01/2019 -> 01/03/2019 ) 
"""
def relativeDate(numberOfDays , month = 0 ,day = 0,year = 0, date = ()): #-> int
    leap = not((year % 100) %4 == 0 or ((year % 1000) - (year % 100)) % 4 == 0) 
    monthDays =  (31,28+leap,31,30,31,30,31,31,30,31,30,31)
    if len(date)>0:
        month= date[0]
        day = date[1]
        year = date[2]
    temp = numDayToMDY((MDYToNumDay(month,day,year)+numberOfDays),year)
    if temp[1]<1:
        month = 12-(temp[0]-1)
        day = monthDays[temp[0]]+temp[1]
        if month ==12 or (temp[0]-1)>2:
            year-=1
        
    return numDayToMDY((MDYToNumDay(month,day,year)+numberOfDays),year)

#function test
#print(relativeDate(2,2,4,2019))


"""
This function will take a date. 
It will output the day of the week that date falls on as an int .
(01/01/2019 -> 2)

days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
Code from: http://mathforum.org/dr.math/faq/faq.calendar.html 
Modifide by Zac Haider
""" 
def weekDay(month = 0 ,day = 0,year = 0, date = ()): # - >int
    if len(date)>0:
        month= date[0]
        day = date[1]
        year = date[2]
    if month<3:
        month+=10
        d = (year%100)-1
    else:
         month-=2
         d = (year%100)
    c = (year-d)//100
    f = (day + ((13*month)-1)//5 + d + (d//4) + (c//4) - (2*c))%7
    return f


"""
This funciton will take an input of a year.
It will output the date of easter for the year entered.
The code is from:http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/
"""
def calcEaster( year):#->[int]
    a = (year % 19)
    b = (year // 100)
    c = (year % 100)
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return  month,day,year


"""
This function will take an int and a year. 
It will output all the date that are sundays.
(2019 -> [(1,6,2019),...(12/30/2019)] ) 
"""
def allSundays(year): # - >[ [int,int,int,string,string] ]
    leap = not((year % 100) %4 == 0 or ((year % 1000) - (year % 100)) % 4 == 0) 
    calender = []
    for i in range(1-weekDay(1,1,year),366+leap,7):
        if i>0:
            month,day, year = numDayToMDY(i,year)
            dayOfTheWeek = weekDay(date=(month,day,year))
            calender.append((month,day,year))
    return calender





# Main_________________________________________________________________________

cal = []
allFixedDates =[]
for year in range(2014,2021,1):
    easter = calcEaster(year)
    
    epiphanyA = relativeDate(7-(weekDay(date=(1,6,year))),date = (1,6,year))
    epiphanyB = relativeDate(7,date = epiphanyA)
    epiphanyC = relativeDate(-49,date = easter)
    ashWed = relativeDate(-46,date = easter)
    lent = relativeDate(4,date = ashWed)
    palm = relativeDate(-7,date = easter)
    hThursday = relativeDate(-3,date = easter)
    gFriday = relativeDate(-2,date = easter)
    #easter
    pentA = relativeDate(49,date = easter)
    trinity = relativeDate(7,date = pentA)
    pentB = relativeDate(7,date = trinity)
    ref =  relativeDate(0-weekDay(10,31,year),date = (10,31,year))
    saints =  relativeDate(7,date=ref)
    pentD = relativeDate(7,date = saints)
    thanks = relativeDate(0-weekDay(11,3,year),11,28,year)
    advent = relativeDate(3,date = thanks)
    xmas = (12,25,year)
    
    sundays = allSundays(year)
    yearFixedDates = [epiphanyA,epiphanyB,epiphanyC,ashWed,lent,palm,hThursday,gFriday,easter,pentA,trinity,pentB,ref,saints,pentD,thanks,advent, xmas]
    for x in yearFixedDates:
        print(x)
    allFixedDates+= yearFixedDates
    cal += sorted(set(yearFixedDates+sundays), key = lambda x: (x[0], x[1]))


#file writenig 
csv = True
json = False

if csv:
    colors =["white","white","green","white","black","purple","red","white","black","white","red","white","green","red","white","green","white","blue","white"]
   
    finalCalC = []
    colorIndex = 0
    for date in cal:
        if date in allFixedDates and len(finalCalC):
            if colorIndex == len(colors)-1:
                colorIndex = 0
            else:
                colorIndex+=1
        finalCalC.append((date,colors[colorIndex]))
    with open("cal.csv","w") as file:
        file.write("month,day,year,color\n") 
        for x in finalCalC:
             temp = str(x)
             temp = temp.replace("(","").replace(")","").replace("'","").replace(" ","") +"\n"
             file.write(temp)
if json: 
    finalCalJ = []
    colors =["white","white","green","white","black","purple","red","white","black","white","red","white","green","red","white","green","white","blue","white"]
    colorIndex = 0
    for date in cal:
        if date in allFixedDates and len(finalCalJ):
            if colorIndex == len(colors)-1:
                colorIndex = 0
            else:
                colorIndex+=1
        print(colorIndex)
        finalCalJ.append(("{date:","[Month:",date[0],"Day:",date[1],"Year:",date[2],"]color:",colors[colorIndex],"}"))
    with open("cal.json","w") as file:
        file.write("[")
        for x in finalCalJ:
             temp = str(x)
             temp = temp.replace("(","").replace(")","").replace("'","").replace(" ","") +"\n"
             file.write(temp)
        file.write("]")




    





