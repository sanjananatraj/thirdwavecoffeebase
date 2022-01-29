from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

temple = CoffeeSite("Temple Coffee Roasters", "https://templecoffee.com/", "https://templecoffee.com/collections/coffee")
roaster_id = getRoasterID(temple.name)
temple.add_class("parentDiv", ("collection-products", "div"))
temple.add_class("coffeeDiv", ("o-layout__item", "div"));
temple.add_class("title", ("product__title", "h3"));
temple.add_class("price", ("money", "span"));
temple.add_class("desc", (".product-single__content-text", "div"));

temple_coffees = scrapeCoffeeSite(temple, roaster_id, False, 0)

for coffee in temple_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(temple_coffees)