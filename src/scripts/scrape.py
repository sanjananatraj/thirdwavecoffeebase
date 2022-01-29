# scrape.py
# pass in parameters of coffee info (html classes), return a python list of tuples of coffees
import requests
import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import uuid
import unicodedata

def scrapeCoffeeSite(coffeeSite, roaster_id, multiplePages, maxPages):
  """
    Scrape a coffee website and return a list with the roaster's info, as well as a list of their coffees and info.
    baseURL: baseURL
    URL: specific URL of page that displays all coffees
    parentContainerClass: the class name of the container that contains all of the coffees.
    contentContainerClass: the class name of the container that lists each specific coffee.
    coffeeInfoContainer: located in contentContainerClass, the class name that contains relevant info of every coffee
    titleClass: the class name that has the coffee's title.
    priceClass: the class name that has the coffee's price.
    descClass: the class name that has the coffee's description.

    Note: title, price, desc, are the bare minimum. Website may contain more info - use other methods to handle extra info. 
  
  """
  page = 1 # page counter if there are multiple pages to loop through
  coffeeObjs = []
  if multiplePages:
    while page <= maxPages:
      if page != 1:
        multiURL = coffeeSite.url + "?page=" + str(page)
      else:
        multiURL = coffeeSite.url
      print(multiURL)
      pageURL = requests.get(multiURL)
      if(pageURL.status_code != 200):
        print("Error: HTTP Code", pageURL.status_code)
        return
      
      # coffeeEntries = soupify(coffeeSite.baseURL, pageURL, coffeeSite.classes["parentDiv"][0], coffeeSite.classes["coffeeDiv"][0], coffeeSite.classes["title"][0], coffeeSite.classes["title"][1], coffeeSite.classes["price"][0], coffeeSite.classes["price"][1], coffeeSite.classes["desc"][0], roaster_id)

      coffeeEntries = soupify(roaster_id, coffeeSite.classes, pageURL, coffeeSite.baseURL)
      
      coffeeObjs.extend(coffeeEntries)
      page = page + 1
  else:
    pageURL = requests.get(coffeeSite.url)
    print(coffeeSite.url)
    if(pageURL.status_code != 200):
      print("Error: HTTP Code", pageURL.status_code)
      return
    coffeeEntries = soupify(roaster_id, coffeeSite.classes, pageURL, coffeeSite.baseURL)
    coffeeObjs.extend(coffeeEntries)
    
  return coffeeObjs

# def soupify(baseURL, pageURL, parentContainerClass, contentContainerClass,  titleClass, titleClassType, priceClass, priceClassType, descClass, roaster_id, coffeeDict):

def soupify(roaster_id, coffeeDict, pageURL, baseURL):
  coffeeObjs = []
  soup = BeautifulSoup(pageURL.content, 'html.parser');
  parentContainer = soup.find(coffeeDict["parentDiv"][1], class_= coffeeDict["parentDiv"][0]) # extract div that contains all coffee listings
  print(coffeeDict["parentDiv"][1], coffeeDict["parentDiv"][0], pageURL )
  
  coffeeDivs = parentContainer.find_all(coffeeDict["coffeeDiv"][1], class_= coffeeDict["coffeeDiv"][0]) # get all of the individual cards of the product listings
  if coffeeDivs:
    for coffeeDiv in coffeeDivs:
      coffeeInfo = getCoffeeInfo(baseURL, coffeeDiv, coffeeDict["title"][0], coffeeDict["title"][1], coffeeDict["price"][0], coffeeDict["price"][1])
      coffeeDesc = getCoffeeDescription(coffeeInfo[2], coffeeDict["desc"][0], coffeeDict["desc"][1])
      #coffeePrice = getCoffeePrice(coffeeInfo[2], coffeeDict["price"][0])
      #coffeeTitle = getCoffeeName(coffeeInfo[2], coffeeDict["title"][0])

      coffee_id = "c" + str(uuid.uuid4())[:7] # new coffee id for every coffee under one roaster
      newCoffee = (coffee_id, roaster_id, coffeeInfo[0], float(coffeeInfo[1]), coffeeDesc)
      coffeeObjs.append(newCoffee)
  else:
    print("empty coffeeDivs")
    print(coffeeDivs)
  return coffeeObjs


def getCoffeeInfo(baseURL, coffeeDiv, titleClass, titleClassType, priceClass, priceClassType):
  """
  After getting the html content of each coffee product listing, navigate to coffee product page and extract title & price. Returns tuple of coffee name, price, and link to coffee page.
  """
  coffeeTitleDiv = coffeeDiv.find(titleClassType, class_= titleClass)
  coffeeTitle = ""
  if coffeeTitleDiv:
    coffeeTitle = coffeeTitleDiv.text.strip()
  
  coffeePriceDiv = coffeeDiv.find(priceClassType, class_= priceClass)
  coffeePrice = 0
  if coffeePriceDiv:
    coffeePrice = coffeePriceDiv.text.strip()
    coffeePrice = ''.join(coffeePrice.split())
    coffeePriceRe = re.search('\$\d+(?:\.\d+)?', coffeePrice)
    if coffeePriceRe:
      coffeePrice = coffeePriceRe.group(0).lstrip("$")
    elif not coffeePrice and not coffeePriceRe:
      print("no price")
      coffeePrice = 0
  
  href = coffeeDiv.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+'))
  if href:
    hrefLink = href.attrs['href']
  else: 
    hrefLink = ""
  coffeeLink = baseURL + hrefLink
  # print(baseURL)
  # print(hrefLink)

  return (coffeeTitle, coffeePrice, coffeeLink)

  # coffeeLinks = coffeeDiv.find_all("a"); # find all of the links in the coffeeDiv
  # for coffeeLink in coffeeLinks:
  #   print(coffeeLink.prettify())

def getCoffeeDescription(productLink, descClass, classType):
  session = HTMLSession()
  # print(productLink)
  r = session.get(productLink)
  infoParent = r.html.find(descClass, first=True)
  descString = ""
  if infoParent:
    desc = infoParent.find(classType) # only want paragraph elements in the coffee description
    for d in desc:
      descString = descString + d.text + " "
  descString = cleanDescription(descString)
  return str(descString.strip())

def getCoffeePrice(productLink, priceClass):
  price = 0
  session = HTMLSession()
  r = session.get(productLink)
  priceClassWithSelector = "." + priceClass
  priceDetails = r.html.find(priceClassWithSelector, first=True)
  if priceDetails:
    price = priceDetails.text
    price = ''.join(price.split())
    price = re.search('\$\d+(?:\.\d+)?', price)
    price = price.group(0).lstrip("$")
  return price

def getCoffeeName(productLink, titleClass):
  coffeeTitle = ""
  session = HTMLSession()
  r = session.get(productLink)
  titleClassWithSelector = "." + titleClass
  title = r.html.find(titleClassWithSelector, first=True)
  if title:
    coffeeTitle = title.text.strip()
  return coffeeTitle

def cleanDescription(s):
  s = s.replace("\n", "")
  s = unicodedata.normalize("NFKD", s)
  return s

def getTastingNotes(productLink):
  # once we're at the individual coffee page, attempt to extract tasting notes (if exists)
  tastingNotes = ""
  session = HTMLSession()
  r = session.get(productLink)
  test = r.html.search('Taste {}')[0]
  print(test)



