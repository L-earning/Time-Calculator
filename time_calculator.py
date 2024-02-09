def add_time(start, duration, day=None):

  weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  #split up into pieces
  start_part = ""
  if start.find("PM") != -1:
    start_part = "PM"
  elif start.find("AM") != -1:
    start_part = "AM"
  start_min = int(start.split(":")[1].replace(" "+start_part, ""))
  start_hrs = int(start.split(":")[0])
  
  dura_min = int(duration.split(":")[1])
  dura_hrs = int(duration.split(":")[0])
  
  #error statements
  #invalid start time
  if start_hrs > 12 or start_min > 59:
    return "Error: invalid start time, needs to be in 12-hour clock format"

  #invalid duration (must be in time format (no minutes more than 59) -> hours:minutes
  if dura_min > 59:
    return "Error: invalid duration time, needs to be in hours:minutes"

  #invalid day of the week
  if day is not None:
    if day.capitalize() not in weekdays:
        return "Error: invalid starting day, must either be None or a day in a week"
    
    

  #total minutes 
  minutes = start_min + dura_min
  #how many minutes at the end
  fin_min = ""
  #total hous
  hours = start_hrs + dura_hrs
  
  if minutes >= 60:
    minutes -= 60
    hours += 1

  #adding a 0 before a number if it is below 10 to be in correct format
  fin_min = "0" + str(minutes) if minutes < 10 else str(minutes)

  #ending with AM or PM
  final_part = ""

  #how many days since start
  new_day = 0

  
  if hours < 12:
    final_part = start_part

  #if hours is more than 12, it will need to switch from AM->PM or vice versa
  while hours >= 12:
    #change in hour shift
    if final_part == "":
      if start_part == "AM":
        final_part = "PM"
      elif start_part == "PM":
        final_part = "AM"
        #going from night to morning -> new day
        new_day += 1
    #change in hour shift
    else:
      if final_part == "AM":
        final_part = "PM"
      elif final_part == "PM":
        final_part = "AM"
        #from night to morning -> new day
        new_day += 1
        
    if hours > 12:
      hours -= 12
    #if hours is 12, then break as 12-hour clocks is 1-12 and does not include 00:00
    else:
      break
    


  #format the result into hours:minutes AM/PM
  new_time = f'{str(hours)}:{fin_min} {final_part}'

  #if no day is given, just state how many days after start
  if day is None:
    if new_day == 1:
      new_time += " (next day)"
    elif new_day >1: 
      new_time += f' ({new_day} days later)'
      
  #if day is given, calculate what day as well as hoiw many days after start
  else:
    day = day.capitalize()
    if new_day == 1:
      new_time += f', {weekdays[weekdays.index(day)+new_day]} (next day)'
    elif new_day > 1:
      
      #the starting day (index) plus however many days after duration has been added 
      day_index = new_day + weekdays.index(day)

      #find final day
      while day_index >= 7:
        day_index -= 7 
        
      new_time += f', {weekdays[day_index]} ({new_day} days later)'
      
    #if it's the same day and day is given
    else:
      new_time += f', {day}'
  
  return new_time
