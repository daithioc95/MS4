# Generated by Django 3.2.4 on 2021-06-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210628_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Is_Highlight',
            field=models.BooleanField(default=False),
        ),
    ]
