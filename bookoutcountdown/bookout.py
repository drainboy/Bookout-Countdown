"""
A script containing all bookout related global variable
"""
import datetime
from .classes.Time import Time
from .classes.Meal import Meal

BOOKOUTITEMS = [Time(), Meal()]
BOOKOUT = {"day" : 4, "time" : datetime.time(18,30,00)}
BOOKIN = {"day" : 6, "time" : datetime.time(21,00,00)}