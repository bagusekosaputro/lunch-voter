CREATE OR REPLACE FUNCTION update_timestamp_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = now();
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255)
);
CREATE INDEX IF NOT EXISTS idx_employees_name ON employees(name);
CREATE INDEX IF NOT EXISTS idx_employees_email ON employees(email);
CREATE TRIGGER update_employees_updated_at_timestamp BEFORE UPDATE
    ON employees FOR EACH ROW EXECUTE PROCEDURE
    update_timestamp_column();

CREATE TABLE IF NOT EXISTS restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    restaurant_code VARCHAR(20) UNIQUE NOT NULL,
    api_key VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255)
);
CREATE INDEX IF NOT EXISTS idx_restaurants_name ON restaurants(name);
CREATE INDEX IF NOT EXISTS idx_restaurants_restaurant_code ON restaurants(restaurant_code);
CREATE INDEX IF NOT EXISTS idx_restaurants_restaurant_api_key ON restaurants(api_key);
CREATE TRIGGER update_restaurants_updated_at_timestamp BEFORE UPDATE
    ON restaurants FOR EACH ROW EXECUTE PROCEDURE
    update_timestamp_column();

CREATE TABLE IF NOT EXISTS menus (
    id SERIAL PRIMARY KEY,
    restaurant_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    menu_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255),
    CONSTRAINT fk_restaurants FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
);
CREATE INDEX IF NOT EXISTS idx_menus_name ON menus(name);
CREATE INDEX IF NOT EXISTS idx_menus_menu_date ON menus(menu_date);
CREATE TRIGGER update_menus_updated_at_timestamp BEFORE UPDATE
    ON menus FOR EACH ROW EXECUTE PROCEDURE
    update_timestamp_column();

CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    menu_id INT NOT NULL,
    employee_id INT NOT NULL,
    vote_point INT,
    vote_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW() NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    updated_by VARCHAR(255),
    CONSTRAINT fk_menus FOREIGN KEY(menu_id) REFERENCES menus(id),
    CONSTRAINT fk_employees FOREIGN KEY(employee_id) REFERENCES employees(id)
);
CREATE INDEX IF NOT EXISTS idx_votes_vote_point ON votes(vote_point);
CREATE INDEX IF NOT EXISTS idx_votes_vote_date ON votes(vote_date);
CREATE TRIGGER update_votes_updated_at_timestamp BEFORE UPDATE
    ON votes FOR EACH ROW EXECUTE PROCEDURE
    update_timestamp_column();
