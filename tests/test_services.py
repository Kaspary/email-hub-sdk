from unittest import mock
from src.models import EmailMime
from src.services import EmailService


class TestEmailService:

    def setup_method(self):
        pass


    @mock.patch("src.services.EmailService._mount_email")
    def test_send_email(self, mount_email):

        mime_obj = mock.Mock()
        mime_obj.as_string.return_value = 'EMAIL MESSAGE'
        mount_email.return_value = mime_obj

        client_obj = mock.MagicMock()
        client_obj.__enter__.return_value = client_obj
        client_obj.__exit__.return_value = None
        client_obj.smtp.return_value = client_obj
        client_obj.send_mail.return_value = None

        service = EmailService(client_obj)

        email_mime = EmailMime(
            sender='sender_example@email.com',
            subject='TESTE',
            body='BODY',
            to=['to_example@email.com'],
            cc=['cc_example@email.com'],
            bcc=['bcc_example@email.com'],
        )
        result = service.send_email(email_mime)

        assert client_obj.__enter__.called_once
        assert client_obj.__exit__.called_once
        assert client_obj.smtp.called_once
        assert client_obj.send_mail.called_once_with(email_mime.recipients, mime_obj.as_string.return_value)
        assert result == None
