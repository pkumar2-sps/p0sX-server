# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_item_can_have_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]