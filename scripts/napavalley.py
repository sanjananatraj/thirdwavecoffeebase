from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

napavalley = CoffeeSite("Napa Valley Coffee", "https://napavalleycoffee.com", "https://napavalleycoffee.com/fresh-roasted-coffee")
roaster_id = getRoasterID(napavalley.name)
napavalley.add_class("parentDiv", ("ProductList-grid", "div"))
napavalley.add_class("coffeeDiv", ("ProductList-item", "div"));
napavalley.add_class("title", ("ProductList-title", "h1"));
napavalley.add_class("price", ("sqs-money-native", "span"));
napavalley.add_class("desc", (".ProductItem-details-excerpt", "div"));

coffees = scrapeCoffeeSite(napavalley, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

insertCoffeeIntoDB(coffees)
