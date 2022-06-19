# Generated by Django 4.0.4 on 2022-05-16 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_glosowanie_wybory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='poparcie',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wybory',
            name='rodzaj_wyborow',
            field=models.CharField(choices=[('Dziekana wydziału', 'Dziekana wydziału'), ('Starosty roku', 'Starosty roku'), ('Parlamentarne', 'Parlamentarne'), ('Prezydenckie', 'Prezydenckie')], max_length=30),
        ),
    ]