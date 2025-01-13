import pytest
from pydantic import ValidationError
from src.reader import read_csv

class TestReadCSV:

    def test_read_valid_csv(self, make_valid_csv_file):
        test_result = read_csv(make_valid_csv_file)
        assert isinstance(test_result, list)
        assert len(test_result) == 2


    def test_invalid_csv_file(self, make_invalid_csv_file):
        with pytest.raises(ValidationError):
            read_csv(make_invalid_csv_file)