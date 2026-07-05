 CREATE TABLE Users (
     user_id SERIAL PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(255) UNIQUE NOT NULL,
     password_hash VARCHAR(255) NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );

 CREATE TABLE Trips (
     trip_id SERIAL PRIMARY KEY,
     user_id INT NOT NULL,
     title VARCHAR(255) NOT NULL,
     destination VARCHAR(100) NOT NULL,
     start_location VARCHAR(100) NOT NULL,
     travelers INT NOT NULL
         CHECK ( travelers>=1 ),
     start_date DATE NOT NULL,
     end_date DATE NOT NULL,
     CHECK(end_date >= start_date),
     status VARCHAR(20) DEFAULT 'draft'
                   CHECK ( status IN ('draft','planning','confirmed','completed')),
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (user_id)
         REFERENCES Users(user_id)
         ON DELETE CASCADE
 );

CREATE TABLE ItineraryDays(
    day_id SERIAL PRIMARY KEY ,
    trip_id INT NOT NULL,
    day_number INT NOT NULL,
    UNIQUE(trip_id, day_number),
    date DATE NOT NULL,
    notes TEXT,

    FOREIGN KEY (trip_id)
                    REFERENCES Trips(trip_id)
        ON DELETE CASCADE
);

 CREATE TABLE BudgetCategories(
    category_id SERIAL PRIMARY KEY ,
    trip_id INT NOT NULL,
    name VARCHAR(255) NOT NULL
        CHECK ( name IN ('lodging','food','transport','activities','misc')),
    UNIQUE(trip_id, name),
    allocated_amount DECIMAL(10,2) NOT NULL
        CHECK (allocated_amount >= 0),
    spent_amount DECIMAL(10,2) NOT NULL
        CHECK (spent_amount >= 0),
    currency CHAR(3) DEFAULT 'INR' NOT NULL ,

    FOREIGN KEY (trip_id)
      REFERENCES Trips(trip_id)
        ON DELETE CASCADE

 );


 CREATE TABLE ItineraryItems(
     item_id SERIAL PRIMARY KEY ,
     day_id INT NOT NULL,
     category_id INT,
     item_type VARCHAR(20) NOT NULL
         CHECK ( item_type IN ('route','hotel','restaurant','activity')),
     title VARCHAR(100) NOT NULL,
     location VARCHAR(100) NOT NULL,
     start_time TIME NOT NULL,
     end_time TIME NOT NULL
         CHECK(end_time > start_time),
     cost DECIMAL(10,2) NOT NULL
         CHECK ( cost>=0 ),
     source_agent VARCHAR(50) NOT NULL,
     FOREIGN KEY (day_id)
         REFERENCES ItineraryDays(day_id)
         ON DELETE CASCADE,
     FOREIGN KEY (category_id)
         REFERENCES BudgetCategories(category_id)
         ON DELETE CASCADE
 );

 CREATE TABLE Preferences(
     pref_id SERIAL PRIMARY KEY ,
     user_id INT NOT NULL,
     trip_id INT ,
     pref_type  VARCHAR(20) NOT NULL
         CHECK (
         pref_type IN
         (
          'cuisine',
          'pace',
          'accessibility',
          'activity',
          'fears'
             )
         ),
     UNIQUE(user_id, trip_id, pref_type),
     pref_value VARCHAR(255) NOT NULL ,
     FOREIGN KEY (user_id)
          REFERENCES Users(user_id)
         ON DELETE CASCADE,
     FOREIGN KEY (trip_id)
         REFERENCES Trips(trip_id)
         ON DELETE CASCADE
 );

 CREATE TABLE Feedback(
     feedback_id SERIAL PRIMARY KEY ,
     user_id INT NOT NULL,
     trip_id INT NOT NULL ,
     item_id INT,

     UNIQUE(user_id,item_id),


     rating INT NOT NULL CHECK ( rating>=1 AND rating <=5 ),
     comment TEXT,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (user_id)
        REFERENCES Users(user_id)
         ON DELETE CASCADE,
     FOREIGN KEY (trip_id)
        REFERENCES Trips(trip_id)
         ON DELETE CASCADE,
     FOREIGN KEY (item_id)
         REFERENCES ItineraryItems(item_id)
         ON DELETE CASCADE
 );

 CREATE TABLE ChatMessages(
     message_id SERIAL PRIMARY KEY ,
     user_id INT,
     trip_id INT,
     role  VARCHAR(20) NOT NULL
        CHECK ( role IN ('user','agent','system') ),
     agent_name VARCHAR(50),
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     content TEXT NOT NULL,
     FOREIGN KEY (user_id)
         REFERENCES Users(user_id)
         ON DELETE CASCADE,
     FOREIGN KEY (trip_id)
         REFERENCES Trips(trip_id)
         ON DELETE CASCADE
 );


-- Trips
 CREATE INDEX idx_trips_user_id
     ON Trips(user_id);

-- ItineraryDays
 CREATE INDEX idx_itinerary_days_trip_id
     ON ItineraryDays(trip_id);

-- ItineraryItems
 CREATE INDEX idx_itinerary_items_day_id
     ON ItineraryItems(day_id);

 CREATE INDEX idx_itinerary_items_category_id
     ON ItineraryItems(category_id);

-- BudgetCategories
 CREATE INDEX idx_budget_categories_trip_id
     ON BudgetCategories(trip_id);

-- Preferences
 CREATE INDEX idx_preferences_user_id
     ON Preferences(user_id);

 CREATE INDEX idx_preferences_trip_id
     ON Preferences(trip_id);

-- Feedback
 CREATE INDEX idx_feedback_trip_id
     ON Feedback(trip_id);

 CREATE INDEX idx_feedback_user_id
     ON Feedback(user_id);

 CREATE INDEX idx_feedback_item_id
     ON Feedback(item_id);

-- ChatMessages
 CREATE INDEX idx_chat_messages_trip_id
     ON ChatMessages(trip_id);

 CREATE INDEX idx_chat_messages_user_id
     ON ChatMessages(user_id);