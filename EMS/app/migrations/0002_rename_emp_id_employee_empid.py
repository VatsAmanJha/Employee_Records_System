# Generated by Django 4.2.3 on 2023-07-21 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emp_id',
            new_name='empid',
        ),
    ]