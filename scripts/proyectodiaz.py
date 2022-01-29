from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

proyectodiaz = CoffeeSite("Proyecto Diaz Coffee", "https://www.proyectodiazcoffee.com", "https://www.proyectodiazcoffee.com/shop?category=Coffee")
roaster_id = getRoasterID(proyectodiaz.name)
proyectodiaz.add_class("parentDiv", ("ProductList-grid", "div"))
proyectodiaz.add_class("coffeeDiv", ("ProductList-item", "div"));
proyectodiaz.add_class("title", ("ProductList-title", "h1"));
proyectodiaz.add_class("price", ("sqs-money-native", "span"));
proyectodiaz.add_class("desc", (".ProductItem-details-excerpt", "div"));
coffees = scrapeCoffeeSite(proyectodiaz, roaster_id, False, 0)

for coffee in coffees:
  print(coffee)
  print()

#insertCoffeeIntoDB(coffees)