# Generated by Django 4.0.4 on 2022-06-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_wybory_rodzaj_wyborow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wybory',
            name='rodzaj_wyborow',
            field=models.CharField(choices=[('Parlamentarne', 'Parlamentarne'), ('Prezydenckie', 'Prezydenckie'), ('Dziekana wydziału', 'Dziekana wydziału'), ('Starosty roku', 'Starosty roku')], max_length=30),
        ),
    ]
