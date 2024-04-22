# Generated by Django 3.2.25 on 2024-04-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myenvapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]