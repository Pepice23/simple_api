# Generated by Django 3.1.5 on 2021-01-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logos')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]