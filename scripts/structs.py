from dataclasses import dataclass
from typing import Optional


@dataclass
class Registration:
    name: str
    pronouns: Optional[str]
    institution: Optional[str]
    email: str
    website: Optional[str]
    attending_in_person: bool
    name_on_website: bool
    attending_pub: bool
    attending_dinner: bool
    dietary: str


@dataclass
class PublicRegistration:
    name: str
    institution: Optional[str]
    website: Optional[str]
    inperson: bool


@dataclass
class Namebadge:
    name: str
    institution: Optional[str]
    pronouns: Optional[str]
    institution2: Optional[str] = None