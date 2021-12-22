# Generated by Django 3.2.6 on 2021-12-22 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='ram', max_length=20)),
                ('last_name', models.CharField(default='dev', max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('guest', 'guest'), ('user', 'user')], default='user', max_length=20)),
                ('super_user', models.BooleanField(default=False)),
                ('dob', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
