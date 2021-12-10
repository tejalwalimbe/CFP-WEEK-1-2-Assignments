 
import random
class Gambler:
        def __init__(user, start_amount,goal_amount):
          user.start_amount = start_amount
          user.goal_amount = goal_amount

        def CalculateAverage(user):

          countBet = 0
          wincount = 0
          losscount = 0

          while True:
              if user.start_amount == 0 or user.start_amount == user.goal_amount:
                break
              else:
                random_value = int(random.choice([0,1]))
                countBet = countBet + 1
                if random_value == 1:
                  user.start_amount = user.start_amount + 1
                  wincount = wincount + 1
                  print("win",wincount)

                else:
                  user.start_amount = user.start_amount - 1
                  losscount = losscount + 1
                  print("loss",losscount)
              
              return wincount, losscount, countBet

stake_value = int (input("Enter start amount :"))
if stake_value < 0:
  print("please enter positive value")

goal_value = int (input("Enter goal amount :"))
if stake_value < 0:
  print("please enter positive value")

gambler_object = Gambler(stake_value, goal_value)
wincount, losscount, countBet = gambler_object.CalculateAverage()
print("percentage of win count",(wincount/countBet) * 100)
print("percentage of loss count",(losscount/countBet) * 100)
