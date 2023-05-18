from unittest import mock
from email_hub_sdk.services import EmailService


class TestEmailService:
    def setup_method(self):
        pass

    def test_send_email(self):
        mime_obj = mock.Mock()
        mime_obj.as_string.return_value = "EMAIL MESSAGE"
        mime_obj.recipients = ["example@email.com"]

        client_obj = mock.MagicMock()
        client_obj.__enter__.return_value = client_obj
        client_obj.__exit__.return_value = None
        client_obj.smtp.return_value = client_obj
        client_obj.send_mail.return_value = None

        service = EmailService(client_obj)

        result = service.send_email(mime_obj)

        assert client_obj.__enter__.called_once
        assert client_obj.__exit__.called_once
        assert client_obj.smtp.called_once
        assert client_obj.send_mail.called_once_with(
            mime_obj.recipients, mime_obj.as_string.return_value
        )
        assert result is None
