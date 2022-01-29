from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

addictive = CoffeeSite("Addictive Coffee Roasters", "https://addictivecoffee.com", "https://addictivecoffee.com/collections/all-coffee")
roaster_id = getRoasterID(addictive.name)
addictive.add_class("parentDiv", ("ProductList--grid", "div"))
addictive.add_class("coffeeDiv", ("Grid__Cell", "div"));
addictive.add_class("title", ("ProductItem__Title", "h2"));
addictive.add_class("price", ("ProductMeta__Price", "span"));
addictive.add_class("desc", (".p1", "i"));

coffees = scrapeCoffeeSite(addictive, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)