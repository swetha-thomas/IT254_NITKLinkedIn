# Generated by Django 4.0 on 2022-05-08 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='num_alumni',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
