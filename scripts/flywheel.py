from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

flywheel = CoffeeSite("Flywheel Coffee Roasters", "https://flywheelcoffee.com", "https://flywheelcoffee.com/collections/coffee")
roaster_id = getRoasterID(flywheel.name)
flywheel.add_class("parentDiv", ("clear-after--lg-3", "div"))
flywheel.add_class("coffeeDiv", ("col-sm-12", "div"));
flywheel.add_class("title", ("product-partial--title", "h3"));
flywheel.add_class("price", ("product-partial--price", "h4"));
flywheel.add_class("desc", (".product-description", "p"));

coffees = scrapeCoffeeSite(flywheel, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)