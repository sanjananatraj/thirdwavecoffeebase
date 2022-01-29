from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

caffeeroma = CoffeeSite("Caffee Roma", "https://www.cafferoma.com", "https://www.cafferoma.com/shop")
roaster_id = getRoasterID(caffeeroma.name)
caffeeroma.add_class("parentDiv", ("ProductList-grid", "div"))
caffeeroma.add_class("coffeeDiv", ("ProductList-item", "div"));
caffeeroma.add_class("title", ("ProductList-title", "h1"));
caffeeroma.add_class("price", ("sqs-money-native", "span"));
caffeeroma.add_class("desc", (".ProductItem-details-excerpt", "p"));

coffees = scrapeCoffeeSite(caffeeroma, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)