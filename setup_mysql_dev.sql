-- Initializes a new database named hbnb_dev_db within the
-- active MySQL server instance.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Establishes a new MySQL server user account named hbnb_test.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants Permissions for user hbnb_test
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
