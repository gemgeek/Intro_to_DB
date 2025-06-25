USE alx_book_store;
-- SQL script to insert multiple records into the Customers table in the alx_book_store database.
INSERT INTO customer (
    customer_id,
    customer_name,
    email,
    address
) VALUES
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');