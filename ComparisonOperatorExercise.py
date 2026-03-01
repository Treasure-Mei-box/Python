"""
month = int(input("Enter a month: "))
week = int(input("Enter a week: "))
day = int(input("Enter day: "))

TotalWorkingDays = (month*30) + (week*7)
RemainingDays = TotalWorkingDays - day 
print(f"Total working days left - {RemainingDays}")

hoursFirst = int(input("Enter hours for first trip: "))
minutesFirst = int(input("Enter minutes for first trip: "))
secondsFirst = int(input("Enter seconds for first trip: "))

firstTrip = (hoursFirst*3600) + (minutesFirst*60) + secondsFirst

hoursSecond = int(input("Enter hours for second trip: "))
minutesSecond = int(input("Enter minutes for second trip: "))
secondsSecond = int(input("Enter seconds for second trip: "))

secondTrip = (hoursSecond*3600) + (minutesSecond*60) + secondsSecond

totalTrip = firstTrip + secondTrip
print(f"Total seconds for both trips - {totalTrip} seconds")
totalHours = totalTrip // 3600
totalMinutes = (totalTrip % 3600) // 60
totalSeconds = totalTrip % 60 

#print(f"Total time for both trips - {totalHours} hours, {totalMinutes} minutes, {totalSeconds} seconds")
"""

print('hi.')
print("hi")
print("'hi '")