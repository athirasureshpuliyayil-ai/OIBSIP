import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a random password with selected options"""
    if length < 4:
        length = 4  # minimum length for safety
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        chars = string.ascii_letters  # fallback

    return "".join(random.choice(chars) for _ in range(length))

def check_strength(password):
    """Return password strength"""
    length = len(password)
    categories = [any(c.islower() for c in password),
                  any(c.isupper() for c in password),
                  any(c.isdigit() for c in password),
                  any(c in string.punctuation for c in password)]
    score = length + sum(categories) * 2

    if score < 8:
        return "Weak"
    elif score < 12:
        return "Medium"
    else:
        return "Strong"
