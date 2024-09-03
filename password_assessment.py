import re

def assess_password_strength(password):
    # Criteria for password strength
    criteria = {
        "length": len(password) >= 8,
        "lowercase": bool(re.search(r'[a-z]', password)),
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    # Scoring
    score = sum(criteria.values())

    # Feedback
    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["lowercase"]:
        feedback.append("Password should contain at least one lowercase letter.")
    if not criteria["uppercase"]:
        feedback.append("Password should contain at least one uppercase letter.")
    if not criteria["digit"]:
        feedback.append("Password should contain at least one digit.")
    if not criteria["special_char"]:
        feedback.append("Password should contain at least one special character.")

    # Password strength assessment
    if score == 5:
        strength = "Your Password is Strong"
    elif 3 <= score < 5:
        strength = "Your Password is Moderate"
    else:
        strength = "Your Password is Weak"

    return strength, feedback

# Usage
password = input("Enter your password to assess its strength: ")
strength, feedback = assess_password_strength(password)

print(f"Password strength: {strength}")
for comment in feedback:
    print(comment)
