from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

reveille = CoffeeSite("Reveille Coffee", "https://www.reveillecoffee.com/", "https://www.reveillecoffee.com/coffee")
roaster_id = getRoasterID(reveille.name)
reveille.add_class("parentDiv", ("sqs-pinterest-products-wrapper", "div"))
reveille.add_class("coffeeDiv", ("product", "a"));
reveille.add_class("title", ("product-title", "div"));
reveille.add_class("price", ("sqs-money-native", "span"));
reveille.add_class("desc", (".product-excerpt", "div"));

coffees = scrapeCoffeeSite(reveille, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)