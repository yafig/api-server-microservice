from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str
    fullname: str
    password: str
    password_salt: str
    status: str = "Pending"

