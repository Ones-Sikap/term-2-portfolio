#jacob cook
#Activity Planer
#1/8/2020

import datetime
import random
import math

# tuples of daily options and matching prices
options = ("Snorkeling","Scuba Diving","Fishing","Sunbathing","Shopping","Helicopter Ride","Sleeping")
prices  = (10.00, 150.00, 25.00, 0.00, 200.00, 450.00, 0.00)

# get and parse vacation starting and ending dates
staying = input("when are you staying put in mm-dd-year format:")
startDate = datetime.datetime.strptime(staying,"%m-%d-%Y")
leaving = input("when are you leaving put in mm-dd-year format:")
stopDate = datetime.datetime.strptime(leaving,"%m-%d-%Y")





# calculate and print the timedelta difference between dates
delta = stopDate - startDate
print("Your vacation is ",delta,"days long")



# initialize empty costs list
costs = []
for i in range(delta.days):
    activityIndex = random.randrange(0,7)  #random.randint(0,len(options))
    activity = options[activityIndex]
    cost = prices[activityIndex]
    thisDate = startDate + datetime.timedelta(days=i)
    thisDateString = datetime.datetime.strftime(thisDate, "%m-%d-%Y")
    print(str.format("On {}, {} costs ${:.2f}",str(thisDateString),activity,cost))
    costs.append(cost)
print(str.format("The most expensive day cost ${}",max(costs)))
print(str.format("The least expensive day cost ${}",min(costs)))
total = sum(costs)
print(str.format("Overall the total trip cost ${}",total))
average = total/delta.days
print(str.format("The average cost per day was ${:.2f}",average))
  

# print most and least expensive days



# calculate and print total cost of the trip



# calculate and print the average cost per day
