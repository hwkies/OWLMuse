from typing_extensions import TypedDict, NotRequired
from datetime import datetime

class User(TypedDict):
    username: str
    email: str
    password: str
    created_at: NotRequired[datetime]

class SafeUser(TypedDict):
    username: str
    email: str
    created_at: NotRequired[datetime]

class PartialUser(TypedDict):
    username: str
    email: NotRequired[str]
    password: NotRequired[str]