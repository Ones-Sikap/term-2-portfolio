#Jacob cook
#Guess my number
#10/28/2019
import random


#functions
def get_num_in_range(rmin,rmax):
     while True:
          num = input("pick a number between " +str(rmin)+ " and " +str(rmax)+"\n")
          if num.isdigit():
               num = int(num)
               if num >= rmin and num <= rmax:
                    return num
               print("not a good num")
#set up program vars
rmin = 1
rmax = 11
               

randNum = random.randint(rmin,rmax)
maxTrys = 3

def game(rmin,rmax,maxTrys):
     Trys = 0

     guess = get_num_in_range(rmin,rmax)
     Trys += 1
#start game loop

     while guess != randNum and Trys != maxTrys:
          if guess > randNum:
               print("guess lower")
          else:
               print("guess higher")
          guess = get_num_in_range(rmin,rmax)
          Trys += 1

#end game loop
     if guess == randNum:
          print("You Win")
     else:
          print("loser")
#to Quit
     print("do you want to quit? yes/no")
     leave = str(input())
     if leave == "yes":
          quit()
     else:
          print("ok")
print("""
     what mode do you want
     1.Easy
     2.Normal
     3.Hard
     """)
mode = input().title()
#options
def options(mode):
     global rmin,rmax,maxTrys
     if str(mode) == "Easy":
          print("Easy Mode")
          
          maxTrys = 7
          rmin = 1
          rmax = 10
     if mode == "Normal":
          print("Normal Mode")
          maxTrys = 6
          rmin = 1
          rmax = 20
     if mode == "Hard":
          print("Hard Mode")
          maxTrys = 5
          rmin = 1
          rmax = 100

options(mode)
game(rmin,rmax,maxTrys)
