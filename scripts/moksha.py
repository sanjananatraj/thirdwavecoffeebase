from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

moksha = CoffeeSite("Moksha Coffee", "https://eshop.mokshacoffeeroasting.com", "https://eshop.mokshacoffeeroasting.com/index.php/product-category/coffees/")
roaster_id = getRoasterID(moksha.name)
moksha.add_class("parentDiv", ("product_list", "ul"))
moksha.add_class("coffeeDiv", ("type-product", "li"));
moksha.add_class("title", ("product_title", "h1"));
moksha.add_class("price", ("woocommerce-Price-amount", "span"));
moksha.add_class("desc", ("#tab-description", "p"));

coffees = scrapeCoffeeSite(moksha, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

insertCoffeeIntoDB(coffees)