# Generated by Django 4.0.4 on 2022-06-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_rename_czyuprawniony_wyborca_czy_uprawniony_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wybory',
            name='rodzaj_wyborow',
            field=models.CharField(choices=[('Starosty roku', 'Starosty roku'), ('Parlamentarne', 'Parlamentarne'), ('Dziekana wydziału', 'Dziekana wydziału'), ('Prezydenckie', 'Prezydenckie')], max_length=30),
        ),
    ]
