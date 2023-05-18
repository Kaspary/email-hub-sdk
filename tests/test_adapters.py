from src.adapters import EmailMIMEAdapter

SENDER_MOCK = "sender@email.com"
SUBJECT_MOCK = "Email Title"
BODY_MOCK = "Email Body"
TO_MOCK = ["to_example@email.com"]
CC_MOCK = ["cc_example@email.com"]
BCC_MOCK = ["bcc_example@email.com"]
ATTATCHMENTS_MOCK = [(b"", "filename.txt")]


class TestEmailMIMEAdapter:
    def test_initialization(self):
        adapter = EmailMIMEAdapter(
            sender=SENDER_MOCK,
            subject=SUBJECT_MOCK,
            body=BODY_MOCK,
            to=TO_MOCK,
            cc=CC_MOCK,
            bcc=BCC_MOCK,
            attatchments=ATTATCHMENTS_MOCK,
        )

        assert adapter.sender == SENDER_MOCK
        assert adapter.subject == SUBJECT_MOCK
        assert adapter.body == BODY_MOCK
        assert adapter.to == TO_MOCK
        assert adapter.cc == CC_MOCK
        assert adapter.bcc == BCC_MOCK
        assert adapter.attatchments == ATTATCHMENTS_MOCK
        assert isinstance(adapter.as_string(), str)
        assert adapter.recipients == TO_MOCK + CC_MOCK + BCC_MOCK

    def test_initialization_with_name_sender(self):
        sender = ("Example", "example@email.com")
        adapter = EmailMIMEAdapter(
            sender=sender,
            subject=SUBJECT_MOCK,
            body=BODY_MOCK,
            to=TO_MOCK,
            cc=CC_MOCK,
            bcc=BCC_MOCK,
            attatchments=ATTATCHMENTS_MOCK,
        )

        assert sender[0] in adapter.sender
        assert sender[1] in adapter.sender
