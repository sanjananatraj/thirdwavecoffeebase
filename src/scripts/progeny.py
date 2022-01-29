from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

progeny = CoffeeSite("Progeny Coffee", "https://progenycoffee.com/", "https://progenycoffee.com/pages/wholebeans")
roaster_id = getRoasterID(progeny.name)
progeny.add_class("parentDiv", ("shg-row", "div"))
progeny.add_class("coffeeDiv", ("shg-product", "div"));
progeny.add_class("title", ("shg-product-title-component", "div"));
progeny.add_class("price", ("shg-product-price", "span"));
progeny.add_class("desc", (".shg-theme-text-content", "div"));
coffees = scrapeCoffeeSite(progeny, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)