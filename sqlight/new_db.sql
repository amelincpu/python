-- switches table
CREATE TABLE IF NOT EXISTS switches (
        id integer PRIMARY KEY,
	    hostname text NOT NULL,
        model text,
        ip text
);