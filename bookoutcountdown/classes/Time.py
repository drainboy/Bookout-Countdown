import datetime
from .BookoutItem import BookoutItem, BookoutSubItem
from ..common import TIMEZONE
from ..common import get_timedelta_to


class Time(BookoutItem):
    def __init__(self):
        self.category = "Time"
        self.month = TimeSubItem("Month")
        self.week = TimeSubItem("Week")
        self.day = TimeSubItem("Day")
        self.hour = TimeSubItem("Hour")
        self.minute = TimeSubItem("Minute")
        self.second = TimeSubItem("Second")
        self.total_seconds = 0
        self.subitems = [self.month,self.week, self.day, self.hour, self.minute, self.second]

    def get_total(self):
        return int(self.total_seconds // 3600)

    def update(self, bookout_meta):
        """set time value"""
        now = datetime.datetime.now(TIMEZONE)
        self.total_seconds = get_timedelta_to(bookout_meta, now).total_seconds()
        days = get_timedelta_to(bookout_meta, now).days
        seconds = get_timedelta_to(bookout_meta, now).seconds

        self.week.set_value(days//7)
        self.day.set_value(days - self.week.value * 7)
        self.hour.set_value(int(seconds // 3600))
        self.minute.set_value(int((seconds - self.hour.value * 3600) // 60))
        self.second.set_value(int(seconds - self.hour.value * 3600 - self.minute.value * 60))
    
    def get_total_variable(self, total):
        if total > 1:
            return "hours"
        return "hour"

class TimeSubItem(BookoutSubItem):
    def get_quantifier(self):
        if self.value <= 0:
            return None
        return str(self.value).zfill(2)