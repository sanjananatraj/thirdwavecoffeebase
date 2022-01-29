from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

naked = CoffeeSite("Naked Coffee", "https://nakedcoffee.net/", "https://nakedcoffee.net/collections/coffees")
roaster_id = getRoasterID(naked.name)
naked.add_class("parentDiv", ("tt-product-listing", "div"))
naked.add_class("coffeeDiv", ("tt-col-item", "div"));
naked.add_class("title", ("tt-title", "h2"));
naked.add_class("price", ("tt-price", "div"));
naked.add_class("desc", (".tt-collapse-content", "div"));

coffees = scrapeCoffeeSite(naked, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)
