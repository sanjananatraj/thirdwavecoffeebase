from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

tico = CoffeeSite("Tico Coffee Roasters", "https://www.ticoroasters.com/", "https://www.ticoroasters.com/collections/coffee")
roaster_id = getRoasterID(tico.name)
tico.add_class("parentDiv", ("grid-link__container", "div"))
tico.add_class("coffeeDiv", ("grid__item", "div"));
tico.add_class("title", ("grid-link__title", "p"));
tico.add_class("price", ("grid-link__meta", "p"));
tico.add_class("desc", (".smart-tabs-content-block", "div"));

tico_coffees = scrapeCoffeeSite(tico, roaster_id, False, 0)

for coffee in tico_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(tico_coffees)