# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regionaldata', '0002_codes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Codes',
            new_name='Code',
        ),
    ]
