def solution(directions):
  orientation = ["up", "right", "down", "left"] #Set of possible directions the robot can face
  facing = 0 #Robot given an intiial direction facing up
  xcoord = 0
  ycoord = 0 #Initial starting point set to coordinates (0,0)
  min_commands = 0 #Minimum commands required to return to starting point set to 0
  for action in directions: 
    if action == "R":
      if facing == 3:
        facing = 0             
      else:
        facing += 1
                               #For each action in the command given the orientation of the robot is calculated
    if action == "L":
      if facing == 0:
        facing = 3             
      else:
        facing -= 1
    
    if action == "F":
      if orientation[facing] == "up":
        ycoord += 1
      if orientation[facing] == "right":
        xcoord += 1
      if orientation[facing] == "down":         #For each forward action in the command, the new coordinates are calculated
        ycoord -= 1
      if orientation[facing] == "left":
        xcoord -= 1
  
  if xcoord == 0 and ycoord == 0:
    min_commands = 0      
    
    #If the coordinates are equal to the start point i.e zero, the minimum commands required to return to the start point is zero

  elif xcoord <= 0:
    if orientation[facing] == "right":
      if ycoord == 0:
        min_commands = abs(xcoord)
      else:
        min_commands = abs(xcoord) + abs(ycoord) + 1
    else:
      min_commands = abs(xcoord) + abs(ycoord) + 2

  elif xcoord >= 0: 
    if orientation[facing] == "left":
      if ycoord == 0:                    
        min_commands = abs(xcoord)
      else:
        min_commands = abs(xcoord) + abs(ycoord) + 1
    else:
      min_commands = abs(xcoord) + abs(ycoord) + 2

   #Calculates the shortest number of commands to return to start


  if xcoord == 0:
    if orientation[facing] == "down" and ycoord > 0 or orientation[facing] == "up" and ycoord < 0:

      min_commands = abs(ycoord)
    
  return (min_commands)
                
solution("RFFFLF")
     
        

