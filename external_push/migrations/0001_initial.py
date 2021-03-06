# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-02 21:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gravity', '0002_tilt_refactor'),
        ('app', '0009_auto_20180709_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericPushTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Unique name for this push target', max_length=48, unique=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('disabled', 'Disabled')], default='active', help_text='Status of this push target', max_length=24)),
                ('push_frequency', models.IntegerField(choices=[(59, '1 minute'), (119, '2 minutes'), (299, '5 minutes'), (599, '10 minutes'), (899, '15 minutes'), (1799, '30 minutes'), (3599, '1 hour')], default=900, help_text='How often to push data to the target')),
                ('api_key', models.CharField(blank=True, default='', help_text='API key required by the push target (if any)', max_length=256)),
                ('brewpi_push_selection', models.CharField(choices=[('all', 'All Active Sensors/Devices'), ('list', 'Specific Sensors/Devices'), ('none', 'Nothing of this type')], default='all', help_text='How the BrewPi devices to push are selected', max_length=12)),
                ('gravity_push_selection', models.CharField(choices=[('all', 'All Active Sensors/Devices'), ('list', 'Specific Sensors/Devices'), ('none', 'Nothing of this type')], default='all', help_text='How the gravity sensors to push are selected', max_length=12)),
                ('target_type', models.CharField(choices=[('http (post)', 'HTTP/HTTPS'), ('tcp', 'TCP (Telnet/Socket)')], default='http (post)', help_text='Protocol to use to connect to the push target', max_length=24)),
                ('target_host', models.CharField(blank=True, default='http://127.0.0.1/', help_text='The URL to push to (for HTTP/HTTPS) or hostname/IP address (for TCP)', max_length=256)),
                ('target_port', models.IntegerField(default=80, help_text='The port to use (not used for HTTP/HTTPS)', validators=[django.core.validators.MinValueValidator(10, 'Port must be 10 or higher'), django.core.validators.MaxValueValidator(65535, 'Port must be 65535 or lower')])),
                ('data_format', models.CharField(choices=[('generic', 'All Data (Generic)'), ('brewersfriend', 'Brewers Friend')], default='generic', help_text='The data format to send to the push target', max_length=24)),
                ('last_triggered', models.DateTimeField(default=django.utils.timezone.now, help_text='The last time we pushed data to this target')),
                ('brewpi_to_push', models.ManyToManyField(help_text="BrewPi Devices to push (ignored if 'all' devices selected)", related_name='push_targets', to='app.BrewPiDevice')),
                ('gravity_sensors_to_push', models.ManyToManyField(help_text="Gravity Sensors to push (ignored if 'all' sensors selected)", related_name='push_targets', to='gravity.GravitySensor')),
            ],
            options={
                'verbose_name': 'Generic Push Target',
                'verbose_name_plural': 'Generic Push Targets',
            },
        ),
    ]
