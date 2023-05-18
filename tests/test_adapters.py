from unittest import mock

import pytest
from src.adapters import EmailMIMEAdapter

SENDER_MOCK = "sender@email.com"
SUBJECT_MOCK = "Email Title"
BODY_MOCK = "Email Body"
TO_MOCK = ["to_example@email.com"]
CC_MOCK = ["cc_example@email.com"]
BCC_MOCK = ["bcc_example@email.com"]
ATTATCHMENTS_MOCK = [(b"", "filename.txt")]


class TestEmailMIMEAdapter:
    def setup_method(self):
        self.adapter = EmailMIMEAdapter(
            sender=SENDER_MOCK,
            subject=SUBJECT_MOCK,
            body=BODY_MOCK,
            to=TO_MOCK,
            cc=CC_MOCK,
            bcc=BCC_MOCK,
            attatchments=ATTATCHMENTS_MOCK,
        )

    def test_initialization(self):
        assert self.adapter.sender == SENDER_MOCK
        assert self.adapter.subject == SUBJECT_MOCK
        assert self.adapter.body == BODY_MOCK
        assert self.adapter.to == TO_MOCK
        assert self.adapter.cc == CC_MOCK
        assert self.adapter.bcc == BCC_MOCK
        assert self.adapter.attatchments == ATTATCHMENTS_MOCK
        assert isinstance(self.adapter.as_string(), str)
        assert self.adapter.recipients == TO_MOCK + CC_MOCK + BCC_MOCK

    def test_setter_name_sender(self):
        sender_name = "Example"
        sender_email = "example@email.com"
        self.adapter.sender = (sender_name, sender_email)
        assert sender_name in self.adapter.sender
        assert sender_email in self.adapter.sender

    @mock.patch("src.adapters.EmailMIMEAdapter.attach")
    @mock.patch("src.adapters.EmailMIMEAdapter._EmailMIMEAdapter__set_attatchment")
    @mock.patch("src.adapters.MIMEText")
    def test_as_string(self, mime_text_mock, set_attatchment_mock, attach_mock):
        set_attatchment_mock.return_value = None
        attach_mock.return_value = None

        payload = self.adapter.get_payload()

        assert mime_text_mock.called_once_with(BODY_MOCK)
        assert set_attatchment_mock.called_once_with(*ATTATCHMENTS_MOCK)
        assert attach_mock.called_once_with(mime_text_mock)
        assert isinstance(payload, list)
        assert len(payload) == 0

    @mock.patch("src.adapters.EmailMIMEAdapter.attach")
    @mock.patch("src.adapters.MIMEBase")
    def test_as_string(self, mime_base_mock, attach_mock):
        attach_mock.return_value = None
        mime_base_mock.set_payload.return_value = None
        mime_base_mock.add_header.return_value = None

        self.adapter.get_payload()

        assert mime_base_mock.called_once_with("application", "octet-stream")
        assert mime_base_mock.set_payload.called_once_with(ATTATCHMENTS_MOCK[0][0])
        assert mime_base_mock.add_header.called_once_with(
            "Content-Disposition", f"attachment; filename={ATTATCHMENTS_MOCK[0][1]}"
        )
        assert attach_mock.called_once_with(mime_base_mock)

    def test_sender_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.sender = None

    def test_subject_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.subject = None

    def test_to_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.to = None

    def test_cc_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.cc = None

    def test_bcc_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.bcc = None

    def test_body_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.body = None

    def test_attatchments_setter_invalid_type(self):
        with pytest.raises(AssertionError):
            self.adapter.attatchments = None
