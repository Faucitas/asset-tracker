CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT UNIQUE 
);

CREATE TABLE exchanges (
    exchange_id SERIAL PRIMARY KEY,
    exchange_name TEXT NOT NULL UNIQUE
);

CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    account_name TEXT NOT NULL UNIQUE ,
    account_type TEXT NOT NULL,
    exchange_id INT NOT NULL,
    user_id INT NOT NULL UNIQUE
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    date_time TIMESTAMP NOT NULL,
    transactions_type TEXT NOT NULL,
    account_id INT NOT NULL UNIQUE
);

CREATE TABLE transaction_details (
    transaction_id INT NOT NULL,
    asset_id INT NOT NULL,
    strategy_id INT,
    amount FLOAT NOT NULL,
    fee FLOAT,
    PRIMARY KEY (transaction_id, asset_id)
);

CREATE TABLE strategies (
    strategy_id SERIAL PRIMARY KEY,
    strategy_name TEXT NOT NULL UNIQUE,
    stragegy_rules TEXT NOT NULL
);

CREATE TABLE assets (
    asset_id SERIAL PRIMARY KEY,
    asset_type TEXT NOT NULL,
    asset_name TEXT NOT NULL UNIQUE,
    asset_symbol CHAR(8) UNIQUE
);

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_exchanges
FOREIGN KEY (exchange_id)
REFERENCES exchanges;

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_users
FOREIGN KEY (user_id)
REFERENCES exchanges;

ALTER TABLE transactions
ADD CONSTRAINT fk_transactions_accounts
FOREIGN KEY (account_id)
REFERENCES accounts;

ALTER TABLE transaction_details
ADD CONSTRAINT fk_transaction_details_transactions
FOREIGN KEY (transaction_id)
REFERENCES transactions;

ALTER TABLE transaction_details
ADD CONSTRAINT fk_transaction_details_assets
FOREIGN KEY (asset_id)
REFERENCES assets;
