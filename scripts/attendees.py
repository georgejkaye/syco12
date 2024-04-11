import csv
import sys

from typing import Optional
from dataclasses import asdict

import yaml

from scripts.structs import Namebadge, PublicRegistration, Registration


if len(sys.argv) != 4:
    print(
        f"Usage: python {sys.argv[0]} <registration csv> <website output yaml> <namebadges output yaml>"
    )
    exit(1)

registration_csv = sys.argv[1]
website_output_file = sys.argv[2]
namebadge_output_file = sys.argv[3]


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
                row[1].strip(),
                string_to_optional(row[2].strip()),
                string_to_optional(row[3].strip()),
                row[4].strip(),
                string_to_optional(row[10].strip()),
                yesno_to_bool(row[5]),
                yesno_to_bool(row[6]),
                yesno_to_bool(row[7]),
                yesno_to_bool(row[8]),
                row[11],
            )
        )

public_registrations: list[PublicRegistration] = []
namebadges: list[Namebadge] = []

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
    if registration.attending_in_person:
        namebadges.append(
            Namebadge(
                registration.name, registration.institution, registration.pronouns
            )
        )

sorted_public_registrations = sorted(public_registrations, key=lambda r: r.name)
sorted_public_registration_dicts = [
    asdict(registration) for registration in sorted_public_registrations
]
namebadge_dicts = [
    asdict(namebadge) for namebadge in namebadges
]

with open(website_output_file, "w") as f:
    yaml.dump(sorted_public_registration_dicts, f, encoding="utf8", allow_unicode=True)

with open(namebadge_output_file, "w") as f:
    yaml.dump(namebadge_dicts, f, encoding="utf8", allow_unicode=True)
