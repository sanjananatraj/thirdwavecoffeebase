from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

catahoula = CoffeeSite("Catahoula Coffee", "https://www.catahoulacoffee.com", "https://www.catahoulacoffee.com/buy-coffee")
roaster_id = getRoasterID(catahoula.name)
catahoula.add_class("parentDiv", ("ProductList-grid", "div"))
catahoula.add_class("coffeeDiv", ("ProductList-item", "div"));
catahoula.add_class("title", ("ProductList-title", "h1"));
catahoula.add_class("price", ("sqs-money-native", "span"));
catahoula.add_class("desc", (".ProductItem-details-excerpt", "div"));

coffees = scrapeCoffeeSite(catahoula, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)