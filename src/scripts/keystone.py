from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

keystone = CoffeeSite("Keystone", "https://www.keystonecoffee.com", "https://www.keystonecoffee.com/shop/")
roaster_id = getRoasterID(keystone.name)
keystone.add_class("parentDiv", ("products", "ul"))
keystone.add_class("coffeeDiv", ("product", "li"));
keystone.add_class("title", ("product_title", "h1"));
keystone.add_class("price", ("woocommerce-Price-amount", "span"));
keystone.add_class("desc", (".post-content", "p"));

coffees = scrapeCoffeeSite(keystone, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)