from abc import ABC, abstractmethod
import smtplib
from typing import Sequence

from email_hub_sdk.enums import PortSMTP, ServerSMTP


class BaseEmailClient(ABC):
    _client: any = None

    def __init__(self, server: str, port: int, account: str, password: str):
        self._server = server
        self._port = port
        self._account = account
        self._password = password

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            self._client.close()
        return False

    def smtp(self):
        return self

    @abstractmethod
    def send_email(self, to_addrs: str | Sequence[str], msg: str, from_addr: str = None):
        pass


class GmailClient(BaseEmailClient):
    _client: smtplib.SMTP_SSL

    def __init__(self, account: str, password: str):
        super().__init__(
            ServerSMTP.GMAIL.value, PortSMTP.GMAIL.value, account, password
        )

    def smtp(self):
        self._client = smtplib.SMTP_SSL(self._server, self._port)
        self._client.login(self._account, self._password)
        return self

    def send_email(
        self, to_addrs: str | Sequence[str], message: str, from_addr: str = None
    ):
        from_addr = from_addr or self._account
        self._client.sendmail(from_addr, to_addrs, message)


class OutlookClient(BaseEmailClient):
    _client: smtplib.SMTP

    def __init__(self, account: str, password: str):
        super().__init__(
            ServerSMTP.OUTLOOK.value, PortSMTP.OUTLOOK.value, account, password
        )

    def smtp(self):
        self._client = smtplib.SMTP(self._server, self._port)
        self._client.starttls()
        self._client.login(self._account, self._password)
        return self

    def send_email(
        self, to_addrs: str | Sequence[str], message: str, from_addr: str = None
    ):
        from_addr = from_addr or self._account
        self._client.sendmail(from_addr, to_addrs, message)
