class Student:
  def __init__(self, name):
      self.__name = name

  @property
  def name(self):
      return self.__name
      
s = Student('Steve')

print(s.name)