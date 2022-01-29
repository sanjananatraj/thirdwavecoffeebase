from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

peerless = CoffeeSite("Peerless Coffee", "https://www.peerlesscoffee.com/", "https://www.peerlesscoffee.com/products/all-coffee/")
roaster_id = getRoasterID(peerless.name)
peerless.add_class("parentDiv", ("columns-4", "ul"))
peerless.add_class("coffeeDiv", ("product", "li"));
peerless.add_class("title", ("woocommerce-loop-product__title", "h2"));
peerless.add_class("price", ("woocommerce-Price-amount", "span"));
peerless.add_class("desc", (".summary", "div"));

coffees = scrapeCoffeeSite(peerless, roaster_id, True, 3)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)