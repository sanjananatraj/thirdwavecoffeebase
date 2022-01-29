from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

avid = CoffeeSite("Avid Coffee", "https://www.avidcoffee.com", "https://www.avidcoffee.com/shop/")
roaster_id = getRoasterID(avid.name)
avid.add_class("parentDiv", ("portfoliolist", "div"))
avid.add_class("coffeeDiv", ("portfolio", "div"));
avid.add_class("title", ("feature-sec", "em"));
avid.add_class("price", ("woocommerce-Price-amount", "span"));
avid.add_class("desc", (".prod-para", "p"));

coffees = scrapeCoffeeSite(avid, roaster_id, False, 0)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)