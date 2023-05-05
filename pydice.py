import random
#this is a simple sex dice game that is #usable with 2+ people
Body_Parts = ["lips", "genitals","thigh","neck", "chest","foot"]
Acts = ["suck", "lick", "nibble","caress","kiss","massage"]
Players = ["player1", "player2", "player3"]

def Roll1():
  #i would like to simplify this code please work on yourself 
  rp2 = random.sample(Players, 2)
  Roll_body = random.choice(Body_Parts)
  Roll_act = random.choice(Acts)
  print (rp2)
  print (Roll_act)
  print (Roll_body)
  
Roll1()


