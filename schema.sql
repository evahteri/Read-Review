CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER 
);
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT 
);
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    author_id INTEGER REFERENCES authors ON DELETE CASCADE,
    title TEXT 
);
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books ON DELETE CASCADE,
    review TEXT,
    title TEXT,
    rating INTEGER,
    created_by_id INTEGER REFERENCES users ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);