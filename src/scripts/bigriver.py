from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

bigriver = CoffeeSite("Big River Coffee", "https://bigrivercoffee.co", "https://bigrivercoffee.co/shop/coffee/")
roaster_id = getRoasterID(bigriver.name)
bigriver.add_class("parentDiv", ("product-listing", "div"))
bigriver.add_class("coffeeDiv", ("item", "div"));
bigriver.add_class("title", ("item", "h3"));
bigriver.add_class("price", ("price", "div"));
bigriver.add_class("desc", ("col-sm-6", "p"));

coffees = scrapeCoffeeSite(bigriver, roaster_id, True, 2)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)