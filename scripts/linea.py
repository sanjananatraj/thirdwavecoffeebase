from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

linea = CoffeeSite("Linea Caffe", "https://lineacaffe.com/", "https://lineacaffe.com/shop/coffee/")
roaster_id = getRoasterID(linea.name)
linea.add_class("parentDiv", ("product-grid", "div"))
linea.add_class("coffeeDiv", ("product_column", "div"));
linea.add_class("title", ("product_title", "div"));
linea.add_class("price", ("woocommerce-Price-amount", "span"));
linea.add_class("desc", (".product_summary", "div"));

coffees = scrapeCoffeeSite(linea, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)