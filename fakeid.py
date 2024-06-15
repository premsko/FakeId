import random

def fakename():
    first_names = [
        'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas',
        'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
        'Christopher', 'Matthew', 'Daniel', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth',
        'Emily', 'Ashley', 'Megan', 'Amanda', 'Rachel', 'Lauren', 'Sarah', 'Hannah', 'Kayla', 'Stephanie',
        'Joshua', 'Kevin', 'Brian', 'Jason', 'Eric', 'Samantha', 'Melissa', 'Heather', 'Nicole', 'Amy',
        'Laura', 'Kimberly', 'Angela', 'Tiffany', 'Christina', 'Crystal', 'Brittany', 'Melissa', 'Rebecca'
    ]
    last_names = [
        'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
        'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
        'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
        'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
        'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins'
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def fakeemail(name):
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    name_parts = name.lower().split()
    username = ''.join(name_parts) + str(random.randint(1, 99))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def fakelocation():
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
    states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA']
    return f"{random.choice(cities)}, {random.choice(states)}, USA"

def fakeprofile():
    name = fakename()
    email = fakeemail(name)
    location = fakelocation()
    profile_pic = f"https://thispersondoesnotexist.com/"
    return {
        'Name': name,
        'Email': email,
        'Location': location,
        'Profile Picture': profile_pic
    }
fake_person = fakeprofile()

for key, value in fake_person.items():
    print(f"{key}: {value}")
