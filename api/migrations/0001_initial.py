# Generated by Django 4.1.5 on 2023-01-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('video_id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('published_time', models.DateTimeField()),
                ('thumbnail_url', models.URLField()),
                ('channel_title', models.CharField(max_length=150)),
                ('channel_id', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
