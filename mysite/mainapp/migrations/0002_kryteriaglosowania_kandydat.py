# Generated by Django 4.0.4 on 2022-04-27 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kryteriaglosowania',
            name='kandydat',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='mainapp.kandydat'),
            preserve_default=False,
        ),
    ]
