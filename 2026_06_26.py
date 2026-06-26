class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    
  def get_name(self):
    return self.__name
    
  def set_name(self, name):
    if name != "":
      self.__name = name
    else:
      print("wrong value!")

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_name())
print(p1.get_age())

p1.set_name("kirbal")
print(p1.get_name())
p1.set_age(26)
print(p1.get_age())
