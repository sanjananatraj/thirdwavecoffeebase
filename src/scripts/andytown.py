from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

andytown = CoffeeSite("Andytown Coffee Roasters", "https://www.andytownsf.com", "https://www.andytownsf.com/purchase?category=Coffee")
roaster_id = getRoasterID(andytown.name)
andytown.add_class("parentDiv", ("ProductList-grid", "div"))
andytown.add_class("coffeeDiv", ("ProductList-item", "div"));
andytown.add_class("title", ("ProductList-title", "h1"));
andytown.add_class("price", ("sqs-money-native", "span"));
andytown.add_class("desc", (".ProductItem-details-excerpt", "p"));

coffees = scrapeCoffeeSite(andytown, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)