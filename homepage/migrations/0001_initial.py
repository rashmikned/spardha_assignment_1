# Generated by Django 4.2.3 on 2023-08-20 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('institute', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=50)),
                ('Team_name', models.CharField(max_length=50)),
                ('player_first_name', models.CharField(max_length=50)),
                ('player_last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
