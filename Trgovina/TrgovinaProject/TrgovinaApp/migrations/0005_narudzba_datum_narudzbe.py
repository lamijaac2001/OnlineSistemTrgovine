# Generated by Django 5.0 on 2024-01-05 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrgovinaApp', '0004_narudzba_detaljioisporuci_narudzba_nacinplacanja_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='narudzba',
            name='datum_narudzbe',
            field=models.DateField(blank=True, null=True),
        ),
    ]
