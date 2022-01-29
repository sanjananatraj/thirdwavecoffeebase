from scrape import scrapeCoffeeSite
import sys
sys.path.append('..\db')
sys.path.append('..\classes')
from getRoasterID import getRoasterID
from insertCoffee import insertCoffeeIntoDB
from coffeeSite import CoffeeSite

wrecking_ball = CoffeeSite("Wrecking Ball", "https://www.wreckingballcoffee.com/", "https://www.wreckingballcoffee.com/collections/whole-bean-coffee/")
roaster_id = getRoasterID(wrecking_ball.name)
wrecking_ball.add_class("parentDiv", ("product-grid", "div"));
wrecking_ball.add_class("coffeeDiv", ("product-item", "div"));
wrecking_ball.add_class("title", ("title", "p"));
wrecking_ball.add_class("price", ("price", "p"));
wrecking_ball.add_class("desc", (".rte-content", "div"));

wrecking_ball_coffees = scrapeCoffeeSite(wrecking_ball, roaster_id, False, 0)

for coffees in wrecking_ball_coffees:
  print(coffees)
  print()

#insertCoffeeIntoDB(wrecking_ball_coffees)