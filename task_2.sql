-- Use the alx_book_store database
USE alx_book_store;

-- Drop tables if they exist to prevent errors
DROP TABLE IF EXISTS order_details;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS customers;

-- Create Authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Create Books table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) -- Author foreign key
);

-- Create Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
);

-- Create Orders table with a foreign key referencing Customers
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT, -- This column references the customer_id in the Customers table
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)  -- Inserted the FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order_Details table with foreign keys referencing Orders and Books
CREATE TABLE IF NOT EXISTS order_details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,  -- This column references the order_id in the Orders table
    book_id INT,   -- This column references the book_id in the Books table
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),  -- Foreign key referencing orders
    FOREIGN KEY (book_id) REFERENCES books(book_id)  -- Foreign key referencing books
);
