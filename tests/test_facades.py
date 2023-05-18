from unittest import mock
from email_hub_sdk.facades import send_email, send_email_with_gmail, send_email_with_outlook

ACCOUNT_MOCK = "account@email.com"
PASSWORD_MOCK = "password"
SUBJECT_MOCK = "Email Title"
BODY_MOCK = "Email Body"
SENDER_MOCK = "sender@email.com"
TO_ADDRS_MOCK = ["to_example@email.com"]
CC_ADDRS_MOCK = ["cc_example@email.com"]
BCC_ADDRS_MOCK = ["bcc_example@email.com"]
ATTATCHMENTS_MOCK = [(b"", "filename.txt")]


@mock.patch("src.facades.GmailClient")
@mock.patch("src.facades.send_email")
def test_send_email_with_gmail(send_email_mock, gmail_client_mock):
    send_email_with_gmail(
        account=ACCOUNT_MOCK,
        password=PASSWORD_MOCK,
        subject=SUBJECT_MOCK,
        body=BODY_MOCK,
        to_addrs=SENDER_MOCK,
        cc_addrs=TO_ADDRS_MOCK,
        bcc_addrs=CC_ADDRS_MOCK,
        attatchments=BCC_ADDRS_MOCK,
        sender=ATTATCHMENTS_MOCK,
    )
    assert send_email_mock.called_once_with(
        SUBJECT_MOCK,
        BODY_MOCK,
        SENDER_MOCK,
        TO_ADDRS_MOCK,
        CC_ADDRS_MOCK,
        BCC_ADDRS_MOCK,
        ATTATCHMENTS_MOCK
    )
    assert gmail_client_mock.called_once_with(ACCOUNT_MOCK, PASSWORD_MOCK)


@mock.patch("src.facades.OutlookClient")
@mock.patch("src.facades.send_email")
def test_send_email_with_outlook(send_email_mock, outlook_client_mock):
    send_email_with_outlook(
        account=ACCOUNT_MOCK,
        password=PASSWORD_MOCK,
        subject=SUBJECT_MOCK,
        body=BODY_MOCK,
        to_addrs=SENDER_MOCK,
        cc_addrs=TO_ADDRS_MOCK,
        bcc_addrs=CC_ADDRS_MOCK,
        attatchments=BCC_ADDRS_MOCK,
        sender=ATTATCHMENTS_MOCK,
    )
    assert send_email_mock.called_once(
        SUBJECT_MOCK,
        BODY_MOCK,
        SENDER_MOCK,
        TO_ADDRS_MOCK,
        CC_ADDRS_MOCK,
        BCC_ADDRS_MOCK,
        ATTATCHMENTS_MOCK
    )
    assert outlook_client_mock.called_once_with(ACCOUNT_MOCK, PASSWORD_MOCK)


@mock.patch("src.facades.EmailMIMEAdapter")
@mock.patch("src.facades.EmailService")
def test_send_email(email_mime_mock, email_service_mock):
    client_obj = mock.Mock()
    send_email(
        client=client_obj,
        subject=SUBJECT_MOCK,
        body=BODY_MOCK,
        to_addrs=SENDER_MOCK,
        cc_addrs=TO_ADDRS_MOCK,
        bcc_addrs=CC_ADDRS_MOCK,
        attatchments=BCC_ADDRS_MOCK,
        sender=ATTATCHMENTS_MOCK,
    )
    assert email_mime_mock.called_once_with(
        SUBJECT_MOCK,
        BODY_MOCK,
        SENDER_MOCK,
        TO_ADDRS_MOCK,
        CC_ADDRS_MOCK,
        BCC_ADDRS_MOCK,
        ATTATCHMENTS_MOCK
    )
    assert email_service_mock.called_once_with(client_obj)
