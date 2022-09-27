# Generated by Django 3.2.7 on 2021-12-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20211124_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField(verbose_name='Enter Questions')),
                ('Answer', models.TextField(verbose_name='Enter Answers')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
    ]
