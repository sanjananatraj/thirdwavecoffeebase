from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

ohm = CoffeeSite("Ohm Coffee Roasters", "https://www.ohmcoffee.com", "https://www.ohmcoffee.com/collections/blends")
roaster_id = getRoasterID(ohm.name)
ohm.add_class("parentDiv", ("product-list", "div"))
ohm.add_class("coffeeDiv", ("product-wrap", "div"));
ohm.add_class("title", ("title", "span"));
ohm.add_class("price", ("money", "span"));
ohm.add_class("desc", (".description", "div"));

coffees = scrapeCoffeeSite(ohm, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)
