# Generated by Django 4.0.4 on 2022-06-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_wybory_rodzaj_wyborow'),
    ]

    operations = [
        migrations.AddField(
            model_name='wyborca',
            name='czy_glosowal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wyborca',
            name='czy_uprawniony',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wybory',
            name='rodzaj_wyborow',
            field=models.CharField(choices=[('Dziekana wydziału', 'Dziekana wydziału'), ('Parlamentarne', 'Parlamentarne'), ('Prezydenckie', 'Prezydenckie'), ('Starosty roku', 'Starosty roku')], max_length=30),
        ),
    ]
