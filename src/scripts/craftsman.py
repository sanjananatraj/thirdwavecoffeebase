from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

craftsman = CoffeeSite("Craftsman Coffee", "https://crftsmncoffee.com", "https://crftsmncoffee.com/collections/frontpage")
roaster_id = getRoasterID(craftsman.name)
craftsman.add_class("parentDiv", ("grid__item", "div"))
craftsman.add_class("coffeeDiv", ("product-item-parent", "div"));
craftsman.add_class("title", ("grid__item", "h3"));
craftsman.add_class("price", ("price", "p"));
craftsman.add_class("desc", (".rte", "p"));

coffees = scrapeCoffeeSite(craftsman, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)