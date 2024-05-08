DROP TABLE IF EXISTS players;

CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    position TEXT NOT NULL,
    rank INTEGER
);
