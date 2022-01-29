from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

mrespresso = CoffeeSite("Mr. Espresso", "https://mrespresso.com/", "https://mrespresso.com/shop/coffee/")
roaster_id = getRoasterID(mrespresso.name)
mrespresso.add_class("parentDiv", ("products", "ul"))
mrespresso.add_class("coffeeDiv", ("type-product", "li"));
mrespresso.add_class("title", ("product-title", "h3"));
mrespresso.add_class("price", ("woocommerce-Price-currencySymbol", "span"));
mrespresso.add_class("desc", (".woocommerce-product-details__short-description", "div"));

coffees = scrapeCoffeeSite(mrespresso, roaster_id, True, 2)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

# insertCoffeeIntoDB(coffees)