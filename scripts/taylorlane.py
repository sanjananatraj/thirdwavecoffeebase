from src.scripts.scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

taylorlane = CoffeeSite("Taylor Lane Organic Coffee", "https://www.taylorlane.com", "https://www.taylorlane.com/collections/coffees")
roaster_id = getRoasterID(taylorlane.name)
print(roaster_id)
taylorlane.add_class("parentDiv", ("boost-pfs-filter-products", "div"))
taylorlane.add_class("coffeeDiv", ("boost-pfs-filter-product-item", "div"));
taylorlane.add_class("title", ("product__title", "h1"));
taylorlane.add_class("price", ("boost-pfs-filter-product-item-regular-price", "span"));
taylorlane.add_class("desc", (".product__entry", "p"));

coffees = scrapeCoffeeSite(taylorlane, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)