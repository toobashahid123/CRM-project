# Generated by Django 4.2.2 on 2023-09-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementprogram', '0002_member_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='emailid',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
