# Generated by Django 5.0.2 on 2024-03-04 08:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_account_identity'),
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('schoolawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schoolapp.schoolawaremodel')),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('schoolapp.schoolawaremodel',),
        ),
    ]
