from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

nomadic = CoffeeSite("Nomadic Coffee", "https://nomadiccoffee.com", "https://nomadiccoffee.com/collections/frontpage")
roaster_id = getRoasterID(nomadic.name)
nomadic.add_class("parentDiv", ("site-box-container", "div"))
nomadic.add_class("coffeeDiv", ("box__collection", "div"));
nomadic.add_class("title", ("overflowed", "span"));
nomadic.add_class("price", ("price", "span"));
nomadic.add_class("desc", (".rte", "div"));

coffees = scrapeCoffeeSite(nomadic, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)
