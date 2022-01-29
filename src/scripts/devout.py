from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

devout = CoffeeSite("Devout Coffee", "https://www.devoutcoffee.com", "https://www.devoutcoffee.com/coffee")
roaster_id = getRoasterID(devout.name)
devout.add_class("parentDiv", ("ProductList-grid", "div"))
devout.add_class("coffeeDiv", ("ProductList-item", "div"));
devout.add_class("title", ("ProductList-title", "h1"));
devout.add_class("price", ("sqs-money-native", "span"));
devout.add_class("desc", (".ProductItem-details-excerpt", "p"));

coffees = scrapeCoffeeSite(devout, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)