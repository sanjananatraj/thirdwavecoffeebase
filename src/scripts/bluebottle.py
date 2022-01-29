from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

bluebottle = CoffeeSite("Captain + Stoker", "https://bluebottlecoffee.com/", "https://bluebottlecoffee.com/store/coffee")
roaster_id = getRoasterID(bluebottle.name)
bluebottle.add_class("parentDiv", ("mb40", "div"))
bluebottle.add_class("coffeeDiv", ("df", "div"));
bluebottle.add_class("title", ("lh-title", "h2"));
bluebottle.add_class("price", ("js-variant-price", "div"));
bluebottle.add_class("desc", (".mb40", "div"));

coffees = scrapeCoffeeSite(bluebottle, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)