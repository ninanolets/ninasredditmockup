# Generated by Django 3.1 on 2020-09-17 19:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subreddits', '0002_subreddit_pub_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(default='')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('subreddit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subreddits.subreddit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]