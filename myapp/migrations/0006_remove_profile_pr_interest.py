# Generated by Django 3.1.7 on 2021-04-05 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_anouncement_anc_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pr_interest',
        ),
    ]
