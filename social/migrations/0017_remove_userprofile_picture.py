# Generated by Django 4.0.1 on 2022-10-05 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_tag_comment_tags_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
    ]