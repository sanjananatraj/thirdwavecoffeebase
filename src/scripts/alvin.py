from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

alvin = CoffeeSite("Alvin's Coffees", "https://www.alvinsofsf.com", "https://www.alvinsofsf.com/collections/coffee")
roaster_id = getRoasterID(alvin.name)
alvin.add_class("parentDiv", ("grid-collage", "div"))
alvin.add_class("coffeeDiv", ("grid-product", "div"));
alvin.add_class("title", ("title", "span"));
alvin.add_class("price", ("price", "span"));
alvin.add_class("desc", (".description", "div"));

coffees = scrapeCoffeeSite(alvin, roaster_id, True, 3)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)