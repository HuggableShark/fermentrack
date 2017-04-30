# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_allow_null_device_beer_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewpidevice',
            name='prefer_connecting_via_udev',
            field=models.BooleanField(default=True, help_text='Prefer to connect to the device with the correct serial number instead of the serial_port'),
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='udev_serial_number',
            field=models.CharField(default='', help_text='USB Serial ID number for autodetection of serial port', max_length=255),
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='wifi_host_ip',
            field=models.CharField(default='', help_text='Cached IP address in case of mDNS issues (only used if connection_type is wifi)', max_length=46),
        ),
    ]