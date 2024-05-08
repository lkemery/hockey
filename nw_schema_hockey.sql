CREATE TABLE IF NOT EXISTS "users" (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT NOT NULL,
    "password" TEXT
);

CREATE TABLE IF NOT EXISTS "players" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "position1" TEXT,
    "position2" TEXT,
    "rating" INTEGER NOT NULL
);

INSERT INTO "users" VALUES ('1', 'admin', 'password');

INSERT INTO "players" VALUES (1, 'leila', 'kemery', 'defense', 'forward', '2');

