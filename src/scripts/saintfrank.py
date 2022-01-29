from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

saintfrank = CoffeeSite("Saint Frank Coffee", "https://www.saintfrankcoffee.com/", "https://www.saintfrankcoffee.com/collections/our-coffees")
roaster_id = getRoasterID(saintfrank.name)
saintfrank.add_class("parentDiv", ("section-collection", "div"))
saintfrank.add_class("coffeeDiv", ("product-list-item", "div"));
saintfrank.add_class("title", ("product-list-item-title", "h3"));
saintfrank.add_class("price", ("money", "span"));
saintfrank.add_class("desc", (".rte", "div"));

saintfrank_coffees = scrapeCoffeeSite(saintfrank, roaster_id, False, 0)

for coffee in saintfrank_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(saintfrank_coffees)