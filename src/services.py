import logging
from src.adapters import EmailMIMEAdapter

from src.clients import BaseEmailClient


class EmailService:
    def __init__(self, client: BaseEmailClient):
        self.__client = client

    def send_email(self, email: EmailMIMEAdapter) -> None:
        logging.debug(f"Send e-mail to {email.recipients}")
        with self.__client.smtp() as smtp:
            smtp.send_email(email.recipients, email.as_string())
