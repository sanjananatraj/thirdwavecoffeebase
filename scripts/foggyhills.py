from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

foggyhills = CoffeeSite("Foggy Hills Coffee", "https://foggyhillscoffee.com/", "https://foggyhillscoffee.com/collections/roasted-coffee")
roaster_id = getRoasterID(foggyhills.name)
foggyhills.add_class("parentDiv", ("collection-products", "div"))
foggyhills.add_class("coffeeDiv", ("product-list-item", "div"));
foggyhills.add_class("title", ("product-list-item-title", "h3"));
foggyhills.add_class("price", ("money", "span"));
foggyhills.add_class("desc", (".rte", "div"));

coffees = scrapeCoffeeSite(foggyhills, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)