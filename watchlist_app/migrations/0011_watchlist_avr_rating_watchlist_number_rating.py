# Generated by Django 5.1 on 2024-08-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0010_rename_reviewer_review_reviewer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avr_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
