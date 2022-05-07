# Generated by Django 4.0.4 on 2022-05-07 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('org_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=50, null=True)),
                ('company_size', models.CharField(max_length=50, null=True)),
                ('company_type', models.CharField(max_length=50, null=True)),
                ('locations', models.CharField(max_length=200, null=True)),
                ('website_url', models.CharField(max_length=100, null=True)),
                ('contact_no', models.CharField(max_length=20, null=True)),
                ('company_desc', models.CharField(max_length=200, null=True)),
                ('year_of_pass_out', models.IntegerField(blank=True, default=2000, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default_org_profile.jpeg', upload_to='org_profile_uploads/')),
            ],
        ),
    ]
