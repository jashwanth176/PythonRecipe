# Generated by Django 5.1 on 2024-09-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_shoppinglistitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
