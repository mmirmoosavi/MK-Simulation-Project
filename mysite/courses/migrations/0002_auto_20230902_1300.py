# Generated by Django 2.2 on 2023-09-02 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-published_at']},
        ),
    ]
