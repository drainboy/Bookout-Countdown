"""
A script containing common variables and functions

Author: drainboy
Edited: lmoxd
"""
import datetime

TIMEZONE = datetime.timezone(datetime.timedelta(hours = 8))
WIDTH_SIZE = 45


def get_next_datetime(variable, given_datetime):
    """returns the next datetime of bookout or bookin from given datetime"""
    today = given_datetime
    while today.weekday() != variable["day"]:
        today += datetime.timedelta(1)
    the_datetime = datetime.datetime(today.year, today.month, today.day, variable["time"].hour, variable["time"].minute, tzinfo = TIMEZONE)
    return the_datetime


def get_timedelta_to(variable, given_datetime):
    """returns the amount of time until bookout or bookin"""
    bookout_datetime = get_next_datetime(variable, given_datetime)
    now = given_datetime
    the_timedelta = bookout_datetime - now
    return the_timedelta