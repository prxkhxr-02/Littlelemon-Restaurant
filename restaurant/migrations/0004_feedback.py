# Generated by Django 4.2.3 on 2023-08-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feekback', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]