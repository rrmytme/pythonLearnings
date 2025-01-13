import csv

from .models import Person
from .validators import MAX_CSV_LENGTH, validate_csv_headers, validate_csv_length


def read_csv(file_path):

    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

        missing_cols = validate_csv_headers(csv_reader.fieldnames)

        if missing_cols:
            raise ValueError(f"Missing column(s) detected:{missing_cols}")

        if not validate_csv_length(data):
            raise ValueError(f"CSV length exceeds {MAX_CSV_LENGTH}.")

        # Validate and parse each row into a Person model
        people = [Person(**row) for row in data]
        return people