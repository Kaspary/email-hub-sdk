import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from src.clients import BaseEmailClient
from src.models import EmailMime


class EmailService:
    def __init__(self, client: BaseEmailClient):
        self.__client = client

    def _mount_email(self, email: EmailMime) -> MIMEMultipart:
        mime = MIMEMultipart()
        mime["From"] = f"No Reply <{email.sender}>"
        mime["To"] = COMMASPACE.join(email.to)
        mime["Cc"] = COMMASPACE.join(email.cc)
        mime["Bcc"] = COMMASPACE.join(email.bcc)
        mime["Date"] = formatdate(localtime=True)
        mime["Subject"] = email.subject
        mime.attach(MIMEText(email.body))

        if email.attatchment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(email.attatchment)
            encoders.encode_base64(part)
            mime.attach(part)

        return mime

    def send_email(self, email: EmailMime) -> None:
        logging.debug(f"Send e-mail to {email.recipients}")
        mime = self._mount_email(email)
        with self.__client.smtp() as smtp:
            smtp.send_mail(email.recipients, mime.as_string())
