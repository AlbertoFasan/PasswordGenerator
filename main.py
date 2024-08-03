import random
import string
import yaml

def load_config(file_path):
    """
    Load the YAML configuration file.

    Args:
        file_path (str): The path to the YAML configuration file.

    Returns:
        dict: The loaded configuration.
    """
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def generate_password(length, excluded_passwords):
    """
    Generate a random password of the specified length, excluding the given passwords.

    Args:
        length (int): The length of the password to generate.
        excluded_passwords (list): A list of passwords to exclude.

    Returns:
        str: The generated password.
    """
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine the character sets
    all_chars = lowercase + uppercase + digits + special_chars

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the password to avoid the first characters always being from the same set
    random.shuffle(password)

    # Join the password into a single string
    password = ''.join(password)

    # Check if the password is in the excluded list
    if password in excluded_passwords:
        # If it is, generate a new password
        return generate_password(length, excluded_passwords)

    return password

def main():
    config_file = 'config.yml'
    config = load_config(config_file)

    length = config['password_length']
    excluded_passwords = config['excluded_passwords']

    password = generate_password(length, excluded_passwords)
    print(f"Generated password: {password}")

if __name__ == '__main__':
    main()