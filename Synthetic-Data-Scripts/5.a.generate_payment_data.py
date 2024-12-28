import mysql.connector
import random
import decimal
from datetime import datetime, timedelta

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='student',
    password='5trathm0re',
    database='siwaka_dishes'
)
cursor = conn.cursor()

# Fetch existing customerOrder and payment methods
cursor.execute("SELECT orderNumber, orderDate FROM customerOrder")
customerOrders = cursor.fetchall()

cursor.execute("SELECT paymentMethodID FROM paymentMethod")
paymentMethods = cursor.fetchall()

# Function to generate random payments
def generate_payments():
    def random_date(start, end):
        """Generate a random datetime between start and end dates."""
        delta = end - start
        random_seconds = random.randint(0, int(delta.total_seconds()))
        return start + timedelta(seconds=random_seconds)

    end_date = datetime(2024, 12, 8)

    for order in customerOrders:
        orderNumber, orderDate = order
        
        # Calculate the total amount expected for the order
        cursor.execute("""
            SELECT SUM(quantityOrdered * priceEach)
            FROM orderDetail
            WHERE orderNumber = %s
        """, (orderNumber,))
        total_amount_expected = cursor.fetchone()[0]
        
        if total_amount_expected is None:
            continue
        
        # Generate 1 to 5 payments
        num_payments = random.randint(1, 5)
        total_amount_paid = 0
        
        for _ in range(num_payments):
            paymentMethodID = random.choice(paymentMethods)[0]
            remaining_amount = decimal.Decimal(total_amount_expected) - decimal.Decimal(total_amount_paid)
            max_payment = remaining_amount if _ == num_payments - 1 else remaining_amount * decimal.Decimal(random.uniform(0.1, 0.5))
            amount_paid = round(random.uniform(float(remaining_amount) * 0.1, float(max_payment)), 2)
            total_amount_paid += amount_paid
            
            # Generate random payment date on or after the order date
            payment_date = random_date(orderDate, end_date)
            
            cursor.execute("""
                INSERT INTO payment (orderNumber, paymentMethodID, amount, paymentDate)
                VALUES (%s, %s, %s, %s)
            """, (orderNumber, paymentMethodID, amount_paid, payment_date))
            
            with open('./Synthetic-Data-Scripts/4.b.DML_payment_data.sql', 'a') as f:
                f.write(cursor.statement + ';\n')
        
        # Ensure total amount paid is between 80% and 100% of the total amount expected
        if total_amount_paid < total_amount_expected * decimal.Decimal('0.8'):
            additional_payment = total_amount_expected * decimal.Decimal('0.8') - decimal.Decimal(total_amount_paid)
            paymentMethodID = random.choice(paymentMethods)[0]
            
            # Generate random payment date on or after the order date
            payment_date = random_date(orderDate, end_date)
            
            cursor.execute("""
                INSERT INTO payment (orderNumber, paymentMethodID, amount, paymentDate)
                VALUES (%s, %s, %s, %s)
            """, (orderNumber, paymentMethodID, additional_payment, payment_date))
            
            with open('./Synthetic-Data-Scripts/5.b.DML_payment_data.sql', 'a') as f:
                f.write(cursor.statement + ';\n')
            decimal.Decimal(total_amount_paid) == decimal.Decimal(total_amount_paid) + decimal.Decimal(additional_payment)

# Generate and insert payments
generate_payments()

# Commit the transaction and close the connection
conn.commit()
conn.close()
