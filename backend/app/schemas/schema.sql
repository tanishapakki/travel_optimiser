 CREATE TABLE Users (
     user_id SERIAL PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(255) UNIQUE NOT NULL,
     created_at DATE NOT NULL,
 );

 CREATE TABLE Trip (
     trip_id SERIAL PRIMARY KEY,
     user_id SERIAL NOT NULL,
     title VARCHAR(255) NOT NULL,
     destination VARCHAR(100) NOT NULL,
     start_date DATE NOT NULL,
     end_date DATE NOT NULL,
     status VARCHAR(20) DEFAULT 'draft'
                   CHECK ( status IN ('draft','planning','confirmed','completed'))
    created_at DATE NOT NULL,
 )


