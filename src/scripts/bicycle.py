from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

bicycle = CoffeeSite("Bicycle Coffee", "https://www.bicyclecoffeeco.com", "https://www.bicyclecoffeeco.com/collections/all-items-1")
roaster_id = getRoasterID(bicycle.name)
bicycle.add_class("parentDiv", ("product-list", "div"))
bicycle.add_class("coffeeDiv", ("product-block__title-price", "div"));
bicycle.add_class("title", ("title", "a"));
bicycle.add_class("price", ("theme-money", "span"));
bicycle.add_class("desc", (".product-description", "p"));

coffees = scrapeCoffeeSite(bicycle, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)