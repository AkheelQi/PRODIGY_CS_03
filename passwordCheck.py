import re

def password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[\W_]', password)

    # Calculate strength score
    score = sum([length_criteria, bool(uppercase_criteria), bool(lowercase_criteria), bool(number_criteria), bool(special_char_criteria)])
    max_score = 5
    strength_percentage = (score / max_score) * 100

    # Provide feedback based on score
    if score == 5:
        strength_label = "Very Strong"
    elif score == 4:
        strength_label = "Strong"
    elif score == 3:
        strength_label = "Moderate"
    elif score == 2:
        strength_label = "Weak"
    else:
        strength_label = "Very Weak"

    return strength_label, strength_percentage

while True:
    password = input("Enter a password to check its strength: ")
    strength_label, strength_percentage = password_strength(password)
    print(f"Password strength: {strength_label} ({strength_percentage:.2f}%)")

    check_again = input("Do you want to check another password? (yes/no): ").strip().lower()
    if check_again != 'yes':
        break
