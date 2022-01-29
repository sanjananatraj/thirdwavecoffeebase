from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

barefoot = CoffeeSite("Barefoot Coffee", "https://www.barefootcoffee.com/", "https://www.barefootcoffee.com/collections/all-coffee")
roaster_id = getRoasterID(barefoot.name)
barefoot.add_class("parentDiv", ("products", "div"))
barefoot.add_class("coffeeDiv", ("alpha", "div"));
barefoot.add_class("title", ("title", "span"));
barefoot.add_class("price", ("price", "span"));
barefoot.add_class("desc", (".description", "div"));

coffees = scrapeCoffeeSite(barefoot, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)