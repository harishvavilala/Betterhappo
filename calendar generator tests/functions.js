/*
Created on Sat Jun 15 15:07:13 2019
Full calendar test 1.0
@author: s516936

All dates are represented in MM-DD-YYYY 
All funcitons needing dates in inputs or as outputs will use this order
Dates are stored in arrays
*/


/*
This function will take a year.
It return 1 if it is a leap year and zero if it is not. 
*/
function leap(year){
   if ((year % 100) %4 == 0){
   		return 1}
   if((year % 1000) - ((year % 100) % 4 == 0) && (year % 100)==0){
   		return 1}
   return 0
}
//console.log(leap(2019));


/*
This function will take a date. 
It will output the number of days from 1-366.
(01/01/2019 -> 01 ;12/31/2019 -> 365) 
*/
function MDYToNumDay(date){ //-> int
    var month= date[0]
    var day = date[1]
    var year = date[2]
    var monthDays =  [31,28+leap(year),31,30,31,30,31,31,30,31,30,31];
    var numDays = day;
    for( var i=0 ;i<month-1;i++){
        numDays += monthDays[i] }
    return numDays;
 }
//console.log("mMDYToNumDay 1,2,2019: "+MDYToNumDay([1,2,2019]));


/*
This function will take a number of days from 1-365 and and a year.
It will output the corasponding date.
(01,2019 -> 01/01/2019 ; 365 -> 12/31/2019) 
*/
function numDayToMDY(dayNum,year){// -> month, Day, Year
   var monthDays =  [31,28+leap(year),31,30,31,30,31,31,30,31,30,31]
    for (var month = 0; month <12;month++){
        if (dayNum > monthDays[month]){
			dayNum -= monthDays[month];}
        else{
			return [month+1,dayNum,year];}
	}
}
//console.log("NumDayToMDY 111,2019: "+numDayToMDY(111,2019));


/*
This function will take an int and a date. 
It will output the date that is however many days befor or after the date.
(2 , 01/01/2019 -> 01/03/2019 ) 
*/
function relativeDate(numberOfDays, date){//-> date
   console.log(date)
   let year = date[2]
   var monthDays =  [31,28+leap(date[2]),31,30,31,30,31,31,30,31,30,31]
   var dateDayNumber = MDYToNumDay(date)
   dateDayNumber += numberOfDays
   var dateNew = numDayToMDY(dateDayNumber,year)
   if (dateNew[1]<0){
		dateNew[2] -=1 
		dateNew[0] = 13 - dateNew[0]
		i = date[1]
		i += 31
		dateNew[1] += monthDays[dateNew[0]-1]
   }
   return dateNew
}
//console.log(relativeDate(-46, [4,21,2019]))


/*
This function will take a date. 
It will output the day of the week that date falls on as an int .
(01/01/2019 -> 2)

days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
Code from: http://mathforum.org/dr.math/faq/faq.calendar.html 
Modifide by Zac Haider
*/
function weekDay(date){// - >int
	var month= date[0]
	var day = date[1]
	var year = date[2]
    if (month<3){
        month+=10
		d = (year%100)-1
	}
    else{
         month-=2
		d = (year%100)
		}
   var c = parseInt((year-d)/100)
    var f =(day + parseInt(((13*month)-1)/5) + d + parseInt(d/4) + parseInt(c/4) - (2*c))%7
    return f;
}
//console.log("weekDay: "+weekDay([1,1,2019]));


/*
This funciton will take an input of a year.
It will output the date of easter for the year entered.
The code is from:http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/
*/
function calcEaster(year){//->[int]
    var a = (year % 19)
    var b = parseInt(year / 100)
    var c = (year % 100)
    var d = (19 * a + b - b / 4 - parseInt((b - (b + 8) / 25 + 1) / 3) + 15) % 30
    var e = (32 + 2 * (b % 4) + 2 * parseInt(c / 4) - d - (c % 4)) % 7
    var f = d + e - 7 * parseInt((a + 11 * d + 22 * e) / 451) + 114
    var month = parseInt(f / 31)
    var day = f % 31 + 1    
    return  [month,day,year]
}
//console.log("calcEaster: "+calcEaster(2019));


/*
This function will take an int and a year. 
It will output all the date that are sundays.
(2019 -> [[1,6,2019],...[12/30/2019)] ] 
*/
function allSundays(year){// - >[ [int,int,int,string,string] ]
   var calendar = []
    for( i = 1-weekDay([1,1,year]);i<(366+leap(year));i+=7){
        if (i>0){
            calendar.push(numDayToMDY(i,year))
		}
	}
	return calendar
}
//console.log("allSundays "+allSundays(2019))

/*
This function will take a year.
It return the whole calendar for the luthren church. 
*/
function  allDays(year){
    let easter = calcEaster(year)
	console.log(7-(weekDay([1,6,year])))
    var epiphanyA = [1,6,year]
    if (weekDay([1,6,year])>0){
    epiphanyA = relativeDate(7-(weekDay([1,6,year])),[1,6,year])
	}
    let epiphanyB = relativeDate(14,epiphanyA)
    let ashWed = relativeDate(-46,easter)
    let epiphanyC = relativeDate(-3, ashWed)
    let lent = relativeDate(4,ashWed)
    let palm = relativeDate(-7,easter)
    let hThursday = relativeDate(-3,easter)
    let gFriday = relativeDate(-2,easter)
    //easter
    let pentA = relativeDate(49,easter)
    let trinity = relativeDate(7,pentA)
    let pentB = relativeDate(7,trinity)
    let ref =  relativeDate(0-weekDay([10,31,year]),[10,31,year])
    let saints =  relativeDate(7,ref)
    let pentD = relativeDate(7,saints)
    let thanks = relativeDate(0-weekDay([11,3,year]),[11,28,year])
    let advent = relativeDate(3,thanks)
    let xmas = [12,25,year]
    
    let sundays = allSundays(year)
    let yearFixedDates = [[epiphanyA,"white","Epiphany First Block"],[epiphanyB,"green","Epiphany Second Block"],[epiphanyC,"white","Epiphany Final Block"],[ashWed,"black","Ash Wednesday"],[lent,"purple","Lent"],[palm,"red","Palm Sunday"],[hThursday,"white","Holy Thursday"],[gFriday,"black","Good Friday"],[easter,"white","Easter"],[pentA,"red","Pentecost First Block"],[trinity,"white","Trinity"],[pentB,"green","Pentecost Second Block"],[ref,"red","Reformation"],[saints,"white","All Saints Day"],[pentD,"green","Pentecost Final Block"],[thanks,"white","Thanks Giving"],[advent,"blue","Advent"],[xmas,"white","Cristmas"]]
	let monthDays =  [31,28+leap(year),31,30,31,30,31,31,30,31,30,31];
	var calendar = [[[0,0,0],"white"]] 
	for (var month =0;month <12;month++){
		for (var day =1;day<monthDays[month]+1;day++){
			if (yearFixedDates.length >0){
			if ((yearFixedDates[0][0])+"" == sundays[0]+"" ){
					sundays.splice(0,1)
			}		
			if ((yearFixedDates[0][0])+"" == [month+1,day,year]+"" ){
				calendar.push(yearFixedDates[0])
				yearFixedDates.splice(0,1)
			}}
			if (sundays[0]+"" == [month+1,day,year]+""){
				calendar.push([[month+1,day,year],calendar[calendar.length-1][1]])
				sundays.splice(0,1)
			}
		}
	}
	calendar.splice(0,1)
	return calendar
}
//console.log(allDays(2019))

