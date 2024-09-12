DROP INDEX IF EXISTS idx_votes_vote_date;
DROP INDEX IF EXISTS idx_votes_vote_point;
DROP TRIGGER IF EXISTS update_votes_updated_at_timestamp ON votes;
DROP TABLE IF EXISTS votes;

DROP INDEX IF EXISTS idx_menus_menu_date;
DROP INDEX IF EXISTS idx_menus_name;
DROP TRIGGER IF EXISTS update_menus_updated_at_timestamp ON menus;
DROP TABLE IF EXISTS menus;

DROP INDEX IF EXISTS idx_restaurants_name;
DROP INDEX IF EXISTS idx_restaurants_restaurant_code;
DROP INDEX IF EXISTS idx_restaurants_restaurant_api_key;
DROP TRIGGER IF EXISTS update_restaurants_updated_at_timestamp ON restaurants;
DROP TABLE IF EXISTS restaurants;

DROP INDEX IF EXISTS idx_employees_email;
DROP INDEX IF EXISTS idx_employees_name;
DROP TRIGGER IF EXISTS update_employees_updated_at_timestamp ON employees;
DROP TABLE IF EXISTS employees;

DROP FUNCTION IF EXISTS update_timestamp_column;