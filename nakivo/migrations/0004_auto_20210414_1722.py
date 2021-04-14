# Generated by Django 3.1.7 on 2021-04-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakivo', '0003_auto_20210409_0147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='middle_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
        migrations.AddField(
            model_name='profile',
            name='password1',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
