from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

souvenir = CoffeeSite("Souvenir Coffee", "https://www.souvenir-coffee.com/", "https://www.souvenir-coffee.com/collections/coffee")
roaster_id = getRoasterID(souvenir.name)
souvenir.add_class("parentDiv", ("grid-uniform", "div"))
souvenir.add_class("coffeeDiv", ("grid__item", "div"));
souvenir.add_class("title", ("grid-product__title", "span"));
souvenir.add_class("price", ("grid-product__price", "span"));
souvenir.add_class("desc", (".rte", "div"));

souvenir_coffees = scrapeCoffeeSite(souvenir, roaster_id, False, 0)

for coffee in souvenir_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(souvenir_coffees)