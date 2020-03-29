from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str
    fullname: str
    password: str
    password_salt: str
    status: str
