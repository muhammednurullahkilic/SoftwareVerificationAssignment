import pytest
from src.validator import UserValidator

# Setup Metodu 
@pytest.fixture
def validator():
    return UserValidator()

# --- First Name Testleri ---

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