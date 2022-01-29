from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

roastco = CoffeeSite("RoastCo", "https://www.roastco.com", "https://www.roastco.com/collections/all")
roaster_id = getRoasterID(roastco.name)
roastco.add_class("parentDiv", ("main", "div"))
roastco.add_class("coffeeDiv", ("one-third", "div"));
roastco.add_class("title", ("title", "span"));
roastco.add_class("price", ("current_price", "span"));
roastco.add_class("desc", (".description", "p"));

coffees = scrapeCoffeeSite(roastco, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)