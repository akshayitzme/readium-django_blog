# Generated by Django 3.2.4 on 2021-06-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='readTime',
            field=models.IntegerField(default=0),
        ),
    ]
