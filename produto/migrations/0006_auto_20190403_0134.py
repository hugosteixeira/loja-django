# Generated by Django 2.1.7 on 2019-04-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20190403_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(default='none.png', upload_to='media'),
        ),
    ]
