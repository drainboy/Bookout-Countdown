from main import *
from datetime import time
import pendulum

def test():
  test_get_next_datetime()


def test_get_next_datetime():
  test_timezone = pendulum.timezone("Asia/Singapore")
  test_bookout = {"day":4, "time":time(17,00,00)}
  test_now = datetime.datetime(2020, 10, 12, 12, 00, 00) # 12 October 2020 12pm
  expected_result = pendulum.datetime(2020, 10, 16, 17, 00, 00, tz=test_timezone)
  assert get_next_datetime(test_bookout, test_now) == expected_result