from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

redbay = CoffeeSite("Red Bay Coffee", "https://www.redbaycoffee.com/", "https://www.redbaycoffee.com/collections/coffee")
roaster_id = getRoasterID(redbay.name)
redbay.add_class("parentDiv", ("grid--uniform", "div"))
redbay.add_class("coffeeDiv", ("grid__item", "div"));
redbay.add_class("title", ("name_wrapper", "p"));
redbay.add_class("price", ("price_wrapper", "p"));
redbay.add_class("desc", (".rte", "div"));

coffees = scrapeCoffeeSite(redbay, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

# insertCoffeeIntoDB(coffees)