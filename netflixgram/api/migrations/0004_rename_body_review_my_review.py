# Generated by Django 4.0.4 on 2022-05-26 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_rating_movie_average_rating_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='my_review',
        ),
    ]
