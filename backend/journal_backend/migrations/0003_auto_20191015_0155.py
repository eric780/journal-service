# Generated by Django 2.2.6 on 2019-10-15 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_backend', '0002_auto_20191015_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentrymodel',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalentrymodel',
            name='date',
            field=models.CharField(default='0000-00-00', max_length=10),
            preserve_default=False,
        ),
    ]
