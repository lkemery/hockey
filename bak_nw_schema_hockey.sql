DROP TABLE "users";
CREATE TABLE IF NOT EXISTS "users" (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT,
    "password" TEXT
);

INSERT INTO "users" VALUES (1, 'boss', '1234');
INSERT INTO "users" VALUES (2, 'admin', 'password');


CREATE TABLE IF NOT EXISTS "players" (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    "firstname" TEXT,
    "lastname" TEXT,
    "position1" TEXT,
    "position2" TEXT
);

CREATE TABLE IF NOT EXISTS "teams" (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    "team" TEXT,
);

INSERT INTO "teams" VALUES (0, 'red');
INSERT INTO "teams" VALUES (1, 'white');
