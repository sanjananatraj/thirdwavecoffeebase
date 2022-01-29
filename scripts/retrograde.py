from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

retrograde = CoffeeSite("Retrograde Coffee", "https://www.retrograderoasters.com", "https://www.retrograderoasters.com/store/c3/shop-coffee")
roaster_id = getRoasterID(retrograde.name)
retrograde.add_class("parentDiv", ("wsite-com-category-product-group", "div"))
retrograde.add_class("coffeeDiv", ("wsite-com-category-product", "div"));
retrograde.add_class("title", ("wsite-com-category-product-name", "div"));
retrograde.add_class("price", ("wsite-com-product-price", "div"));
retrograde.add_class("desc", ("#wsite-com-product-short-description", "div"));

coffees = scrapeCoffeeSite(retrograde, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)
