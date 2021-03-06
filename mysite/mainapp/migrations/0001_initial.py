# Generated by Django 4.0.4 on 2022-04-27 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kandydat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('miejscowosc', models.CharField(max_length=30)),
                ('wiek', models.PositiveIntegerField()),
                ('urzadNaJakiKandyduje', models.CharField(max_length=30)),
                ('poparcie', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KryteriaGlosowania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iluMoznaPoprzec', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Raport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frekwencja', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wyborca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('wiek', models.PositiveIntegerField()),
                ('czyUprawniony', models.BooleanField()),
            ],
        ),
    ]
