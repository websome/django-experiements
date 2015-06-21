# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mitbringsel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MitbringselType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='mitbringsel',
            name='definitiv',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mitbringsel',
            name='type',
            field=models.ForeignKey(to='mitbringsel.MitbringselType'),
        ),
    ]
