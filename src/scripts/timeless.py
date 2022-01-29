from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

timeless = CoffeeSite("Timeless Coffee", "https://timelesscoffee.com/", "https://timelesscoffee.com/collections/coffee")
roaster_id = getRoasterID(timeless.name)
timeless.add_class("parentDiv", ("grid_wrapper", "div"))
timeless.add_class("coffeeDiv", ("product-index", "div"));
timeless.add_class("title", ("js-product-details-link", "a"));
timeless.add_class("price", ("price__regular", "div"));
timeless.add_class("desc", (".rte", "div"));

timeless_coffees = scrapeCoffeeSite(timeless, roaster_id, False, 0)

for coffee in timeless_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(timeless_coffees)