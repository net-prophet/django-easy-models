# Generated by Django 2.0 on 2020-01-09 07:59

import EasyModels.base
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('age', models.IntegerField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, EasyModels.base.EasyLookupBase),
        ),
    ]
