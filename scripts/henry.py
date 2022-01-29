from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

henry = CoffeeSite("Henry''s House of Coffee", "https://henryshouseofcoffee.com/", "https://henryshouseofcoffee.com/product-category/coffee/")
roaster_id = getRoasterID(henry.name)
henry.add_class("parentDiv", ("products-grid", "ul"))
henry.add_class("coffeeDiv", ("animate", "li"));
henry.add_class("title", ("title", "span"));
henry.add_class("price", ("theme-money", "span"));
henry.add_class("desc", (".product-detail__form__description", "div"));

coffees = scrapeCoffeeSite(henry, roaster_id, True, 2)

if coffees:
  for coffee in coffees:
    print(coffee)
    print()

#insertCoffeeIntoDB(coffees)