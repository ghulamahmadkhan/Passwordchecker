import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Minimum length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Rule 2: Contains uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Rule 3: Contains numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Rule 4: Contains special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Rule 5: Check for common patterns (e.g., "12345", "password")
    common_patterns = ["12345", "password", "qwerty", "letmein"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid using common patterns or words.")
        score -= 1

    if score >= 4:
        return "Strong", feedback
    elif score == 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")

    if feedback:
        print("Tips to improve your password:")
        for tip in feedback:
            print(f"- {tip}")

    if strength == "Weak":
        print("Here's a suggested strong password:")
        print(generate_strong_password())

if __name__ == "__main__":
    main()
