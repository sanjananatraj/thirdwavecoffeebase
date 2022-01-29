from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

barkingdog = CoffeeSite("Barking Dog Roasters", "https://www.barkingdogroasters.com/", "https://www.barkingdogroasters.com/collections/coffee")
roaster_id = getRoasterID(barkingdog.name)
barkingdog.add_class("parentDiv", ("grid--view-items", "ul"))
barkingdog.add_class("coffeeDiv", ("grid__item", "li"));
barkingdog.add_class("title", ("grid-view-item__title", "div"));
barkingdog.add_class("price", ("price-item", "span"));
barkingdog.add_class("desc", (".product-single__description", "p"));

coffees = scrapeCoffeeSite(barkingdog, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)