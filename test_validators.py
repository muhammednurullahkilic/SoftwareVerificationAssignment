import pytest
from validators import *

# --- NAME TESTS ---
def test_valid_single_name():
    assert is_valid_name("Ali")

def test_valid_multiple_names():
    assert is_valid_name("Şükrü Öztürk")
    assert is_valid_name("Ali Mehmet Veli")

def test_invalid_name_with_hyphen():
    assert not is_valid_name("Ali-Kemal")

def test_invalid_name_double_space():
    assert not is_valid_name("Ali  Kemal")

def test_invalid_name_four_words():
    assert not is_valid_name("Ali Mehmet Veli Bey")

def test_invalid_name_with_numbers():
    assert not is_valid_name("123Ali")

def test_invalid_name_empty():
    assert not is_valid_name("")
    assert not is_valid_name(None)

# --- EMAIL TESTS ---
def test_valid_email():
    assert is_valid_email("test@example.com")

def test_invalid_email_no_at():
    assert not is_valid_email("test.example.com")

def test_invalid_email_no_domain():
    assert not is_valid_email("user@.com")

def test_invalid_email_empty():
    assert not is_valid_email("")

# --- PASSWORD TESTS ---
def test_valid_password():
    assert is_valid_password("abc12345")

def test_invalid_password_too_short():
    assert not is_valid_password("1234567")

def test_invalid_password_no_digit():
    assert not is_valid_password("abcdefgh")

def test_invalid_password_no_letter():
    assert not is_valid_password("12345678")

# --- DOB TESTS ---
def test_valid_dob_over_18():
    assert is_valid_dob("01/01/2000")

def test_invalid_dob_under_18():
    assert not is_valid_dob("01/01/2020")

def test_invalid_dob_format():
    assert not is_valid_dob("invalid")

# --- PASSWORD MATCH TESTS ---
def test_passwords_match():
    assert passwords_match("abc12345", "abc12345")

def test_passwords_do_not_match():
    assert not passwords_match("abc12345", "ABC12345")

def test_passwords_empty_match():
    assert not passwords_match("", "")