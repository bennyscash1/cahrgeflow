from datetime import date
import random
import os

def generate_random_numbers(count=5):
    return ''.join(str(random.randint(0, 9)) 
                   for _ in range(count))


def generate_email(valid_email=True):
    random_part = generate_random_numbers()

    if valid_email:
        return f"bennys+{random_part}@gmail.com"

    invalid_emails = [
        f"bennys{random_part}gmail.com", 
        f"bennys+{random_part}@",             
        f"@gmail.com",                         
        f"bennys+{random_part}@gmail",         
        f"bennys+{random_part}@.com",          
        f"bennys+{random_part}!@gmail.com", 
        f"bennys +{random_part}@gmail.com",    
    ]

    return random.choice(invalid_emails)
    

def generate_full_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Davis"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"


from datetime import date, timedelta
def get_birthdate_under_18():
    today = date.today()
    try:
        birthdate = today.replace(year=today.year - 18) + timedelta(days=2)
    except ValueError:
        # Handle February 29 for leap years
        birthdate = today.replace(month=2, day=28, year=today.year - 18) + timedelta(days=1)

    return birthdate.strftime("%Y-%m-%d")
