# Generated by Django 5.0 on 2024-01-05 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrgovinaApp', '0005_narudzba_datum_narudzbe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='narudzba',
            old_name='detaljiOIsporuci',
            new_name='detalji_o_isporuci',
        ),
        migrations.RenameField(
            model_name='narudzba',
            old_name='nacinPlacanja',
            new_name='nacin_placanja',
        ),
    ]
