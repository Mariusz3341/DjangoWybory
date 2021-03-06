# Generated by Django 4.0.4 on 2022-04-27 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_kryteriaglosowania_kandydat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='urzadNaJakiKandyduje',
            field=models.CharField(blank=True, choices=[('Prezydent', 'Prezydent'), ('Poseł', 'Poseł'), ('Starosta roku', 'Starosta roku'), ('Dziekan wydziału', 'Dziekan wydziału')], max_length=30),
        ),
        migrations.AlterField(
            model_name='kryteriaglosowania',
            name='kandydat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.kandydat'),
        ),
    ]
