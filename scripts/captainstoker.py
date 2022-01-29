from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

captainstoker = CoffeeSite("Captain + Stoker", "https://www.captainandstoker.com", "https://www.captainandstoker.com/coffee")
roaster_id = getRoasterID(captainstoker.name)
captainstoker.add_class("parentDiv", ("ProductList-grid", "div"))
captainstoker.add_class("coffeeDiv", ("ProductList-item", "div"));
captainstoker.add_class("title", ("ProductList-title", "h1"));
captainstoker.add_class("price", ("sqs-money-native", "span"));
captainstoker.add_class("desc", (".ProductItem-details-excerpt", "p"));

coffees = scrapeCoffeeSite(captainstoker, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)