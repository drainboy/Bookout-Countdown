import datetime
from .BookoutItem import BookoutItem, BookoutSubItem
from ..common import TIMEZONE
from ..common import get_timedelta_to, get_next_datetime


class Meal(BookoutItem):
    def __init__(self):
        self.category = "Meal"
        self.breakfast = MealSubItem("Breakfast", datetime.time(6, 30, 0))
        self.lunch = MealSubItem("Lunch", datetime.time(11, 15, 0))
        self.dinner = MealSubItem("Dinner", datetime.time(18, 0, 0), False)
        self.night_snack = MealSubItem("Night Snack", datetime.time(20, 0, 0))
        self.subitems = [self.breakfast, self.lunch, self.dinner, self.night_snack]

    def update(self, bookout_meta):
        """Count the number of meals to bookout_datetime and set meals value"""
        now = datetime.datetime.now(TIMEZONE).replace(minute = 0, second = 0, microsecond = 0)
        hours_to_bookout = int(get_timedelta_to(bookout_meta, now).total_seconds()/3600)
        bookout_datetime = get_next_datetime(bookout_meta, now)

        for hour in range(hours_to_bookout):
            if now.hour in [meal.event_time.hour for meal in self.subitems]:
                for minute in range(0, 60, 5):
                    for meal in self.subitems:
                        if now.time() == meal.event_time:
                            if meal.on_bookout or now.day != bookout_datetime.day:
                                meal.value += 1
                    now += datetime.timedelta(minutes = 5)
            now += datetime.timedelta(hours = 1)

class MealSubItem(BookoutSubItem):
    def __init__(self, name, event_time, on_bookout = True):
        super().__init__(name, on_bookout)
        self.event_time = event_time
    
    def get_grammar_name(self):
        return self.name
 