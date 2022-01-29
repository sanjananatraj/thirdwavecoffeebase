from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

soulwork = CoffeeSite("Soul Work Coffee", "https://www.soulworkcoffee.com/", "https://www.soulworkcoffee.com/collections/all-day-every-day")
roaster_id = getRoasterID(soulwork.name)
soulwork.add_class("parentDiv", ("products", "div"))
soulwork.add_class("coffeeDiv", ("column", "div"));
soulwork.add_class("title", ("title", "span"));
soulwork.add_class("price", ("price", "span"));
soulwork.add_class("desc", (".description", "div"));

soulwork_coffees = scrapeCoffeeSite(soulwork, roaster_id, False, 0)

for coffee in soulwork_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(soulwork_coffees)