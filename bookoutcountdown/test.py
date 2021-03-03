import datetime
from .common import get_next_datetime


def test():
   test_get_next_datetime()


def test_get_next_datetime():
  test_timezone = datetime.timezone(datetime.timedelta(hours = 8))
  test_bookout = {"day":4, "time":datetime.time(17,00,00)}
  test_now = datetime.datetime(2020, 10, 12, 12, 00, 00) # 12 October 2020 12pm
  expected_result = datetime.datetime(2020, 10, 16, 17, 00, 00, tzinfo=test_timezone)
  assert get_next_datetime(test_bookout, test_now) == expected_result