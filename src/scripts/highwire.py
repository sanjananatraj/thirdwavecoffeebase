from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

highwire = CoffeeSite("Highwire Coffee Roasters", "https://www.highwirecoffee.com", "https://www.highwirecoffee.com/collections/coffee")
roaster_id = getRoasterID(highwire.name)
highwire.add_class("parentDiv", ("product-list-container", "div"))
highwire.add_class("coffeeDiv", ("product-block", "div"));
highwire.add_class("title", ("title", "span"));
highwire.add_class("price", ("theme-money", "span"));
highwire.add_class("desc", (".product-detail__form__description", "div"));

coffees = scrapeCoffeeSite(highwire, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)