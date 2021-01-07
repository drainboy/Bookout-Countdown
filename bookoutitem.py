

class BookoutItem:
  def __init__(self, category, *subitems):
    self.category = category
    self.subitem_list = []
    for subitem in subitems:
      self.subitem_list.append(BookoutSubItem(subitem))


class BookoutSubItem:
  def __init__(self, name):
    self.__name = name
    self.__value = 0

  
  def get_quantifier(self):
      return f"{self.get_value()}x"
  
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
  
  def get_quantifier(self):
      return str(self.get_value()).zfill(2)
  
    

  