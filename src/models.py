from dataclasses import dataclass, field
from typing import List

@dataclass
class EmailMime:
    sender: str
    subject: str
    body: str
    to: List[str] = field(default_factory=list)
    cc: List[str] = field(default_factory=list)
    bcc: List[str] = field(default_factory=list)
    attatchment: bytes = None

    @property
    def recipients(self) -> List[str]:
        return self.to + self.cc + self.bcc
