from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

ecodelight = CoffeeSite("Eco Delight", "https://ecodelightcoffee.com/", "https://ecodelightcoffee.com/")
roaster_id = getRoasterID(ecodelight.name)
ecodelight.add_class("parentDiv", ("list-grid", "div"))
ecodelight.add_class("coffeeDiv", ("grid-item", "div"));
ecodelight.add_class("title", ("grid-title", "div"));
ecodelight.add_class("price", ("sqs-money-native", "span"));
ecodelight.add_class("desc", (".ProductItem-details-excerpt", "p"));

coffees = scrapeCoffeeSite(ecodelight, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)