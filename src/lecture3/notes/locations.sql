CREATE TABLE locations
(
  id SERIAL PRIMARY KEY,
  code VARCHAR NOT NULL,
  name VARCHAR NOT NULL
);

INSERT INTO locations (code, name) VALUES ('LA', 'Los Angeles');
INSERT INTO locations (code, name) VALUES ('NYC', 'New York City'); 
INSERT INTO locations (code, name) VALUES ('TOR', 'Toronto'); 
INSERT INTO locations (code, name) VALUES ('LON', 'London'); 
INSERT INTO locations (code, name) VALUES ('PES', 'Peshawar'); 
INSERT INTO locations (code, name) VALUES ('ND', 'New Deli'); 
INSERT INTO locations (code, name) VALUES ('BHA', 'Bhagdad'); 
INSERT INTO locations (code, name) VALUES ('KYT', 'Kyoto'); 
INSERT INTO locations (code, name) VALUES ('SHA', 'Shang Hai'); 
INSERT INTO locations (code, name) VALUES ('BEG', 'Begin'); 