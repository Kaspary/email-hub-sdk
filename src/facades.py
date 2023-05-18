from src.adapters import EmailMIMEAdapter
from src.services import EmailService
from src.clients import BaseEmailClient, GmailClient, OutlookClient


def send_email_with_gmail(
    account: str,
    password: str,
    subject: str,
    body: str,
    to_addrs: list[str],
    cc_addrs: list[str],
    bcc_addrs: list[str],
    attatchments: list[tuple[bytes, str]],
    sender: str | tuple[str, str] = None,
):
    return send_email(
        GmailClient(account, password),
        sender or account,
        subject,
        body,
        to_addrs,
        cc_addrs,
        bcc_addrs,
        attatchments,
    )


def send_email_with_outlook(
    account: str,
    password: str,
    subject: str,
    body: str,
    to_addrs: list[str],
    cc_addrs: list[str],
    bcc_addrs: list[str],
    attatchments: list[tuple[bytes, str]],
    sender: str | tuple[str, str] = None,
):
    return send_email(
        OutlookClient(account, password),
        sender or account,
        subject,
        body,
        to_addrs,
        cc_addrs,
        bcc_addrs,
        attatchments,
    )


def send_email(
    client: BaseEmailClient,
    sender: str | tuple[str, str],
    subject: str,
    body: str,
    to_addrs: list[str],
    cc_addrs: list[str],
    bcc_addrs: list[str],
    attatchments: list[tuple[bytes, str]],
):
    service = EmailService(client)
    return service.send_email(
        EmailMIMEAdapter(
            sender,
            subject,
            body,
            to_addrs,
            cc_addrs,
            bcc_addrs,
            attatchments,
        )
    )
