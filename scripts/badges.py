import yaml
import sys

from structs import Namebadge

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <namebadges yaml> <output latex>")
    exit(1)

namebadges_file = sys.argv[1]
latex_output = sys.argv[2]

badges : list[Namebadge] = []

with open(namebadges_file, "r") as f:
    raw_badges = yaml.safe_load(f)
    for badge in raw_badges:
        if badge.get("institution2") is None:
            institution2 = None
        else:
            institution2 = badge["institution2"]
        badges.append(Namebadge(badge["name"], badge["institution"], badge["pronouns"], institution2))


with open(latex_output, "w") as f:
    for badge in badges:
        if badge.institution:
            institution_arg = f"{{{badge.institution}}}"
        else:
            institution_arg = "{}"
        if badge.institution2:
            institution2_arg = f"{{{badge.institution2}}}"
        else:
            institution2_arg = "{}"
        if badge.pronouns:
            pronouns_arg = f"{{{badge.pronouns}}}"
        else:
            pronouns_arg = "{}"
        f.write(f"\\badge{{{badge.name}}}{pronouns_arg}{institution_arg}{institution2_arg}\n")