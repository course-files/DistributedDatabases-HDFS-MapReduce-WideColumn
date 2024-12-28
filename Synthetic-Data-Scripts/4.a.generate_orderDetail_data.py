import mysql.connector
import random

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='student',
    password='5trathm0re',
    database='siwaka_dishes'
)
cursor = conn.cursor()

# Fetch existing customerOrder, customers, and products
cursor.execute("SELECT orderNumber FROM customerOrder")
customerOrder = cursor.fetchall()

cursor.execute("SELECT productCode FROM product")
products = cursor.fetchall()

# Function to generate random order details
def generate_order_details():
    for order in customerOrder:
        orderNumber = order[0]
        num_order_details = random.randint(1, 7)
        
        for _ in range(num_order_details):
            productCode = random.choice(products)[0]
            quantity = random.randint(1, 10)

            cursor.execute("SELECT sellingPrice FROM product WHERE productCode = %s", (productCode,))
            sellingPrice = cursor.fetchone()[0]
            
            cursor.execute("""
                INSERT INTO orderDetail (orderNumber, productCode, quantityOrdered, priceEach)
                VALUES (%s, %s, %s, %s)
            """, (orderNumber, productCode, quantity, sellingPrice))

            with open('./Synthetic-Data-Scripts/4.b.DML_orderDetail_data.sql', 'a') as f:
                f.write(cursor.statement + ';\n')

# Generate and insert order details
generate_order_details()

# Commit the transaction and close the connection
conn.commit()
conn.close()