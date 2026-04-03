import random
import string

def generate_password(length=12, use_symbols=True):
    """
    Generate a strong password.

    Parameters:
    - length (int): length of the password (default 12)
    - use_symbols (bool): whether to include symbols (default True)

    Returns:
    - str: generated password
    """

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/" if use_symbols else ""

    # Ensure at least one character from each required type
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    if use_symbols:
        password_chars.append(random.choice(symbols))

    # Fill the rest of the password
    all_chars = lower + upper + digits + symbols
    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_chars, k=remaining_length)

    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)

    return "".join(password_chars)
