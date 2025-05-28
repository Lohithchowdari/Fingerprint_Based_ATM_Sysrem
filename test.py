import mysql.connector

# Connect to Railway MySQL and create the 'atm' database if it doesn't exist
conn = mysql.connector.connect(
    user='root',
    password='KLaftEEZoBvrSelyDyFsQXrgkjYLdmZA',
    host='crossover.proxy.rlwy.net',
    port=26866,
    database='railway',  # Initial DB to connect to; we’ll switch later
    autocommit=True
)
cursor = conn.cursor()

# Create the 'atm' database
cursor.execute("CREATE DATABASE IF NOT EXISTS railway")
print("✅ Database 'atm' created or already exists.")

# Switch to 'atm' database
conn.database = 'railway'

# Create the ATM_database table
create_table_query = """
CREATE TABLE IF NOT EXISTS ATM_database (
  Sr_no INT AUTO_INCREMENT,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  phone_no BIGINT NOT NULL,
  Account_no BIGINT NOT NULL UNIQUE,
  finger_print LONGBLOB NOT NULL,
  Balance INT NOT NULL,
  Transaction TEXT NOT NULL,
  Amount INT NOT NULL,
  Date_Time DATETIME NOT NULL,
  block_status VARCHAR(10) NOT NULL,
  block_time DATETIME,
  PRIMARY KEY(Sr_no)
);
"""  # <- This is now correctly closed

cursor.execute(create_table_query)
print("✅ ATM_database table created successfully.")

# Just checking: run a SELECT to confirm
cursor.execute("SELECT * FROM ATM_database")
print(cursor.fetchall())
