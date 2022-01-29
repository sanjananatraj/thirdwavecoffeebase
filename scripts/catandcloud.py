from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

catandcloud = CoffeeSite("Cat and Cloud", "https://catandcloud.com/", "https://catandcloud.com/collections/coffee")
roaster_id = getRoasterID(catandcloud.name)
catandcloud.add_class("parentDiv", ("collection-products", "div"))
catandcloud.add_class("coffeeDiv", ("product-list-item", "div"));
catandcloud.add_class("title", ("product-list-item-title", "h4"));
catandcloud.add_class("price", ("money", "span"));
catandcloud.add_class("desc", (".product-description", "p"));

coffees = scrapeCoffeeSite(catandcloud, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)