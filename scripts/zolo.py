from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

zolo = CoffeeSite("Zolo Coffee", "https://zolocoffee.com", "https://zolocoffee.com/collections/coffees");
zolo.add_class("parentDiv", ("card-list", "div"));
zolo.add_class("coffeeDiv", ("critical-clear", "div"));
zolo.add_class("title", ("card__name", "h3"));
zolo.add_class("price", ("card__price", "div"));
zolo.add_class("desc", (".rte", "div"));

roaster_id = getRoasterID(zolo.name)
zolo_coffees = scrapeCoffeeSite(zolo, roaster_id, True, 2)

for coffees in zolo_coffees:
  print(coffees)
  print()

insertCoffeeIntoDB(zolo_coffees)