import datetime
from .common import WIDTH_SIZE
from .motivation.motivation import get_quote, format_quote

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


def print_format(bookoutitem_list):
  # Header
  # ==================================================================
    print(print_aligning("centre","BOOKOUT COUNTDOWN"))
    print(print_aligning("centre","Soon Bookout Street"))
    print(print_aligning("centre", "Singapore"))
    print("\n",datetime.date.today())
    print("-"*WIDTH_SIZE, "\n")
  
  # Content
  # ==================================================================
    for item in bookoutitem_list:
        if item.get_total() > 0:
            print(item)
  
  # Summary
  # ==================================================================
    print("-"*WIDTH_SIZE, "\n")

    summary_output = "\033[1m" + print_aligning("left","Total:\n")

    for item in bookoutitem_list:
        item_total = item.get_total()
        if item_total:
            item_right_aligned = print_aligning("right",f"{item_total} {item.get_total_variable(item_total)}")
            summary_output += item_right_aligned + "\n"

    print(f"{summary_output}\033[0m")

    for line in format_quote(WIDTH_SIZE,get_quote()):
        print(print_aligning("centre",line))
