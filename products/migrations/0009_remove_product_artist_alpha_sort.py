# Generated by Django 3.2.4 on 2021-07-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210629_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Artist_Alpha_Sort',
        ),
    ]