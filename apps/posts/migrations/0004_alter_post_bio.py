# Generated by Django 4.2.4 on 2023-08-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_content_post_bio_remove_post_title_post_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]