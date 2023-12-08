import random
import string

def generate_password(length, include_uppercase=True, include_numbers=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    # Get user input
    length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate and print passwords
    for _ in range(num_passwords):
        password = generate_password(length)
        print(password)

if __name__ == "__main__":
    main()
