from dataclasses import dataclass


@dataclass
class User(object):
    name: str
    email: str


@dataclass
class Request(object):
    userId: str
    ip: str
