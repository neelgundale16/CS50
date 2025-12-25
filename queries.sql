CREATE TABLE flights (
id INTEGER PRIMARY KEY AUTOINCREMENT,
origin TEXT NOT NULL,
destination TEXT NOT NULL,
duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES     
    ('Delhi', 'Paris', 510),
    ('Tokyo', 'Sydney', 600),
    ('Mumbai', 'Dubai', 190),
    ('Berlin', 'Rome', 120);

SELECT * FROM flights;    