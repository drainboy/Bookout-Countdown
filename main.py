import pendulum
import datetime
from test import *
from datetime import time
from datetime import timedelta
from bookoutitem import Meal
from bookoutitem import Time


BOOKOUTITEMS = {}
TIMEZONE = pendulum.timezone("Asia/Singapore")
BOOKOUT = {"day":4, "time": time(18,30,00)}
BOOKIN = {"day":6, "time": time(21,00,00)}
DINNER_ON_BOOKOUT = False


def init():
  """Initialize BookoutItems at start"""
  breakfast = Meal("Breakfast", time(6, 30, 0))
  lunch = Meal("Lunch", time(11, 15, 0))
  dinner = Meal("Dinner", time(18, 0, 0))
  BOOKOUTITEMS["Meals"] = [breakfast, lunch, dinner]
  
  week = Time("Week")
  day = Time("Day")
  hour = Time("Hour")
  minute = Time("Minute")
  second = Time("Second")
  BOOKOUTITEMS["Time"] = [week, day, hour, minute, second]

  #insert custom BookoutItem here


# get functions
# =============================================================================
def get_next_datetime(variable, given_datetime):
  """returns the next datetime of bookout or bookin from given datetime"""
  now = given_datetime
  while now.weekday() != variable["day"]:
    now += timedelta(1)
  the_datetime = pendulum.datetime(now.year, now.month, now.day, variable["time"].hour, variable["time"].minute, tz=TIMEZONE)
  return the_datetime
  

def get_timedelta_to(variable, given_datetime):
  """returns the amount of time until bookout or bookin"""
  bookout_datetime = get_next_datetime(variable, given_datetime)
  now = given_datetime
  the_timedelta = bookout_datetime - now
  return the_timedelta


# update functions
# ==========================================================================
def update_time_to_bookout(time_list):
  """set time value"""
  now = pendulum.now(TIMEZONE)
  seconds_to_bookout = get_timedelta_to(BOOKOUT, now).seconds
  weeks_to_bookout = get_timedelta_to(BOOKOUT, now).days//7
  days_to_bookout = get_timedelta_to(BOOKOUT, now).days - weeks_to_bookout*7
  hours_to_bookout = int(seconds_to_bookout//60//60)
  minutes_to_bookout = int((seconds_to_bookout - hours_to_bookout*60*60)//60)
  seconds_to_bookout = int(seconds_to_bookout - hours_to_bookout*60*60 - minutes_to_bookout*60)
  update_list = [weeks_to_bookout, days_to_bookout, hours_to_bookout, minutes_to_bookout, seconds_to_bookout]
  for subitem_index in range(len(time_list)):
    time_list[subitem_index].set_value(update_list[subitem_index])


def update_meals_to_bookout(bookout_datetime, meal_list):
  """Count the number of meals to bookout_datetime and set meals value"""
  for meal in meal_list:
    meal.set_value = 0
  now = pendulum.now(TIMEZONE)
  minutes_to_bookout = int(get_timedelta_to(BOOKOUT, now).total_seconds()/60)
  
  for minute in range(minutes_to_bookout):
    for meal in meal_list:
      formatted_time = pendulum.time(now.hour, now.minute, 0)
      if formatted_time == meal.get_time():
        if not (meal.get_name() == "Dinner" and now.day == bookout_datetime.day and not DINNER_ON_BOOKOUT):
          meal.add_value()
        
    now += timedelta(minutes=1)

# insert custom BookoutItem update function here

def update_bookoutitems(bookout_datetime):
  """consolidated function to update all bookoutitems"""
  update_meals_to_bookout(bookout_datetime, BOOKOUTITEMS["Meals"])
  update_time_to_bookout(BOOKOUTITEMS["Time"])
  # insert custom BookoutItem update function name here


# print function
# =========================================================================  
def print_format():
  num_of_meals_to_bookout = sum([meal.get_value() for meal in BOOKOUTITEMS["Meals"]])
  hours_to_bookout = int(get_timedelta_to(BOOKOUT).total_seconds()/60/60)
  
  # Header
  # ==================================================================
  print("\tBOOKOUT COUNTDOWN\n   Soon Bookout Street\n\t\tSingapore\n")
  print(pendulum.now(TIMEZONE).to_day_datetime_string())
  print("-"*30, "\n")
  
  # Content
  # ==================================================================
  for item in BOOKOUTITEMS:
    print(f"\t{item}\n")
    for subitem in BOOKOUTITEMS[item]:
      if subitem.get_value() != 0:
        print(subitem)
  
  # Summary
  # ==================================================================
  print("-"*30, "\n")
  print(f"\033[1m\tTotal:\t\t\t{str(num_of_meals_to_bookout).zfill(2)} meals\033[0m")
  print(f"\033[1m\t\t\t\t\t{str(hours_to_bookout).zfill(2)} hours\033[0m")
  print("\n   You can do it! Ganbatte!!!")


# main functions
# ============================================================================
def main():
  init()
  bookin_datetime = get_next_datetime(BOOKIN, pendulum.now(TIMEZONE))
  bookout_datetime = get_next_datetime(BOOKOUT, pendulum.now(TIMEZONE))
  update_bookoutitems(bookout_datetime)
  if bookin_datetime > bookout_datetime:
    print_format()
  else:
    print("BOOKOUT LOR")


if __name__ == "__main__":
  main()
  test()