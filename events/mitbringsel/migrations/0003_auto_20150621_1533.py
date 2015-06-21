# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mitbringsel', '0002_auto_20150621_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitbringsel',
            name='comment',
            field=models.CharField(max_length=600, blank=True),
        ),
        migrations.AddField(
            model_name='mitbringsel',
            name='created_by',
            field=models.ForeignKey(editable=False, default=None, to=settings.AUTH_USER_MODEL, related_name='mitbringsel_created_by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mitbringsel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mitbringsel',
            name='modified_by',
            field=models.ForeignKey(editable=False, default=None, to=settings.AUTH_USER_MODEL, related_name='mitbringsel_modified_by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mitbringsel',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=None),
            preserve_default=False,
        ),
    ]
