# Generated by Django 3.2.4 on 2021-06-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210628_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Tags',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
