# Generated by Django 4.0.4 on 2022-06-06 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0008_wybory_oddanych_glosow_alter_wybory_rodzaj_wyborow'),
    ]

    operations = [
        migrations.AddField(
            model_name='wyborca',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wybory',
            name='rodzaj_wyborow',
            field=models.CharField(choices=[('Prezydenckie', 'Prezydenckie'), ('Parlamentarne', 'Parlamentarne'), ('Starosty roku', 'Starosty roku'), ('Dziekana wydziału', 'Dziekana wydziału')], max_length=30),
        ),
    ]