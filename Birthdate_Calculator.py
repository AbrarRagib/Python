from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Input the birthdate in YYYY-MM-DD format
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert the string input to a date object
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

# Calculate and print the age
age = calculate_age(birthdate)
print(f"Your age is: {age} years")
