from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

fourbarrel = CoffeeSite("Four Barrel Coffee", "https://www.fourbarrelcoffee.com/", "https://www.fourbarrelcoffee.com/collections/coffee")
roaster_id = getRoasterID(fourbarrel.name)
fourbarrel.add_class("parentDiv", ("medium-9", "div"))
fourbarrel.add_class("coffeeDiv", ("each-coffee", "div"));
fourbarrel.add_class("title", ("product-title-main", "div"));
fourbarrel.add_class("price", ("product-title-sub", "div"));
fourbarrel.add_class("desc", (".flavor", "span"));

coffees = scrapeCoffeeSite(fourbarrel, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)