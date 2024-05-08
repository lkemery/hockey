DROP TABLE "users";
CREATE TABLE IF NOT EXISTS "users" (
    user_id INTEGER PRIMARY KEY,    
    "username" TEXT,
    "password" TEXT
);

INSERT INTO "users" VALUES ('11','test', '1234');
INSERT INTO "users" VALUES ('01', 'admin', 'password');

