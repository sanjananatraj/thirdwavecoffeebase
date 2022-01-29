from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

coffee = CoffeeSite("3-19", "https://319coffee.com/", "https://319coffee.com/collections/bestsellers")
roaster_id = getRoasterID(coffee.name)
coffee.add_class("parentDiv", ("collection__holder", "div"))
coffee.add_class("coffeeDiv", ("site-box", "div"));
coffee.add_class("title", ("overflowed", "span"));
coffee.add_class("price", ("price", "span"));
coffee.add_class("desc", (".rte", "p"));

coffees = scrapeCoffeeSite(coffee, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)