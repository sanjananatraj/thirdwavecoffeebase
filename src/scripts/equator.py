from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

equator = CoffeeSite("Equator Coffees", "https://www.equatorcoffees.com", "https://www.equatorcoffees.com/collections/coffees")
roaster_id = getRoasterID(equator.name)
equator.add_class("parentDiv", ("product-grid", "div"))
equator.add_class("coffeeDiv", ("product-item", "div"));
equator.add_class("title", ("title", "h3"));
equator.add_class("price", ("price", "span"));
equator.add_class("desc", (".product__iwt-text", "p"));

coffees = scrapeCoffeeSite(equator, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)