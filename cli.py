""" Command Line Interface for gedcom-benji"""

import os
import click
from gedcom_ajry import Gedcom

@click.command()
@click.argument('gedfile')
def gedcom(gedfile):
    ged = Gedcom(gedfile)
    ged.pretty_print()
    ged.us01_date_validate()
    ged.us02_birth_before_marriage()
    ged.us03_birth_before_death()
    ged.us05_marriage_before_death()
    ged.us06_divorce_before_death()
    ged.us11_no_bigamy()
    ged.us20_aunts_and_uncle()
    ged.us22_unique_ids()

