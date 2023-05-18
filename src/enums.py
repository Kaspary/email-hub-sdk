from enum import Enum


class ServerSMTP(Enum):
    GMAIL = "smtp.gmail.com"
    OUTLOOK = "smtp-mail.outlook.com"


class PortSMTP(Enum):
    GMAIL = 465
    OUTLOOK = 587
