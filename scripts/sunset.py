from src.scripts.scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

sunset = CoffeeSite("Sunset Roasters", "https://www.sunsetroasters.com", "https://www.sunsetroasters.com/coffeestore")
roaster_id = getRoasterID(sunset.name)
sunset.add_class("parentDiv", ("ProductList-grid", "div"))
sunset.add_class("coffeeDiv", ("ProductList-item", "div"));
sunset.add_class("title", ("ProductList-title", "h1"));
sunset.add_class("price", ("sqs-money-native", "span"));
sunset.add_class("desc", (".ProductItem-details-excerpt", "p"));

coffees = scrapeCoffeeSite(sunset, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)