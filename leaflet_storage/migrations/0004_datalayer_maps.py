# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaflet_storage', '0003_auto_20160910_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalayer',
            name='maps',
            field=models.ManyToManyField(related_name='_datalayer_maps_+', to='leaflet_storage.Map'),
        ),
    ]