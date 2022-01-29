from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

sunshine = CoffeeSite("Sunshine Coffee", "https://sunshinecoffeeroasters.com/", "https://sunshinecoffeeroasters.com/collections/coffee-beans")
roaster_id = getRoasterID(sunshine.name)
sunshine.add_class("parentDiv", ("grid--uniform", "div"))
sunshine.add_class("coffeeDiv", ("grid__item", "div"));
sunshine.add_class("title", ("product-card__name", "div"));
sunshine.add_class("price", ("product-card__price", "div"));
sunshine.add_class("desc", (".rte", "div"));

sunshine_coffees = scrapeCoffeeSite(sunshine, roaster_id, False, 0)

for coffee in sunshine_coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(sunshine_coffees)