from src.email import send_email
from src.models import Person
from pytest_mock import MockFixture
from sib_api_v3_sdk.models.send_smtp_email import SendSmtpEmail

class TestSendEmail:

    def test_send_email(self, mocker: MockFixture):
        mock_send_smtp_email = mocker.patch(
            "sib_api_v3_sdk.TransactionalEmailsApi.send_transac_email"
        )

        employee = Person(
            name="Anas",
            email="mail.ridwanray@gmail.com",
            title="Engineer",
            phone="01234567890",
        )

        send_email(employee)
        mock_send_smtp_email.assert_called_once()
        arguments: SendSmtpEmail = mock_send_smtp_email.call_args[0][0]
        assert arguments.subject == "Email from Pytest"
        assert arguments.to == [{"email":employee.email}]