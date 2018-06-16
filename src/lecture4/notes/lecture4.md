
# ORM: Object-Relational Modeling
- combines power of classes with sql databases
- use webapp, thus Flask-SQLalchemy

- following 2 codeblocks are same
``` SQL
INSERT INTO flights
  (origin, destination, duration)
  VALUES ('New York', 'Paris', 400);
```

``` python 
flight = Flight(origin='New York', destination='Paris', duration=500)
db.session.add(flight)
```

## select / query
``` SQL
SELECT * FROM flights;
```
``` python 
Flight.query.all()
```
  - example
``` SQL
SELECT * FROM flights WHERE origin='Paris';
```
```python
Flight.query.filter_by(origin='Paris').all()
```

- `.query.first()` will get one
- `.query.count()` will get the number of rows
- `.query.get(id=id)` will get by id number

## update
- example
``` SQL
UPDATE flights SET duration = 80 WHERE id=6; 
```
``` python
flight = Flight.query.get(6)
flight.duration = 80
```

## delete
- example
```SQL
DELTE FROM flights WHERE id=28
```
``` python
flight = Flight.query.get(28)
db.session.delete(flight)
```
- commit 
```SQL COMMIT 
```
``` python 
db.sesion.commit()
```

- ORDER BY > .query.order_by(), by descending -> Flight.origin.desc()
``` SQL
SELECT * FROM flights ORDER BY origin;
```
``` python 
Flight.query.order_by(Flight.origin).all()
```

``` SQL
SELECT * FROM flights WHERE origin != 'Paris';
```
``` python
Flight.query.filter(Flight.origin != 'Paris').all()
```

``` SQL
SELECT * FROM flights WHERE origin LIKE '%a%'
```
``` python 
Flight.query.filter(Flight.origin.like('%a%')).all()
```

- IN 

```SQL
SELECT * FROM flights WHERE origin IN ('Tokyo', 'Paris');
```
``` python 
Flight.query.filter(Flight.origin.in_(['Tokyo', 'Paris'])).all()
```

- AND
``` SQL
SELECT * FROM flights WHERE origin='Paris' AND duration > 500; 
```

``` python 
Flight.query.filter(and_(Flight.origin=='Paris', Flight.duration>500)).all()

- OR
``` SQL
SELECT * FROM flights WHERE origin='Paris' OR duration > 500; 
```

``` python 
Flight.query.filter(or_(Flight.origin=='Paris', Flight.duration>500)).all()

- JOIN
``` SQL
SELECT * FROM flights JOIN passengers
ON flights.id = passengers.id
```

``` python
db.session.query(Flight, Passenger).filter(flight.id == Passenger.flight_id).all()
```

# APIs
- JSON:
  - easy for browsers to interact with json
```JavaScript
{
  "origin": "Tokyo",
  "destination": "Shaghai",
  "duration": 185;
  "passengers": ["Alice", "Bob"]
}
```
- can nest objects
``` JavaScript
{
  "origin": {
    "city": "Tokyo",
    "code": "HND"
  },
  "destination": {
    "city": "Shanghai",
    "code": "PGV"
  },
  "duration": 185,
  "passengers": ["Alice", "Bob"]
}
```
- can interact with the url, 
`/flights/`, `/flights/28`, `/flights/28/passengers`, `/flights/28/passengers/6`
## HTTP Methods
- GET: retrieve resource
- POST: create new resource
- PUT: replace a resource
- PATCH: update a resource
- DELETE: delete a resource
- can do this in python with request library (`pip install requests`)
  - thus do the following: 
  - `requests.get(url)`
  - `requests.post(url)`
  - `requests.put(url)`
  - `requests.patch(url)`
  - `requests.delte(url)`
- STATUS CODES
  - 2?? means sucess
  - 200 OK
  - 201 CREATED
  - 4?? means an error
  - 400 Bad Request
  - 403 Forbidden
  - 404 Not Found
  - 405 Method Not Allowed
  - 422 Unprocessable Entity