from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

sextant = CoffeeSite("Sextant Coffee", "https://sextantcoffee.com/", "https://sextantcoffee.com/collections/featured-products")
roaster_id = getRoasterID(sextant.name)
sextant.add_class("parentDiv", ("product-list-container", "div"))
sextant.add_class("coffeeDiv", ("product-block", "div"));
sextant.add_class("title", ("title", "span"));
sextant.add_class("price", ("theme-money", "span"));
sextant.add_class("desc", (".rte", "div"));

sextant_coffees = scrapeCoffeeSite(sextant, roaster_id, False, 0)

for coffee in sextant_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(sextant_coffees)