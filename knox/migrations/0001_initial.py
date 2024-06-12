# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

from knox.settings import knox_settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(knox_settings.USER_MODEL or settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('key', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=knox_settings.USER_MODEL or settings.AUTH_USER_MODEL, related_name='auth_token_set', on_delete=models.CASCADE)),
            ],
        ),
    ]
