from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

petaluma = CoffeeSite("Petaluma Coffee", "https://www.petalumacoffee.com/", "https://www.petalumacoffee.com/coffee/")
roaster_id = getRoasterID(petaluma.name)
petaluma.add_class("parentDiv", ("post-body", "div"))
petaluma.add_class("coffeeDiv", ("vc_row", "div"));
petaluma.add_class("title", ("t-entry-title", "h3"));
petaluma.add_class("price", ("woocommerce-Price-amount", "span"));
petaluma.add_class("desc", (".woocommerce-product-details__short-description", "div"));
coffees = scrapeCoffeeSite(petaluma, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

#insertCoffeeIntoDB(coffees)