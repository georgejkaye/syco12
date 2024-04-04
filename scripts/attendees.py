import csv
import sys

from typing import Optional
from dataclasses import asdict, dataclass

import yaml


if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <registration csv> <output yaml>")
    exit(1)

registration_csv = sys.argv[1]
output_file = sys.argv[2]


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


registrations: list[Registration] = []


def yesno_to_bool(resp: str) -> bool:
    return resp == "Yes"


def string_to_optional(resp: str) -> Optional[str]:
    if resp == "":
        return None
    return resp


with open(registration_csv, "r") as f:
    reader = csv.reader(f, delimiter=",")
    # Skip header
    next(reader, None)
    for row in reader:
        registrations.append(
            Registration(
                row[1],
                string_to_optional(row[2]),
                string_to_optional(row[3]),
                row[4],
                string_to_optional(row[10]),
                yesno_to_bool(row[5]),
                yesno_to_bool(row[6]),
                yesno_to_bool(row[7]),
                yesno_to_bool(row[8]),
                row[11],
            )
        )

public_registrations: list[PublicRegistration] = []

for registration in registrations:
    if registration.name_on_website:
        public_registrations.append(
            PublicRegistration(
                registration.name,
                registration.institution,
                registration.website,
                registration.attending_in_person,
            )
        )

sorted_public_registrations = sorted(public_registrations, key=lambda r: r.name)
sorted_public_registration_dicts = [asdict(registration) for registration in sorted_public_registrations]

with open(output_file, "w") as f:
    yaml.dump(sorted_public_registration_dicts, f, encoding="utf8", allow_unicode=True)