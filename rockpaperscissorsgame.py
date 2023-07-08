import random

actions = ["rock","paper","scissors"]

player_1_score = 0
player_2_score = 0

round = int(input("How many rounds you want to play?"))

for i in range(0,round):
   

  player_1 = actions[random.randint(0,2)] 
  player_2 = actions[random.randint(0,2)]

  
  print(player_1)
  print(player_2)


  if player_1 == player_2:
    print(player_1,"-",player_2,"Tie! Both players chose the same action.")
  elif player_1 == "paper" and player_2 == "rock":
    print("player_1 is the winner!")
    player_1_score += 1
  elif player_1 == "paper" and player_2 == "scissors":
    print("player_2 is the winner!")
    player_2_score += 1
  elif player_1 == "scissors" and player_2 == "rock":
    print("player_2 is the winner!")
    player_2_score += 1
  elif player_1 == "scissors" and player_2 == "paper":
    print("player_1 is the winner!")
    player_1_score += 1
  elif player_1 == "rock" and player_2 == "paper":
    print("player_2 is the winner!")
    player_2_score += 1
  elif player_1 == "rock" and player_2 == "scissors":
    print("player_1 is the winner!")
    player_1_score += 1


print(player_1_score)
print(player_2_score)

