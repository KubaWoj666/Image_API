# Generated by Django 4.2.5 on 2023-10-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='account_tires',
            new_name='account_tiers',
        ),
    ]