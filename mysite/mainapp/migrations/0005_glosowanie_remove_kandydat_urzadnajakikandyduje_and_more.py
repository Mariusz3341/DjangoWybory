# Generated by Django 4.0.4 on 2022-05-08 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_kandydat_poparcie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glosowanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj_wyborow', models.CharField(choices=[('Prezydenckie', 'Prezydenckie'), ('Dziekana wydziału', 'Dziekana wydziału'), ('Starosty roku', 'Starosty roku'), ('Parlamentarne', 'Parlamentarne')], max_length=30)),
                ('rozpoczecie', models.DateTimeField()),
                ('zakonczenie', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='kandydat',
            name='urzadNaJakiKandyduje',
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='poparcie',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='raport',
            name='frekwencja',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='KryteriaGlosowania',
        ),
        migrations.AddField(
            model_name='kandydat',
            name='glosowanie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.glosowanie'),
        ),
        migrations.AddField(
            model_name='raport',
            name='glosowanie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.glosowanie'),
        ),
    ]
