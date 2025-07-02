import pandas as pd
import pymysql
from pymysql.err import MySQLError

df = pd.read_csv("loan_data_1.csv")

df['previous_loan_completion'] = df['previous_loan_completion'].map({'Yes': True, 'No': False})

try:
    print("Connecting to MySQL. . . .")
    connection = pymysql.connect(
        host='localhost',
        user='Abhilash',
        password='Abhilash@2002',
        database='Customer_Loan_data',
        autocommit=False
    )

    print("Connected to MySQL.")

    with connection.cursor() as cursor:
        insert_query= """
            INSERT INTO customer_data(
                customer_id, customer_name, state, city, pin_code,
                bank_name, salary, previous_loan_history, previous_loan_completion,
                current_loan_requirement, client_property_type,
                client_property_location, property_value_as_per_customer
            ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data_to_insert = [tuple(row) for row in df.itertuples(index=False)]

        batch_size = 1000
        for i in range(0, len(data_to_insert), batch_size):
            batch = data_to_insert[i: i + batch_size]
            cursor.executemany(insert_query, batch)
            connection.commit()
            print(f"Inserted batch {i // batch_size + 1}")

    print("All Records inserted Successfully!")

except MySQLError as e:
    print(f"MySQL Error: {e}")

finally:
    try:
        connection.close()
        print("MySQL connection is closed.")
    except NameError:
        print("Connection was not established.")
