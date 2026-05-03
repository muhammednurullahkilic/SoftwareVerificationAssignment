import re
from datetime import datetime, timedelta

def is_valid_name(name):
    
    return bool(re.fullmatch(r"[A-Za-zÇçĞğİıÖöŞşÜü]+( [A-Za-zÇçĞğİıÖöŞşÜü]+){0,2}", name or ""))


def is_valid_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email or ""))

def is_valid_password(password):
    return (
        password is not None
        and len(password) >= 8
        and any(c.isalpha() for c in password)
        and any(c.isdigit() for c in password)
    )

def is_valid_dob(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%d/%m/%Y")
        return dob <= datetime.now() - timedelta(days=365*18)
    except (ValueError, TypeError):
        return False

def passwords_match(p1, p2):
    return p1 == p2 and p1 != ""