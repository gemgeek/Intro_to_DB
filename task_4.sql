USE alx_book_store;
-- SQL script to describe the Books table in the alx_book_store database.
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS -- <-- THIS LINE WAS CHANGED
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';