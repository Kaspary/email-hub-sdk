from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


class EmailMIMEAdapter(MIMEMultipart):
    __body: str
    __attatchments: list[tuple[bytes, str]]

    def __init__(
        self,
        sender: str,
        subject: str,
        body: str,
        sender_name: str = None,
        to: list[str] = [],
        cc: list[str] = [],
        bcc: list[str] = [],
        attatchments: list[tuple[bytes, str]] = [],
    ) -> None:
        super().__init__()
        self["Date"] = formatdate(localtime=True)
        self.sender = sender
        self.subject = subject
        self.body = body
        self.sender_name = sender_name
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.attatchments = attatchments

    @property
    def sender(self):
        return self["From"]

    @sender.setter
    def sender(self, value: str | tuple[str, str]):
        assert isinstance(
            value, (str, tuple)
        ), f"sender expect string or tuple of strings type, but got {type(value)}"

        del self["From"]
        if isinstance(value, str):
            self["From"] = value
        elif isinstance(value, tuple):
            self["From"] = "{0} <{1}>".format(*value)

    @property
    def subject(self):
        return self["Subject"]

    @subject.setter
    def subject(self, value: str):
        assert isinstance(
            value, str
        ), f"subject expect string type, but got {type(value)}"
        del self["Subject"]
        self["Subject"] = value

    @property
    def to(self):
        return self["To"].split(COMMASPACE) or []

    @to.setter
    def to(self, value: list[str]):
        assert isinstance(
            value, list
        ), f"to expect list of strings type, but got {type(value)}"
        del self["To"]
        self["To"] = COMMASPACE.join(value)

    @property
    def cc(self):
        return self["Cc"].split(COMMASPACE) or []

    @cc.setter
    def cc(self, value: list[str]):
        assert isinstance(
            value, list
        ), f"cc expect list of strings type, but got {type(value)}"
        del self["Cc"]
        self["Cc"] = COMMASPACE.join(value)

    @property
    def bcc(self):
        return self["Bcc"].split(COMMASPACE) or []

    @bcc.setter
    def bcc(self, value: list[str]):
        assert isinstance(value, list), f"bcc expect a list type, but got {type(value)}"
        del self["Bcc"]
        self["Bcc"] = COMMASPACE.join(value)

    @property
    def recipients(self):
        return self.to + self.cc + self.bcc

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value: str):
        assert isinstance(value, str), f"body expect string type, but got {type(value)}"
        self.__body = value

    @property
    def attatchments(self):
        return self.__attatchments

    @attatchments.setter
    def attatchments(self, value: list[tuple[bytes, str]]):
        assert isinstance(
            value, list
        ), f"attatchments expect a list type, but got {type(value)}"
        self.__attatchments = value

    def get_payload(self, *args, **kwargs):
        self._payload = []
        self.attach(MIMEText(self.body))
        for attatchment in self.attatchments:
            self.__set_attatchment(*attatchment)
        return super().get_payload(*args, **kwargs)

    def __set_attatchment(self, data: bytes, filename: str):
        attatchment = MIMEBase("application", "octet-stream")
        attatchment.set_payload(data)
        attatchment.add_header(
            "Content-Disposition", f"attachment; filename={filename}"
        )
        self.attach(attatchment)
