import random
import mysql.connector

first_names = [
    'Mwangi', 'Achieng', 'Kamau', 'Wanjiku', 'Otieno', 'Njeri', 'Kiptoo', 'Wambui', 'Mutiso', 'Amina',
    'Jean', 'Marie', 'Claude', 'Patrick', 'Emmanuel', 'Joseph', 'Paul', 'Pierre', 'Jacques', 'Michel',
    'Felix', 'Alain', 'Jeanne', 'Marie', 'Claudine', 'Patricia', 'Emmanuelle', 'Josephine', 'Pauline',
    'Pierrette', 'Jacqueline', 'Michelle', 'Felicite', 'Alaine'
]
last_names = [
    'Omondi', 'Kiplagat', 'Mutua', 'Wanyama', 'Odhiambo', 'Kariuki', 'Njoroge', 'Ochieng', 'Muthoni', 'Mwangi',
    'Mugisha', 'Ndayishimiye', 'Nkurunziza', 'Kagame', 'Bizimana', 'Mukasa', 'Kabongo', 'Mutombo', 'Kabila',
    'Lumumba', 'Mugabe', 'Mandela', 'Zuma', 'Malema', 'Mbeki', 'Mbeki', 'Mandela', 'Zuma', 'Malema', 'Mbeki',
    'Mbeki', 'Munee', 'Munyao', 'Munyoki', 'Munyua', 'Munyui', 'Munyuli', 'Munywe', 'Munzala', 'Munzala',
    'Hassan', 'Mohammed', 'Ali', 'Abdi', 'Omar', 'Osman', 'Hussein', 'Ahmed', 'Ibrahim', 'Adan', 'Yusuf',
    'Abdullahi'
]
streets = ['Nairobi St', 'Mombasa Rd', 'Kisumu Ave', 'Eldoret Ln', 'Nakuru Blvd',
    'Thika Rd', 'Langata Rd', 'Ngong Rd', 'Jogoo Rd', 'Kenyatta Ave', 'Moi Ave', 'Haile Selassie Ave', 
    'Uhuru Hwy', 'Waiyaki Way', 'Limuru Rd', 'Kiambu Rd', 'Mbagathi Way', 'Dennis Pritt Rd', 'James Gichuru Rd',
    'Riverside Dr', 'State House Rd', 'Koinange St', 'Tom Mboya St', 'Mama Ngina St', 'Kimathi St', 
    'Kilimani Rd', 'Kileleshwa Rd', 'Lavington Rd', 'Karen Rd', 'Runda Dr', 'Gigiri Rd', 'Westlands Rd', 
    'Parklands Rd', 'Eastleigh Rd', 'South B Rd', 'South C Rd', 'Embakasi Rd', 'Donholm Rd', 'Buruburu Rd'
]
counties = [
    'Nairobi', 'Mombasa', 'Kisumu', 'Eldoret', 'Nakuru', 
    'Machakos', 'Kiambu', 'Muranga', 'Nyeri', 'Meru', 
    'Embu', 'Kitui', 'Garissa', 'Wajir', 'Mandera', 
    'Marsabit', 'Isiolo', 'Tharaka-Nithi', 'Laikipia', 'Baringo'
]
sub_counties = [
    'Westlands', 'Kasarani', 'Embakasi', 'Langata', 'Dagoretti',
    'Nyali', 'Likoni', 'Changamwe', 'Kisauni', 'Jomvu',
    'Kisumu Central', 'Kisumu East', 'Kisumu West', 'Nyando', 'Muhoroni',
    'Eldoret East', 'Eldoret West', 'Kesses', 'Moiben', 'Turbo',
    'Nakuru Town', 'Naivasha', 'Gilgil', 'Molo', 'Subukia'
]

business_prefixes = ['Safari', 'Serena', 'Sarova', 'Fairmont', 'InterContinental', 'Hilton', 'Villa Rosa', 'Ole Sereni',
                     'Boma', 'PrideInn','Nyali', 'Diani', 'Hemingways', 'Tamarind', 'Swahili', 'Baobab', 'Voyager',
                     'Leopard Beach', 'Severin', 'Neptune']
business_suffixes = ['Hotel', 'Resort', 'Lodge', 'Suites', 'Inn', 'Retreat', 'Haven', 'Palace', 'Manor', 'Residences']

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='student',
    password='5trathm0re',
    database='siwaka_dishes'
)
cursor = conn.cursor()

# Generate 1,200 customers (synthetic data)
for i in range(1200):
    if random.choice([True, False]):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        customer_name = f'{first_name} {last_name}'
    else:
        customer_name = f'[Business] {random.choice(business_prefixes)} {random.choice(business_suffixes)}'
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
    
    phone = '07' + ''.join([str(random.randint(0, 9)) for _ in range(8)])
    address_line1 = f'{random.randint(1, 999)} {random.choice(streets)}'
    address_line2 = f'Apt {random.randint(1, 100)}'
    postal_code = f'{random.randint(100, 90600)}'
    county = random.choice(counties)
    sub_county = random.choice(sub_counties)
    sales_rep_employee_number = random.randint(1, 20)
    
    cursor.execute(
        "INSERT INTO siwaka_dishes.customer (customerName, contactFirstName, contactLastName, phone, addressLine1, addressLine2, postalCode, county, subCounty, salesRepEmployeeNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (customer_name, first_name, last_name, phone, address_line1, address_line2, postal_code, county, sub_county, sales_rep_employee_number)
    )

    with open('./Synthetic-Data-Scripts/3.b.DML_customerOrder_data.sql', 'a') as f:
        f.write(cursor.statement + ';\n')

conn.commit()
cursor.close()
conn.close()