import random
import string

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test the function
password_length = int(input("Enter the length of the password: "))
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)



