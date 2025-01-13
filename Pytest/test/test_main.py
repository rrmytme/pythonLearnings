from main import main
from pytest_mock import MockFixture

def test_main(make_valid_csv_file, mocker: MockFixture):
    mock_send_smtp_email = mocker.patch(
            "sib_api_v3_sdk.TransactionalEmailsApi.send_transac_email"
        )
    main(make_valid_csv_file)
    assert mock_send_smtp_email.call_count == 2