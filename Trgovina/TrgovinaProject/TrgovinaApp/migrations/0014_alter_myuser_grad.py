# Generated by Django 5.0 on 2024-01-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrgovinaApp', '0013_rename_role_myuser_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='grad',
            field=models.CharField(max_length=30),
        ),
    ]
