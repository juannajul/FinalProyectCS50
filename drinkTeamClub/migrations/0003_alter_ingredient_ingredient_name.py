# Generated by Django 3.2.2 on 2021-05-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkTeamClub', '0002_auto_20210506_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
