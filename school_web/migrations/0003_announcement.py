# Generated by Django 2.2.4 on 2019-10-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_web', '0002_thought'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField()),
            ],
        ),
    ]
