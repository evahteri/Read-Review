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
    author_id INTEGER REFERENCES authors,
    title TEXT 
);
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    review TEXT,
    rating INTEGER,
    created_by_id INTEGER REFERENCES users,
    created_at TIMESTAMP 
);