from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

aka = CoffeeSite("AKA Coffee", "https://aka.coffee", "https://aka.coffee/collections/coffee")
roaster_id = getRoasterID(aka.name)
aka.add_class("parentDiv", ("grid--view-items", "ul"))
aka.add_class("coffeeDiv", ("grid__item", "li"));
aka.add_class("title", ("grid-view-item__title", "div"));
aka.add_class("price", ("price-item", "span"));
aka.add_class("desc", (".product-single__description", "p"));

coffees = scrapeCoffeeSite(aka, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)