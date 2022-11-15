# Generated by Django 4.1.3 on 2022-11-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_turn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='score',
        ),
        migrations.AddField(
            model_name='player',
            name='draws',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='hand',
            field=models.CharField(choices=[('ROCK', 0), ('PAPER', 1), ('SCISSORS', 2)], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='played',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
