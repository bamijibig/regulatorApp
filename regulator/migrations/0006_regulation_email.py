# Generated by Django 5.0.6 on 2024-07-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulator', '0005_remove_regulator_contact_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
