# Generated by Django 2.2.1 on 2019-05-17 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]