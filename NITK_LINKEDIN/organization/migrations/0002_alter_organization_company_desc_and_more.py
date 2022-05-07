# Generated by Django 4.0 on 2022-05-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='company_desc',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='company_size',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='company_type',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='contact_no',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='industry',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='locations',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website_url',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
