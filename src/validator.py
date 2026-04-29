import re

class UserValidator:
    def __init__(self):
        self.name_pattern = r"^[a-zA-ZçğıöşüÇĞİÖŞÜ\s]{2,50}$"

    def validate_first_name(self, first_name):
        if not first_name:
            return False
        return bool(re.match(self.name_pattern, first_name))

    def validate_last_name(self, last_name):
        if not last_name:
            return False
        return bool(re.match(self.name_pattern, last_name))