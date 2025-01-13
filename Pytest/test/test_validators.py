import pytest
from src.validators import validate_phone, validate_csv_headers

# def test_validate_phone():
#     number = "+2341234567890"
#     is_valid =  validate_phone(number)
#     assert is_valid

# def test_validate_phone_1():
#     number = "01234567890"
#     is_valid =  validate_phone(number)
#     assert is_valid    

# def test_validate_phone_2():
#     number = "03734"
#     is_valid =  validate_phone(number)
#     assert not is_valid


# def test_validate_invalid_csv_hearders():
#     headers = ["phone", "title"]
#     missing_cols = validate_csv_headers(headers)
#     assert sorted(missing_cols) == sorted(["email", "name"])
@pytest.mark.skip(reason="To be tested later")
@pytest.mark.unit
@pytest.mark.parametrize("phone_number,output",
                         [
                            ("080", False),
                            ("01234567890", True),
                            ("+2341234567890", True),
                            ("+23412345678", False) 
                         ])
def test_validate_phone(phone_number, output):
    test_result =  validate_phone(phone_number)
    assert test_result == output

@pytest.mark.skip(reason="To be tested later")
@pytest.mark.unit
@pytest.mark.parametrize("headers,missing_cols",
                         [
                             (["phone", "title"],["email","name"]),
                             (["name","email", "phone","title"],[]),
                             ([], ["name","email", "phone","title"]),
                         ])
def test_validate_csv_headers(headers, missing_cols):
    test_result = validate_csv_headers(headers)
    assert sorted(test_result) == sorted(missing_cols)