# Generated by Django 2.2.4 on 2019-10-11 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_web', '0004_delete_galary'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='date',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='month',
            field=models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
