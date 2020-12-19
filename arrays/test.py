

calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]

daily_bounds1 = ["9:00", "20:00"]

calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]

daily_bounds2 = ["10:00", "18:30"]

meeting_duration = 30

# print(daily_bounds1[0][1]) #Single digit hour if 
# print(daily_bounds1[0][:2]) #First two
# print(daily_bounds1[0][-2:]) #Last two

def convert_to_int(time):
  if time[1] == ":":
    hour = int(time[0])
  elif time[2] == ":":
    hour = int(time[:2])
  return hour + float(time[-2:]) / 60

print([[convert_to_int(timeframe[0]), convert_to_int(timeframe[1])] for timeframe in calendar1]) 


def convert_to_string(array):
  pass
  