class CoffeeSite:
  def __init__(self, name, baseURL, coffeeURL):
    self.name = name;
    self.baseURL = baseURL;
    self.url = coffeeURL;
    self.classes = {};

  def add_class(self, classType, className):
    self.classes[str(classType)] = className;

  def get_classes(self):
    return self.classes;