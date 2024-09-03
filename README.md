This is my 3rd project in prodigy infotech. This code is designed to assess the strength of a password based on certain security criteria. Specifically, it evaluates whether a password is "Strong," "Moderate," or "Weak" by checking if it meets the following conditions:

1. **Length**: The password should be at least 8 characters long.
2. **Lowercase Letters**: The password should contain at least one lowercase letter (e.g., `a`, `b`, `c`).
3. **Uppercase Letters**: The password should contain at least one uppercase letter (e.g., `A`, `B`, `C`).
4. **Digits**: The password should contain at least one numeric digit (e.g., `0`, `1`, `2`).
5. **Special Characters**: The password should contain at least one special character (e.g., `!`, `@`, `#`).

### Key Functions:
- **assess_password_strength(password)**: This function takes a password as input and checks it against the criteria listed above. It then provides a score based on how many criteria are met and offers feedback if the password is lacking in any area.

### Usage:
When you run the code, it will prompt you to enter a password. After you input the password, the program will:
1. Assess its strength.
2. Print the strength classification ("Strong," "Moderate," or "Weak").
3. Provide feedback if the password does not meet certain criteria.

This tool is useful for helping users create stronger, more secure passwords by giving them immediate feedback on how to improve their password strength.
