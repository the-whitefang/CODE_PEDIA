import pymysql
from pymysql.err import MySQLError

try:

    connection = pymysql.connect(
        host='localhost',
        user='Abhilash',
        password='Abhilash@2002'
    )
    print("Connected to MySQL server.")

    with connection.cursor() as cursor:

        cursor.execute("CREATE DATABASE IF NOT EXISTS Customer_Loan_data")
        print(" Database 'Customer_Loan_data' created or already exists.")

        cursor.execute("USE Customer_Loan_data")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer_data (
            customer_id VARCHAR(20) PRIMARY KEY,
            customer_name VARCHAR(100),
            state VARCHAR(50),
            city VARCHAR(50),
            pin_code VARCHAR(10),
            bank_name VARCHAR(100),
            salary DECIMAL(12,2),
            previous_loan_history TEXT,
            previous_loan_completion BOOLEAN,
            current_loan_requirement DECIMAL(12,2),
            client_property_type VARCHAR(100),
            client_property_location VARCHAR(100),
            property_value_as_per_customer DECIMAL(12,2)
        );
        """
        cursor.execute(create_table_query)
        print("Table 'customer_loans' created successfully!")

    connection.commit()

except MySQLError as e:
    print(f"MySQL Error: {e}")

finally:
    try:
        connection.close()
        print(" MySQL connection closed.")
    except NameError:
        print(" Connection object was never created.")
