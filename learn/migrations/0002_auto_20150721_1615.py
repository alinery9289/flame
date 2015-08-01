# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('authcode', models.CharField(max_length=32, unique=True, serialize=False, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=45)),
                ('userid', models.CharField(unique=True, max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('userstorage', models.IntegerField(max_length=8)),
                ('secretkey', models.CharField(max_length=45, unique=True, null=True, blank=True)),
                ('outdate', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
