# Generated by Django 3.1.1 on 2020-09-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200912_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]