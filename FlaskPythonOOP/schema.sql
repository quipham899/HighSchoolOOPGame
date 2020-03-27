DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
   name TEXT NOT NULL
   strength INT NOT NULL,
   intelligence INT NOT NULL,
   perception INT NOT NULL,
   personality INT NOT NULL,
   endurance INT NOT NULL,
   luck INT NOT NULL
);
