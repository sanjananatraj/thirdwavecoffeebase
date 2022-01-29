from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

blackoak = CoffeeSite("Black Oak Coffee", "https://blackoakcoffee.com", "https://blackoakcoffee.com/collections/all")
roaster_id = getRoasterID(blackoak.name)
blackoak.add_class("parentDiv", ("product-grid", "ul"))
blackoak.add_class("coffeeDiv", ("df", "div"));
blackoak.add_class("title", ("lh-title", "h2"));
blackoak.add_class("price", ("js-variant-price", "div"));
blackoak.add_class("desc", (".mb40", "div"));

coffees = scrapeCoffeeSite(blackoak, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)