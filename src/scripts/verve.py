from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

verve = CoffeeSite("Verve Coffee Roasters", "https://www.vervecoffee.com/", "https://www.vervecoffee.com/collections/all-coffee")
roaster_id = getRoasterID(verve.name)
verve.add_class("parentDiv", ("product-collection", "section"));
verve.add_class("coffeeDiv", ("width--medium-4", "div"));
verve.add_class("title", ("title", "p"));
verve.add_class("price", ("actual-price", "span"));
verve.add_class("desc", (".rte-content", "div"));

verve_coffees = scrapeCoffeeSite(verve, roaster_id, False, 0)

newTitles = []
for coffee in verve_coffees:
  temp = list(coffee)
  title = coffee[2].strip().encode("ascii", "ignore").decode()
  title = ' '.join(title.split())
  print(title)
  temp[2] = title
  coffee = tuple(temp)

for c in verve_coffees:
  print(c)
  print()
