# SQL - CRUD
- `create.sql`
  - creates a table of flights,
  - id: "serial": integer that auto increments, "primary key": will be unique
  - origin: "varchar": text, "not null": can't be blank
  - destination: "varchar": text, "not null": can't be blank
  - duration: "integer": will be an int, "not null": cant be blank
- `\d` will show database
- __constraints__:
  - `NOT NULL`,   `UNIQUE`,  `PRIMARY KEY`, `DEFAULT`, `CHECK`
  
- `insert.sql`, need to use single quotations.
  - add value to a table
  - the columns and their values
  
- `select.sql`, select data based on query
  - use  `WHERE`
  - use equality, `=`
  - use inequality, `>`, `<`
  - use boolean logic, `AND`, `OR`

  - `AVG(duration)`
  - `COUNT(column)` -> get value
  - `MAX(column)`
  - `MIN(column)`
  - `IN` keyword, like `in` keyword in python
  - can also do string matching, use ing `LIKE` keyword
  
- `update.sql`
- `delete.sql`

- LIMIT 2: get only two rows; 
- ORDER BY column ASC; 
- ORDER BY column DESC; 

- get most popular locations
`SELECT origin, COUTN(*) FROM flights GROUP BY origin;`
- `HAVING` is like `WHERE` but it follows the `GROUP BY`. 

## Foreign Key
- define a table exclusively for one thing. 
- the id's of one table relate to the cells of other columns
  - eg: locations table has (id, code, name)
  -     flights table has (id, origin_code, destination_code, duration)
  -     passengers table has (id, flight_code)
  
- `join` query
  - eg: `SELECT * FROM passengers WEHRE name='Jon';`
  -     `SELECT * FROM flights WHERE id=5;`
  
  - two types of join, 
    1. `INNER JOIN` (defualt)
    2. `LEFT JOIN` (if there is no match still get rows back from left table)
    3.   `RIGHT JOIN` (same as left join but on right table)
    
- can create an index on a column and speeds up the lookup on a column. 
- why not do index for all columns? Time and space are used up. 

- Nested Queries
- eg: 
  - `SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;`
  - `SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);`

## Security
- SQL Injection -> think of authentication.
- Race Conditions -. think of users withdrawing $ simultaneously.
- SQL Transactions prevents the race conditions: BEGIN, COMMIT. 