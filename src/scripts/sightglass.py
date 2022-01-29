from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

sightglass = CoffeeSite("Sightglass Coffee", "https://sightglasscoffee.com/", "https://sightglasscoffee.com/collections/all")
roaster_id = getRoasterID(sightglass.name)
sightglass.add_class("parentDiv", ("shop-page__container", "section"))
sightglass.add_class("coffeeDiv", ("shop-page_items_shop__box", "div"));
sightglass.add_class("title", ("product-name", "a"));
sightglass.add_class("price", ("price", "p"));
sightglass.add_class("desc", (".product-text", "div"));

sightglass_coffees = scrapeCoffeeSite(sightglass, roaster_id, False, 0)

for coffee in sightglass_coffees:
  print(coffee)
  print()

#insertCoffeeIntoDB(sightglass_coffees)