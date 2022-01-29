from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

ritual = CoffeeSite("Ritual Coffee Roasters", "https://ritualcoffee.com/", "https://ritualcoffee.com/collection/coffee/")
roaster_id = getRoasterID(ritual.name)
ritual.add_class("parentDiv", ("products", "ul"))
ritual.add_class("coffeeDiv", ("product", "li"));
ritual.add_class("title", ("title", "h5"));
ritual.add_class("price", ("amount", "span"));
ritual.add_class("desc", (".description", "div"));

coffees = scrapeCoffeeSite(ritual, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)