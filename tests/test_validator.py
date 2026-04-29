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