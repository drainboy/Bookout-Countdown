"""
A simple python script to display the simple things to bookout

Author: Eldrian
"""


import pendulum
import datetime
from test import *
from datetime import time
from datetime import timedelta
from bookoutitem import Meal
from bookoutitem import Time


BOOKOUTITEMS = {}
TIMEZONE = pendulum.timezone("Asia/Singapore")
TIMEZONED = datetime.timezone(timedelta(hours = 8))
BOOKOUT = {"day":4, "time": time(18,30,00)}
BOOKIN = {"day":6, "time": time(21,00,00)}
DINNER_ON_BOOKOUT = False
WIDTH_SIZE = 51


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
def print_aligning(direction, word):
    direction = direction.lower()
    left_spaces = 0
    half_width = WIDTH_SIZE//2
    if direction in ["centre","middle","center"]:
        left_spaces = (WIDTH_SIZE - len(word))//2
    elif direction in ["left"]:
        if len(word) <= half_width:
            left_spaces = (half_width - len(word))//2
    elif direction in ["right"]:
        left_spaces = half_width
        if len(word) <= half_width:
            left_spaces += (half_width - len(word))//2

    return left_spaces * " " + word


def print_format():
  now = datetime.datetime.now(TIMEZONED)
  num_of_meals_to_bookout = sum([meal.get_value() for meal in BOOKOUTITEMS["Meals"]])
  hours_to_bookout = int(get_timedelta_to(BOOKOUT, now).total_seconds()/60/60)
  
  # Header
  # ==================================================================
  print(print_aligning("centre","BOOKOUT COUNTDOWN"))
  print(print_aligning("centre","Soon Bookout Street"))
  print(print_aligning("centre", "Singapore"))
  print("\n",pendulum.now(TIMEZONE).to_day_datetime_string())
  print("-"*WIDTH_SIZE, "\n")
  
  # Content
  # ==================================================================
  for item in BOOKOUTITEMS:
    print(print_aligning("left",item), "\n")
    for subitem in BOOKOUTITEMS[item]:
      if subitem.get_value() != 0:
          quantifier_left = print_aligning("left", "    "*2+subitem.get_quantifier())
          subitem_right = " " * (WIDTH_SIZE//2 + 4) + subitem.get_name()
          print(quantifier_left, subitem_right[len(quantifier_left):], "\n")
  
  # Summary
  # ==================================================================
  print("-"*WIDTH_SIZE, "\n")
  total_left_aligned = print_aligning("left","Total:")
  num_of_meals_right_aligned = print_aligning("right", f"{str(num_of_meals_to_bookout).zfill(2)} meals")
  print(f"\033[1m{total_left_aligned}{num_of_meals_right_aligned[len(total_left_aligned):]}\033[0m")
  hours_to_bookout_right_aligned = print_aligning('right',f'{str(hours_to_bookout).zfill(2)} hours')
  print(f"\033[1m{hours_to_bookout_right_aligned}\033[0m\n")
  print(print_aligning("centre","You can do it! Ganbatte!!!"))


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