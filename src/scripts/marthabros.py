from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

marthabros = CoffeeSite("Martha & Bros Coffee Company", "https://www.marthabros.com", "https://www.marthabros.com/coffee-beans")
roaster_id = getRoasterID(marthabros.name)
marthabros.add_class("parentDiv", ("ProductList-grid", "div"))
marthabros.add_class("coffeeDiv", ("ProductList-item", "div"));
marthabros.add_class("title", ("ProductList-title", "h1"));
marthabros.add_class("price", ("sqs-money-native", "span"));
marthabros.add_class("desc", (".ProductItem-details-excerpt", "div"));

coffees = scrapeCoffeeSite(marthabros, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)