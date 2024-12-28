import random
import mysql.connector

first_names = [
    'Mwangi', 'Achieng', 'Kamau', 'Wanjiku', 'Otieno', 'Njeri', 'Kiptoo', 'Wambui', 'Mutiso', 'Amina',
    'Jean', 'Marie', 'Claude', 'Patrick', 'Emmanuel', 'Joseph', 'Paul', 'Pierre', 'Jacques', 'Michel',
    'Felix', 'Alain', 'Jeanne', 'Marie', 'Claudine', 'Patricia', 'Emmanuelle', 'Josephine', 'Pauline',
    'Pierrette', 'Jacqueline', 'Michelle', 'Felicite', 'Alaine', 'Kwame', 'Chinua', 'Ngozi', 'Thabo', 'Zanele',
    'Bongani', 'Kofi', 'Adebayo', 'Fatou', 'Lerato', 'Adisa', 'Binta', 'Chiamaka', 'Dayo', 'Ebele',
    'Femi', 'Gbemisola', 'Hawa', 'Ifeanyi', 'Jelani'
]

last_names = [
    'Omondi', 'Kiplagat', 'Mutua', 'Wanyama', 'Odhiambo', 'Kariuki', 'Njoroge', 'Ochieng', 'Muthoni', 'Mwangi',
    'Mugisha', 'Ndayishimiye', 'Nkurunziza', 'Kagame', 'Bizimana', 'Mukasa', 'Kabongo', 'Mutombo', 'Kabila',
    'Lumumba', 'Mugabe', 'Mandela', 'Zuma', 'Malema', 'Mbeki', 'Mbeki', 'Mandela', 'Zuma', 'Malema', 'Mbeki',
    'Mbeki', 'Munee', 'Munyao', 'Munyoki', 'Munyua', 'Munyui', 'Munyuli', 'Munywe', 'Munzala', 'Munzala',
    'Hassan', 'Mohammed', 'Ali', 'Abdi', 'Omar', 'Osman', 'Hussein', 'Ahmed', 'Ibrahim', 'Adan', 'Yusuf',
    'Abdullahi'
]

job_titles = [
    'Manager', 'Assistant Manager', 'Chef', 'Sous Chef', 'Cook', 'Waiter', 'Waitress', 'Bartender', 'Host', 'Hostess',
    'Dishwasher', 'Cleaner', 'Cashier', 'Receptionist', 'Security Guard'
]

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='student',
    password='5trathm0re',
    database='siwaka_dishes'
)
cursor = conn.cursor()

# Generate 52 employees (synthetic data)
for i in range(52):
    employee_number = i + 1  # Assuming employee numbers start from 1
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f'{first_name[0].lower()}{last_name.lower()}@siwakadishes.co.ke'
    email = f'{first_name[0].lower()}{last_name.lower()}{random.randint(1, 100)}@siwakadishes.co.ke'
    branch_code = random.randint(1, 10)
    job_title = random.choice(job_titles)

    cursor.execute(
        "INSERT INTO siwaka_dishes.employee (employeeNumber, firstName, lastName, email, branchCode, jobTitle) VALUES (%s, %s, %s, %s, %s, %s)",
        (employee_number, first_name, last_name, email, branch_code, job_title)
    )

    with open('./Synthetic-Data-Scripts/1.c.DML_employee_data.sql', 'a') as f:
        f.write(cursor.statement + ';\n')

conn.commit()

# Retrieve employee numbers of employees with managerial job titles
cursor = conn.cursor()
cursor.execute("SELECT employeeNumber FROM siwaka_dishes.employee WHERE jobTitle IN ('Manager', 'Assistant Manager', 'Chef', 'Sous Chef')")
managers = cursor.fetchall()

# Update each employee to assign a random manager as their reportsTo
cursor.execute("SELECT employeeNumber FROM siwaka_dishes.employee")
employees = cursor.fetchall()

for employee in employees:
    manager = random.choice(managers)[0]
    cursor.execute(
        "UPDATE siwaka_dishes.employee SET reportsTo = %s WHERE employeeNumber = %s",
        (manager, employee[0])
    )
    with open('./Synthetic-Data-Scripts/1.c.DML_employee_data.sql', 'a') as f:
        f.write(cursor.statement + ';\n')

conn.commit()
cursor.close()
conn.close()