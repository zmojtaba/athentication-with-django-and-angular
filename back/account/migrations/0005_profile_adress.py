# Generated by Django 4.1.5 on 2023-01-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adress',
            field=models.ManyToManyField(related_name='profile_adress', to='account.adress'),
        ),
    ]
