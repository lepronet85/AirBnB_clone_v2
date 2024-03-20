-- Initializes a new database named hbnb_test_db within the
-- active MySQL server instance.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Establishes a new MySQL server user account named hbnb_test.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Assigns full permissions to the hbnb_test user for the hbnb_test_db database,-- and SELECT permission on the performance_schema database.
GRANT ALL ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
