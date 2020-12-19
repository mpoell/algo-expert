"""
Imagine that you want to schedule a meeting of a certain
duration with a co-worker. You have access to your calendar
and your co-worker's calendar (both of which contain your 
respective meetings for the day, in the form of [start_time, 
end_time]), as well as both of your daily bounds (ie earliest
and lastest times at which you're available for meetings every
day) in the form of [earliest_time, latest_time])

Write a function that takes in your calendar, your daily bounds,
your co-worker's calendar, your co-worker's daily bounds, and 
the duration of the meeting that you want to schedule, and that 
returns a list of all the time blocks (in the form of [start_time,
end_time]) during which you could schedule the meeting, ordered
from earliest time block to latest.

Note that times will be given and should be returned in military time.
For example: 8:30, 9:01, and 23:56
"""


def calendar_matching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration):
  updated_calendar1 = update_calendar(calendar1, daily_bounds1)
  updated_calendar2 = update_calendar(calendar2, daily_bounds2)
  merged_calendar = merge_calendars(updated_calendar1, updated_calendar2)
  flattened_calendar = flatten_calendar(merged_calendar)
  return get_matching_availabilities(flattened_calendar, meeting_duration)


def update_calendar(calendar, daily_bounds):
  updated_calendar = calendar[:]
  updated_calendar.insert(0, ["0:00", daily_bounds[0]])
  updated_calendar.append([daily_bounds[1], "29:59"])
  return list(map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], updated_calendar))


def merge_calendars(calendar1, calendar2):
  merged_calendar = []
  i, j = 0, 0
  while i < len(calendar1) and j < len(calendar2):
    meeting1, meeting2 = calendar1[i], calendar2[j]
    if meeting1[0] < meeting2[0]:
      merged_calendar.append(meeting1)
      i += 1
    else:
      merged_calendar.append(meeting2)
      j += 1
  while i < len(calendar1):
    merged_calendar.append(calendar1[i])
    i += 1
  while j < len(calendar2):
    merged_calendar.append(calendar2[j])
    j += 1
  return merged_calendar 


def flatten_calendar(calendar):
  flattened = [calendar[0][:]]
  for i in range(1, len(calendar)):
    current_meeting = calendar[i]
    previous_meeting = flattened[-1]
    current_start, current_end = current_meeting
    previous_start, previous_end = previous_meeting
    if previous_end >= current_start:
      new_previous_meeting = [previous_start, max(previous_end, current_end)]
      flattened[-1] = new_previous_meeting
    else:
      flattened.append(current_meeting[:])
  return flattened

def get_matching_availabilities(calendar, meeting_duration):
  matching_availabilities = []
  for i in range(1, len(calendar)):
    start = calendar[i - 1][1]
    end = calendar[i][0]
    duration = end - start
    if duration >= meeting_duration:
      matching_availabilities.append([start, end])
    return list(map(lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])], matching_availabilities))


def time_to_minutes(time):
  hours, minutes = list(map(int, time.split(":")))
  return hours * 60 + minutes


def minutes_to_time(minutes):
  hours = minutes // 60
  minutes = minutes % 60
  hours_string = str(hours)
  minutes_string = "0" + str(minutes) if minutes < 10 else str(minutes)
  return hours_string + ":" + minutes_string



def main():
  calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
  daily_bounds1 = ["9:00", "20:00"]
  calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
  daily_bounds2 = ["10:00", "18:30"]
  meeting_duration = 30

  print(calendar_matching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration))

if __name__ == "__main__":
  main()

