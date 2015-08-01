# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authcode', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=45)),
                ('userid', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('userstorage', models.IntegerField(max_length=8)),
                ('secretkey', models.CharField(max_length=45)),
                ('outdate', models.DateTimeField()),
            ],
        ),
    ]
