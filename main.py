"""
A simple python script to display the simple things to bookout

Author: drainboy
"""


from datetime import datetime
import bookoutcountdown.print_util as print_util
from bookoutcountdown.test import test
from bookoutcountdown.common import TIMEZONE
from bookoutcountdown.bookout import BOOKOUTITEMS, BOOKOUT, BOOKIN
from bookoutcountdown.common import get_next_datetime


def update_bookoutitems(bookout_datetime):
    """BookoutItems initializer"""
    for item in BOOKOUTITEMS:
        item.update(BOOKOUT)


def main():
    bookin_datetime = get_next_datetime(BOOKIN, datetime.now(TIMEZONE))
    bookout_datetime = get_next_datetime(BOOKOUT, datetime.now(TIMEZONE))
    
    update_bookoutitems(bookout_datetime)

    if bookin_datetime > bookout_datetime:
        print_util.print_format(BOOKOUTITEMS)
    else:
        print("BOOKOUT LOR")


if __name__ == "__main__":
    test()
    main()