# Generated by Django 3.1 on 2020-10-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200921_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]
