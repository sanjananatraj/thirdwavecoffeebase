from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

ladyfalcon = CoffeeSite("Lady Falcon Coffee Club", "https://www.ladyfalconcoffeeclub.com", "https://www.ladyfalconcoffeeclub.com/collections/frontpage")
roaster_id = getRoasterID(ladyfalcon.name)
ladyfalcon.add_class("parentDiv", ("js-collectionGrid", "div"))
ladyfalcon.add_class("coffeeDiv", ("js-collectionBlock", "div"));
ladyfalcon.add_class("title", ("collectionBlock__title", "h3"));
ladyfalcon.add_class("price", ("collectionBlock__price", "div"));
ladyfalcon.add_class("desc", (".product-description", "p"));

coffees = scrapeCoffeeSite(ladyfalcon, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

#insertCoffeeIntoDB(coffees)