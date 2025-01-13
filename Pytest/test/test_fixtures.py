import pytest
import os
import csv
from tempfile import NamedTemporaryFile

@pytest.fixture
def make_valid_csv_file():
    with NamedTemporaryFile(suffix=".csv", delete=False,mode="w") as temp_file:
        writer = csv.writer(
            temp_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        writer.writerow(["name", "email", "title", "phone"])
        writer.writerow(["RR1", "rrmytme@gmail.com","Software Engineer","02012345678"])
        writer.writerow(["RR2","rrajeshrajappan@gmail.com","AI Engineer","02012345679"])
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture(scope="function")
def make_invalid_csv_file():
    with NamedTemporaryFile(suffix=".csv", delete=False,mode="w") as temp_file:
        writer = csv.writer(
            temp_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        writer.writerow(["name", "email", "title", "phone"])
        writer.writerow(["hay", "hi@xyz", "Engineer", "01234567890"])

    yield temp_file.name
    os.remove(temp_file.name)