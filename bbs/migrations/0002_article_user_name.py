# Generated by Django 2.1.5 on 2020-05-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
