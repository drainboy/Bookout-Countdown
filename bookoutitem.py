class BookoutItem:
  def __init__(self, category, *subitems):
    self.category = category
    self.subitem_list = []
    for subitem in subitems:
      subitem_list.append(BookoutSubItem(subitem))


class BookoutSubItem:
  def __init__(self, name):
    self.__name = name
    self.__value = 0
    
  def __str__(self):
    return f"\t\t{self.get_value()}x\t\t{self.get_name()}\n"
  
  
  def get_name(self):
    return self.__name
    
    
  def get_value(self):
    return self.__value
  
  
  def add_value(self):
    self.__value += 1
    
    
  def set_value(self, value):
    self.__value = value
    

class Meal(BookoutSubItem):
  def __init__(self, name, time):
    BookoutSubItem.__init__(self, name)
    self.__time = time
  
  
  def get_time(self):
    return self.__time
    
    
class Time(BookoutSubItem):
  def __init__(self, name):
    BookoutSubItem.__init__(self, name)
  
  def __str__(self):
    name = self.get_name()
    value = self.get_value()
    if value > 1:
      name += "s"
    return f"\t\t{value}\t\t{name}\n"
  
    

  