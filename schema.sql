CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    author_id INTEGER REFERENCES authors (id),
    name TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books (id),
    review TEXT,
    rating INTEGER,
    created_by_id INTEGER REFERENCES users (id)
    created_at TIMESTAMP
);