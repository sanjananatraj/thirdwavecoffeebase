from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

mclaughlin = CoffeeSite("McLaughlin Coffee", "https://www.mclaughlincoffee.com", "https://www.mclaughlincoffee.com/collections/products")
roaster_id = getRoasterID(mclaughlin.name)
mclaughlin.add_class("parentDiv", ("grid-uniform", "div"))
mclaughlin.add_class("coffeeDiv", ("grid__item", "div"));
mclaughlin.add_class("title", ("grid-product__title", "span"));
mclaughlin.add_class("price", ("grid-product__price", "span"));
mclaughlin.add_class("desc", (".rte", "div"));

coffees = scrapeCoffeeSite(mclaughlin, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)