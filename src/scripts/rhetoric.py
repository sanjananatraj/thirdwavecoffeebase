from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

rhetoric = CoffeeSite("Rhetoric Coffee", "https://rhetoriccoffee.com", "https://rhetoriccoffee.com/collections/our-coffee")
roaster_id = getRoasterID(rhetoric.name)
rhetoric.add_class("parentDiv", ("product-list", "div"))
rhetoric.add_class("coffeeDiv", ("prod-block", "div"));
rhetoric.add_class("title", ("title", "div"));
rhetoric.add_class("price", ("product-price__amount", "span"));
rhetoric.add_class("desc", (".product-description", "div"));

coffees = scrapeCoffeeSite(rhetoric, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

#insertCoffeeIntoDB(coffees)