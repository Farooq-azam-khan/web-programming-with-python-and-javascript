 -- select everything from table
SELECT * FROM flight; 

-- Get particular column/s
SELECT origin, destination FROM flights; 

-- Get particular row/s
SELECT * FROM flights WHERE id=1; 

-- Use inequality
SELECT * FROM flights WHERE duration>1000; 

-- Use boolean logic
SELECT * FROM flights WHERE origin='Toronto' OR origin='New York';

-- Get the avegrage of a number
SELECT AVG(duration) FROM flights; 

-- Get avg of only origin='Toronto'
SELECT AVG(duration) FROM flights WHERE origin='Toronto'; 

-- Get the count of rows
SELECT COUNT(*) FROM flights; 

-- Get count based on WEHRE
SELECT COUNT(*) FROM flights WHERE origin='Toronto';

-- IN keyword
SELECT * FROM flights WHERE origin IN ('New York', 'Toronto'); 

-- String matching: 
-- return any row where in column origin there is a letter with 'a'
SELECT * FROM flights WHERE origin LIKE '%a%'; 