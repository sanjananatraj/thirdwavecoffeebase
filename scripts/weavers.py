from src.scripts.scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

weaver = CoffeeSite("Weavers Coffee & Tea", "https://weaverscoffee.com", "https://weaverscoffee.com/collections/buy-coffee")
roaster_id = getRoasterID(weaver.name)
print(roaster_id)
weaver.add_class("parentDiv", ("grid--view-items", "div"))
weaver.add_class("coffeeDiv", ("grid__item", "div"));
weaver.add_class("title", ("grid-view-item__title", "div"));
weaver.add_class("price", ("product-price__price", "span"));
weaver.add_class("desc", (".rte", "p"));

coffees = scrapeCoffeeSite(weaver, roaster_id, True, 4)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)