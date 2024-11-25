import random
import string

def generate_password(length):
    """Generates a random password of the specified length.

    Args:
        length: The desired length of the password.

    Returns:
        The generated password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter the desired password length (between 8 and 20): "))
            if 8 <= length <= 20:
                password = generate_password(length)
                print("Generated password:", password)
                break
            else:
                print("Invalid length. Please enter a number between 8 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")