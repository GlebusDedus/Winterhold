# Generated by Django 4.0 on 2021-12-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bolvanka',
        ),
    ]