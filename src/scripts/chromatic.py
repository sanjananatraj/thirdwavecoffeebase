from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

chromatic = CoffeeSite("Chromatic Coffee", "https://www.chromaticcoffee.com", "https://www.chromaticcoffee.com/all-coffee/")
roaster_id = getRoasterID(chromatic.name)
chromatic.add_class("parentDiv", ("productGrid", "ul"))
chromatic.add_class("coffeeDiv", ("product", "li"));
chromatic.add_class("title", ("card-title", "h3"));
chromatic.add_class("price", ("price", "span"));
chromatic.add_class("desc", ("#tab-description", "p"));

coffees = scrapeCoffeeSite(chromatic, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#nsertCoffeeIntoDB(coffees)