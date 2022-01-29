# Third Wave Coffee Base
> Data all about coffees, easily accessible through a RESTful API.

This is a consumption-only API - only the HTTP GET method is available on resources. No authentication is required to access this API, but please help keep hosting costs down by limiting requests and caching data when possible.

# Getting Started

Sample request:
```json
GET https://thirdwavecoffeebase.com/roasters/Sightglass%20Coffee
  {
    "name": "Sightglass Coffee", 
    "location": "San Francisco", 
    "coffees": [
      {
        "name": "Banner Dark", 
        "price": 19.0, 
        "description": "A seasonally rotating blend of fully washed Central and South American coffees sourced for their deep, full-bodied sweetness, attributes which respond beautifully to a more robust roast. Our Banner Dark Blend is meant to appeal to those who enjoy a deeper, richer flavor. Dark chocolate and brown sugar meet rich undertones of vanilla and maple, with a heavier body and lower acidity in the cup.", 
        "origin": "Central America, South America", 
        "type": "blend", 
        "process": "washed", 
        "roastLevel": null, 
        "tastingNotes": [
          "bittersweet cocoa", 
          "toffee", 
          "graham cracker"
        ]
      }, 
      ...
  }
  
```
# API Reference
The base URL is [thirdwavecoffeebase.com](https://thirdwavecoffeebase.com). All endpoints stem from this website itself :)

## Resources
This API has three main endpoints to retrieve data based on different resources: `roasters`, `coffees`, `locations`, and `origins`. You can get data based on a particular roaster, coffee name, or get a list of roasters depending on location.

### `/roasters`
To retrieve a list of all available roasters in the database, request this endpoint without any parameters.

Use `/roasters/<roaster>` to grab data on a specific roaster available in the database, such as Sightglass Coffee above. Spaces must be sent as a `%20` character in the request. 

Each roaster has a unique ID associated with it. If you'd prefer, you can use this id to return the same result `/roasters/<roaster>` does using `/roasters/id/<id>`.

HTTP Request:
```http
GET https://thirdwavecoffeebase.com/roasters/<roaster>
```

Sample Request

With name:
```bash
$ curl https://thirdwavecoffeebase.com/roasters/Rhetoric%20Coffee
```

With ID:
```bash
$ curl https://thirdwavecoffeebase.com/roasters/id/29bb2d35
```

#### RoasterAPIResourceList
| Name  | Description | Type |
| ------------- | ------------- | ------------- |
| id | A unique 8 character [uuid](https://docs.python.org/3/library/uuid.html) pertaining to each roaster in the database.  | *string* |
| name | The name of the third wave coffee roaster. | *string* |
| location | The city the roaster is based in. All roasters are currently from Northern California. | *string* |
| coffees | A list of coffee product listings that the roaster sells. | *list* |

### `/coffees/<coffee>`
Grabs information on a particular coffee by its name. The result would be the same shown in the `coffees[]` array of the `/roasters/<roaster>` endpoint, with information about one product listing instead.

All coffees also have a unique 8 character id associated with them. You can use `/coffees/id/<id>` instead of `/coffees/<coffee>` to return the same output.

HTTP Request:
```http
GET https://thirdwavecoffeebase.com/coffees/<coffee>
```

Sample Request

With name:
```bash
$ curl https://thirdwavecoffeebase.com/coffees/Flying%20Dragon
```

With ID:
```bash
$ curl https://thirdwavecoffeebase.com/coffees/id/ff2b0e6c
```

#### CoffeeAPIResourceList

!> Not all coffee product listings provide all information about the coffee beans. As such, not all of these fields will be populated, and will be **null** instead. A listing without `tastingNotes` returns an empty array.

| Name  | Description | Type |
| ------------- | ------------- | ------------- |
| id | 8 character uuid unique to that coffee. | *string* |
| name | The name of the coffee. | *string* |
| price | Listed price of coffee. If coffee is available in different weights, the 12oz/10z price is listed.  | *integer* |
| description | The description of the coffee, scraped from the roaster's listing. | *string* 
| origin | The origin of the coffee. If the coffee is a *blend*, multiple locations will be listed (can be continent/region/country), separated with commas.  | *string* |
| type | Either *single origin* or *blend*. | *string* 
| process | Either *dry* or *washed*. Specific processes (such as swiss water decaffeination) is not listed at this time.  | *string* |
| roast level | Can be *light, medium,* or *dark*. Mixed roast levels like light-medium is not supported. | *string* 
| tasting notes | Listed tasting notes of that coffee.  | *list* |
| roaster | The roaster where the product listing belongs to. | *string* |

### `/locations`
Calling `/locations` returns a list of available locations that roasters are based in. Use `/locations/<city>` to return a list of roasters based in that city.

HTTP Request:
```http
GET https://thirdwavecoffeebase.com/locations/<city>
```
Sample Request

No params:
```bash
$ curl https://thirdwavecoffeebase.com/locations/
```

With city:
```bash
$ curl https://thirdwavecoffeebase.com/locations/San%20Francisco
```

### `/origins`
Calling `/origins` without any arguments yields a list of available coffee origins in the whole database. From there, use `/origins/<origin>` to return a list of coffees from that location. As of now, only single origin coffees are supported, so coffee blends will not appear.

!> Coffee origins could be the country, region, or continent name. Check out `/origins` for a list of supported origins.

HTTP Request:
```http
GET https://thirdwavecoffeebase.com/origins/<origin>
```

Sample Request

No params:
```bash
$ curl https://thirdwavecoffeebase.com/origins/
```

With origin:
```bash
$ curl https://thirdwavecoffeebase.com/origins/Ethiopia
```

# Tech Stack
This project was built with custom web scraping scripts using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library with [Python](https://www.python.org/). The results were then inputted in a [MySQL](https://www.mysql.com/) relational database. The routing and backend of the API was created using [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/). 

The frontend is generated with [docsify](https://docsify.js.org/#/), specifically with the [docsify-darklight-theme](https://docsify-darklight-theme.boopathikumar.me/#/). 
