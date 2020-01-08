#Jacob cook
#1/8/2020
#assinment 9
 
import datetime
def get_verified_integer(prompt, min, max):
    while True:
        try:
            inputString = input(prompt)
            inputInt = int(inputString)
            if (inputInt >= min) and (inputInt <= max):
                return inputInt
            else:
                print("try again - ", end ="")
        except:
            print("Try again - ",end="")
 
month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day = get_verified_integer("Please enter today's day (1-31): ",1,31)
year = get_verified_integer("Please enter today's month (2000 - 2030): ",2000,2030)
today = datetime.date(year,month,day)
print("Today is a " + today.strftime("%A"))
 

