# Generated by Django 2.0.2 on 2018-04-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0004_auto_20180412_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programminglanguage',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Linguagem'),
        ),
    ]