import pytest
from src.validator import UserValidator

@pytest.fixture
def validator():
    return UserValidator()

def test_first_name_valid(validator):
    assert validator.validate_first_name("Ahmet") is True

def test_first_name_too_short(validator):
    assert validator.validate_first_name("A") is False

def test_first_name_with_numbers(validator):
    assert validator.validate_first_name("Ahmet123") is False

def test_first_name_empty(validator):
    assert validator.validate_first_name("") is False

def test_email_valid(validator):
    assert validator.validate_email("test@example.com") is True

def test_email_missing_at(validator):
    assert validator.validate_email("testexample.com") is False

def test_email_no_domain(validator):
   assert validator.validate_email("test@example") is False

def test_dob_valid(validator):
   assert validator.validate_dob("29/04/2026") is True

def test_dob_invalid_format(validator):
    assert validator.validate_dob("29.04.2026") is False

def test_dob_non_existent_date(validator):
    assert validator.validate_dob("31/04/2026") is False

def test_dob_leap_year_valid(validator):
    assert validator.validate_dob("29/02/2024") is True   

def test_password_strong(validator):
    assert validator.validate_password("SecurePass123!") is True

def test_password_too_short(validator):
    assert validator.validate_password("Secur1!") is False

def test_password_no_uppercase(validator):
    assert validator.validate_password("securepass123!") is False

def test_password_no_number(validator):
    assert validator.validate_password("SecurePass!") is False

def test_password_hacker_sql_injection(validator):
    assert validator.validate_password("' OR 1=1 --") is False 

def test_confirm_password_match(validator):
    assert validator.validate_confirm_password("SecurePass123!", "SecurePass123!") is True

def test_confirm_password_mismatch(validator):
    assert validator.validate_confirm_password("SecurePass123!", "WrongPass123!") is False