# Generated by Django 3.0.3 on 2020-03-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_web', '0011_announcement_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=10)),
                ('id2', models.CharField(max_length=10)),
                ('id3', models.CharField(max_length=10)),
                ('id4', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('answers', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
