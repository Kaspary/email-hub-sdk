from unittest import mock
from src.clients import BaseEmailClient, GmailClient, OutlookClient
from src.enums import PortSMTP, ServerSMTP

SERVER_MOCK = "smtp.server.com"
PORT_MOCK = "8888"
ACCOUNT_MOCK = "account@email.com"
PASSWORD_MOCK = "password1234"
TO_MOCK = ['to_example@email.com']
MESSAGE_MOCK = 'EMAIL MESSAGE'

class TestBaseEmailClient:
    def setup_method(self):
        BaseEmailClient.__abstractmethods__ = set()
        self.client = BaseEmailClient(
            server=SERVER_MOCK,
            port=PORT_MOCK,
            account=ACCOUNT_MOCK,
            password=PASSWORD_MOCK,
        )

    def test_initialization(self):
        assert self.client._server == SERVER_MOCK
        assert self.client._port == PORT_MOCK
        assert self.client._account == ACCOUNT_MOCK
        assert self.client._password == PASSWORD_MOCK
        assert self.client._client == None

    @mock.patch("src.clients.BaseEmailClient._client")
    @mock.patch("src.clients.BaseEmailClient.__enter__")
    def test_the_with_statement(self, enter_mock, client_mock):
        enter_mock.return_value = self.client
        client_mock.close.return_value = None

        with self.client.smtp() as smtp:
            assert isinstance(smtp, self.client.__class__)

        assert client_mock.close.called_once
        assert enter_mock.called_once


class TestGmailClient:
    def setup_method(self):
        self.client = GmailClient(account=ACCOUNT_MOCK, password=PASSWORD_MOCK)

    def test_initialization(self):
        assert self.client._server == ServerSMTP.GMAIL.value
        assert self.client._port == PortSMTP.GMAIL.value
        assert self.client._account == ACCOUNT_MOCK
        assert self.client._password == PASSWORD_MOCK
        assert self.client._client == None

    @mock.patch("src.clients.smtplib.SMTP_SSL")
    def test_smtp(self, smtp_mock):
        smtp_mock.login.return_value = None

        result = self.client.smtp()
        assert isinstance(result, self.client.__class__)
        assert smtp_mock.called_once_with(ServerSMTP.GMAIL.value, PortSMTP.GMAIL.value)
        assert smtp_mock.login.called_once_with(ACCOUNT_MOCK, PASSWORD_MOCK)

    @mock.patch("src.clients.GmailClient._client")
    def test_send_mail(self, client_mock):
        client_mock.sendmail.return_value = None
        result = self.client.send_mail(
            to_addrs=TO_MOCK,
            message=MESSAGE_MOCK,
        )

        assert result == None
        assert client_mock.sendmail.called_once_with(ACCOUNT_MOCK, TO_MOCK, MESSAGE_MOCK)


class TestOutlookClient:
    def setup_method(self):
        self.client = OutlookClient(account=ACCOUNT_MOCK, password=PASSWORD_MOCK)

    def test_initialization(self):
        assert self.client._server == ServerSMTP.OUTLOOK.value
        assert self.client._port == PortSMTP.OUTLOOK.value
        assert self.client._account == ACCOUNT_MOCK
        assert self.client._password == PASSWORD_MOCK
        assert self.client._client == None

    @mock.patch("src.clients.smtplib.SMTP")
    def test_smtp(self, smtp_mock):
        smtp_mock.login.return_value = None
        smtp_mock.starttls.return_value = None

        result = self.client.smtp()
        assert isinstance(result, self.client.__class__)
        assert smtp_mock.called_once_with(ServerSMTP.GMAIL.value, PortSMTP.GMAIL.value)
        assert smtp_mock.login.called_once_with(ACCOUNT_MOCK, PASSWORD_MOCK)
        assert smtp_mock.starttls.called_once

    @mock.patch("src.clients.OutlookClient._client")
    def test_send_mail(self, client_mock):
        client_mock.sendmail.return_value = None
        result = self.client.send_mail(
            to_addrs=TO_MOCK,
            message=MESSAGE_MOCK,
        )

        assert result == None
        assert client_mock.sendmail.called_once_with(ACCOUNT_MOCK, TO_MOCK, MESSAGE_MOCK)
