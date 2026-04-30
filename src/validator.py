import re
from datetime import datetime

class UserValidator:
    def __init__(self):
        self.name_pattern = r"^[a-zA-ZçğıöşüÇĞİÖŞÜ\s]{2,50}$"
        self.email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        self.password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\w\W]{8,}$"

    def validate_first_name(self, first_name):
        if not first_name:
            return False
        return bool(re.match(self.name_pattern, first_name))

    def validate_last_name(self, last_name):
        if not last_name:
            return False
        return bool(re.match(self.name_pattern, last_name))
    
    def validate_email(self, email):
        return bool(email and re.match(self.email_pattern, email))

    def validate_dob(self, dob_str):
        try:
            datetime.strptime(dob_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False
        
    def validate_password(self, password):
        return bool(password and re.match(self.password_pattern, password))

    def validate_confirm_password(self, password, confirm_password):
        return password == confirm_password