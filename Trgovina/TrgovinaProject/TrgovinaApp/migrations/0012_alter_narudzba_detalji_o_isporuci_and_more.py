# Generated by Django 5.0 on 2024-01-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrgovinaApp', '0011_proizvod_boja_proizvod_brend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narudzba',
            name='detalji_o_isporuci',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='narudzba',
            name='nacin_plaćanja',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proizvod',
            name='boja',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='proizvod',
            name='brend',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proizvod',
            name='cijena',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='proizvod',
            name='grad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proizvod',
            name='količina',
            field=models.IntegerField(default=1),
        ),
    ]
