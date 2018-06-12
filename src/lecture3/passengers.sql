
CREATE TABLE passengers
(
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Khan', 10);
INSERT INTO passengers (name, flight_id) VALUES ('Potato', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Ed', 5); 
INSERT INTO passengers (name, flight_id) VALUES ('Samantha', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Tomato', 8);
INSERT INTO passengers (name, flight_id) VALUES ('Jon', 10); 
INSERT INTO passengers (name, flight_id) VALUES ('Eddy', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Sally', 12);
INSERT INTO passengers (name, flight_id) VALUES ('Pam', 10); 
INSERT INTO passengers (name, flight_id) VALUES ('Jim', 13);
INSERT INTO passengers (name, flight_id) VALUES ('Dwight', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Office Mike', 3); 
INSERT INTO passengers (name, flight_id) VALUES ('Prison Mike', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Sal', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Walter', 4); 
