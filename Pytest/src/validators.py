import re

PHONE_NUMBER_REGEX = r"^(0|\+234)\d{10}$"
MAX_CSV_LENGTH = 100


def validate_phone(phone: str):
    if re.match(PHONE_NUMBER_REGEX, phone):
        return True
    return False


def validate_csv_length(data: list) -> bool:
    if len(data) > MAX_CSV_LENGTH:
        return False
    return True


def validate_csv_headers(csv_headers: list) -> list:
    """Returns the missing columns"""
    expected_headers = ["name", "email", "title", "phone"]
    missing_col = [header for header in expected_headers if header not in csv_headers]

    return missing_col